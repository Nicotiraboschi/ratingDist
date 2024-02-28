import pandas as pd
import chessdotcom
from concurrent.futures import ThreadPoolExecutor, as_completed
from chessdotcom import Client
import os
import time
import re

start_time = time.time()
print ('Starting at', time.strftime('%X %x %Z'), start_time)

Client.request_config["headers"]["User-Agent"] = (
    "I wanna analyse rating distribution among chess.com active players, and create a database for some months."
    "Contact me at nico.tiraboschi@gmail.com"
)

if not os.path.exists('csv/setNamesToCheck.csv'):
    set_names_to_check = set()
else:
    set_names_to_check = set(pd.read_csv('csv/setNamesToCheck.csv').iloc[:, 0].tolist())

if not os.path.exists('csv/namesChecked.csv'):
    set_names_checked = set()
else:
    set_names_checked = set(pd.read_csv('csv/namesChecked.csv').iloc[:, 0].tolist())

if not os.path.exists('csv/namesNotFound.csv'):
    set_names_not_found = set()
else:
    set_names_not_found = set(pd.read_csv('csv/namesNotFound.csv').iloc[:, 0].tolist())


def fetch_player_games(player_name):
    try:
        games = chessdotcom.client.get_player_games_by_month(player_name, "2024", "01").json['games']
    except:
        set_names_not_found.add(player_name)
        return
    
    new_games = []

    for game in games:
        if game["rules"] == "chess":
            
            if game["white"]["username"] in selected_names:
                opponent_name = game["black"]["username"]
            else:
                opponent_name = game["white"]["username"]
            
            if opponent_name in set_names_checked:
                continue
            if opponent_name not in set_names_not_found and opponent_name not in set_names_to_check:
                set_names_to_check.add(opponent_name)
            
            result = 1 if game["white"]["result"] == "win" else -1 if game["black"]["result"] == "win" else 0
            new_game = {

                "url": game['url'].split('/')[-1],
                "moves": game["tcn"],
                "result": result,
                
                "white_rating": game["white"]["rating"],
                "white_username": game["white"]["username"],
                "white_id": game["white"]["uuid"],
                
                "black_rating": game["black"]["rating"],
                "black_username": game["black"]["username"],
                "black_id": game["black"]["uuid"],
                
                "rated": game["rated"],
                "endtime": game["end_time"],
                "timecontrol": game["time_control"],        
            }
        else:
            continue
        new_games.append(new_game)


    set_names_checked.add(player_name)
    list_all_games.extend(new_games)
    
                   
list_all_games = []

# Iterate over players using ThreadPoolExecutor
max_threads = 1000

while set_names_to_check:
    with ThreadPoolExecutor(max_threads) as executor:
        selected_names = list(set_names_to_check)[:max_threads]
                
        set_names_to_check -= set(selected_names)

        futures = {executor.submit(fetch_player_games, player_name):
                player_name for player_name in selected_names}

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error fetching games: {e}")
                
                        
        names_checked_pd = pd.DataFrame(set_names_checked)
        names_checked_pd.to_csv('csv/namesChecked.csv', header=["Name"], index=False)
        
        names_to_check_pd = pd.DataFrame(set_names_to_check)
        names_to_check_pd.to_csv('csv/setNamesToCheck.csv', header=["Name"], index=False)
        
        names_not_found_pd = pd.DataFrame(set_names_not_found)
        names_not_found_pd.to_csv('csv/namesNotFound.csv',header=["Name"], index=False)
        
        
        size_limit_gb = 1
        size_limit_bytes = size_limit_gb * 1024 * 1024 * 1024  # 1 gigabyte in bytes
            
            
        def find_largest_number_in_files(folder_path):
            # Get a list of files in the folder
            files = os.listdir(folder_path)

            # Define a regular expression to extract numbers from filenames
            pattern = re.compile(r'games_(\d+)')

            # Extract numbers from filenames and find the largest one
            largest_number = max(
                [int(pattern.search(file).group(1)) for file in files if pattern.search(file)],
                default=None
            )

            return largest_number

        # Example usage
        largest_number = find_largest_number_in_files('./games')

        if largest_number is not None:
            if os.path.getsize(f'./games/games_{largest_number}.csv') > size_limit_bytes:
                games_file_number = largest_number + 1
                games_file_name = f'games_{games_file_number}.csv'
            else:
                games_file_number = largest_number
                games_file_name = f'games_{games_file_number}.csv'
        else:
            games_file_number = 1
            games_file_name = f'games_{games_file_number}.csv'
 
                     
        if len(list_all_games):
            games_pd = pd.DataFrame(list_all_games)
        
            games_path = f'games/{games_file_name}'
            if not os.path.isfile(games_path):
                games_pd.to_csv(f'games/{games_file_name}', header=True, index=False)
            else:
                games_pd.to_csv(f'games/{games_file_name}', mode='a', header=False, index=False)
                
            # REVIEW
            print("--- %s seconds ---" % (time.time() - start_time), f"saved {len(list_all_games)} games")
            
            with open('time.txt', 'a') as f:
                f.write(f"\n{int(time.time() - start_time)}\n")
            
            # END REVIEW  
                    
            list_all_games = []
        