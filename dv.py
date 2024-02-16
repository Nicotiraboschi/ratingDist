import pandas as pd
import chessdotcom
from concurrent.futures import ThreadPoolExecutor, as_completed
from chessdotcom import Client
import time
import re


# start_time = time.time()

# Client.request_config["headers"]["User-Agent"] = (
#     "I'm trying to get games of certain rating range."
#     "Contact me at nico.tiraboschi@gmail.com"
# )

# games_file_number = 1
# games_file_name = f'games_{games_file_number}.csv'

# set_names_checked = set()
# set_names_not_found = set()
# set_names_to_check = set(pd.read_csv('csv/namesToCheck.csv').iloc[:, 0].tolist())
# range_0_games = []
# range_1_games = []
# range_2_games = []

# def fetch_player_games(player_name):
#     try:
#         games = chessdotcom.client.get_player_games_by_month(player_name, "2024", "01").json['games']
#     except:
#         set_names_not_found.add(player_name)
#         return
    


#     for game in games:
#         if game["rules"] == "chess":
            
#             if game["white"]["username"] in selected_names:
#                 opponent_name = game["black"]["username"]
#             else:
#                 opponent_name = game["white"]["username"]
            
#             if opponent_name in set_names_checked:
#                 continue
#             if opponent_name not in set_names_not_found and opponent_name not in set_names_to_check:
#                 set_names_to_check.add(opponent_name)
            
#             white_rating = game["white"]["rating"]
#             black_rating = game["black"]["rating"]
            
#             if white_rating > 1700 or black_rating > 1700 or white_rating < 400 or black_rating < 400:
#                 break
#             if (white_rating < 800 or white_rating > 1400) and (black_rating < 800 or black_rating > 1400):
#                 continue
                
#             new_game = {
#                 game["pgn"]        
#             }
#         else:
#             continue
        
#         800-1000 / 1000-1200 / 1200-1400

#         if (white_rating > 800 and white_rating < 1000) or (black_rating > 800 and black_rating < 1000):
#             range_0_games.append(new_game)
#         elif (white_rating > 1000 and white_rating < 1200) or (black_rating > 1000 and black_rating < 1200):
#             range_1_games.append(new_game)
#         elif (white_rating > 1200 and white_rating < 1400) or (black_rating > 1200 and black_rating < 1400):
#             range_2_games.append(new_game)


#     set_names_checked.add(player_name)
    
                   
# # Iterate over players using ThreadPoolExecutor
# max_threads = 50

# while len(range_0_games) < 3000 or len(range_1_games) < 3000 or len(range_2_games) < 3000:
#     with ThreadPoolExecutor(max_threads) as executor:
#         selected_names = list(set_names_to_check)[:max_threads]
        
        
        
#         set_names_to_check -= set(selected_names)
#         print(f'extracted names: the list is now long {len(set_names_to_check)}')


#         futures = {executor.submit(fetch_player_games, player_name):
#                 player_name for player_name in selected_names}

#         for future in as_completed(futures):
#             try:
#                 future.result()
#             except Exception as e:
#                 print(f"Error fetching games: {e}")
                
                        
# range_0_games_pd = pd.DataFrame(range_0_games)  
# range_0_games_pd.to_csv((f'ranges/range_0.csv'), header=["Pgn"], index=False)

# range_1_games_pd = pd.DataFrame(range_1_games)
# range_1_games_pd.to_csv((f'ranges/range_1.csv'), header=["Pgn"], index=False)

# range_2_games_pd = pd.DataFrame(range_2_games)
# range_2_games_pd.to_csv((f'ranges/range_2.csv'), header=["Pgn"], index=False)
                

filename_0 = 'ranges/range_0.csv'
filename_1 = 'ranges/range_1.csv'
filename_2 = 'ranges/range_2.csv'

def replace(filename):
    with open(filename, 'r') as f:
        content = f.read()
        modified_content = re.sub(r'\"\"+', '"', content)

    with open(filename, 'w') as f:
        f.write(modified_content)

replace(filename_0)
replace(filename_1)
replace(filename_2)

# # REVIEW
# print("--- %s seconds ---" % (time.time() - start_time), f"dowloading games from {len(selected_names)} names")
# start_time = time.time()
# # END REVIEW