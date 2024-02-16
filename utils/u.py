# MAIN FIX GAMES_ID FILE
# import csv
# import pandas as pd

# with open('games_id.csv', newline='') as input_file:
#     reader = csv.reader(input_file)
#     games_id_list = []
#     for row in reader:
#         new_row = []
#         new_row = "".join(row)
#         games_id_list.append(new_row)
#     pd.DataFrame(games_id_list).to_csv("games_id_list.csv", header=None, index=None)

# MAIN MOVE CSV FILES INTO CSV FOLDER
# import os
# import shutil

# # Crea la cartella "csv" se non esiste già
# if not os.path.exists('csv'):
#     os.makedirs('csv')

# # Sposta tutti i file CSV nella cartella "csv"
# for filename in os.listdir('.'):
#     if filename.endswith('.csv'):
#         shutil.move(filename, 'csv')

# MAIN GET DATE NOW TO COMPARE RESULTS
# from datetime import datetime

# current_dateTime = datetime.now()

# print(current_dateTime)

# now_1 = "2024-01-22 02:26:09.318755"
# number_names_checked = 800
# games: 321902

# now_2 = "2024-01-22 14:09:38.276404"
# number_names_checked = 7343
# games: 624638

# now_3 = "2024-01-22 21:15:21.618689"
# number_names_checked = 8900
# games: 1022838

# now_4 = "2024-01-22 21:18:10.734793"
# number_names_checked = 8950
# games: 1034719

# now_5 = "2024-01-23 13:20:30.736548"
# number_names_checked = 100
# games: 19789


# MAIN CHECK DUPLICATES IN GAMES_ID
# import pandas as pd

# # Replace 'your_file.csv' with the actual file containing the names
# list = pd.read_csv('../csv/namesToCheck.csv').iloc[:, 0].tolist()
# # list = pd.read_csv('../csv/setNamesToCheck.csv').iloc[:, 0].tolist()

# # Find duplicates
# is_duplicate = pd.Series(list).duplicated()
# duplicates = [list[i] for i, duplicate in enumerate(is_duplicate) if duplicate]

# if duplicates:
#     print('Duplicate names found:')
#     print(len(duplicates), "duplicates found", len(list))
# else:
#     print(len(list))
#     print('No duplicate names found.')



# MAIN CHECK DUPLICATES IN NAME CHECKED

# import pandas as pd

# # Load data from the three files
# name_series_1 = pd.read_csv('../csv/setNamesToCheck.csv').iloc[:, 0].tolist()
# name_series_2 = pd.read_csv('../csv/namesChecked.csv').iloc[:, 0].tolist()
# name_series_3 = pd.read_csv('../csv/setNewNames.csv').iloc[:, 0].tolist()

# # Convert lists to Pandas Series
# series_1 = pd.Series(name_series_1)
# series_2 = pd.Series(name_series_2)
# series_3 = pd.Series(name_series_3)

# # Find duplicates
# duplicates_1_2 = series_1[series_1.isin(series_2)]
# duplicates_1_3 = series_1[series_1.isin(series_3)]
# duplicates_2_3 = series_2[series_2.isin(series_3)]

# # Combine duplicates from different pairs
# all_duplicates = pd.concat([pd.Series(duplicates_1_2), pd.Series(duplicates_1_3), pd.Series(duplicates_2_3)]).unique()

# if all_duplicates.size > 0:
#     print(f'Duplicates found: some')
# else:
#     print('No duplicates found.')





# MAIN REMOVE FILES IN A FOLDER
# import os

# folder_path = '../games'

# # Get the list of files in the folder
# files = os.listdir(folder_path)

# # Iterate over the files and remove each one
# for file in files:
#     file_path = os.path.join(folder_path, file)
#     if os.path.isfile(file_path):
#         os.remove(file_path)



# MAIN SELEcT TEXT AFTER A WORD
# def delete_text_before_word(file_path, target_word):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     # Find the position of the target word
#     position = content.find(target_word)

#     if position != -1:
#         # Delete the text before the target word
#         new_content = content[position:]
        
#         # Write the updated content back to the file
#         with open(file_path, 'w') as file:
#             file.write(new_content)

#         print(f'Selected text before "{target_word}" deleted successfully.')
#     else:
#         print(f'Target word "{target_word}" not found in the file.')

# # Example usage
# file_path = '../games/games_2.csv'
# target_word = '99689641475'
# delete_text_before_word(file_path, target_word)
# MAIN add column Name
# import pandas as pd
# file_path = '../csv/setNamesToCheck.csv'
# df = pd.read_csv(file_path, header=None, names=['Name'])
# df.to_csv(file_path, index=False)

# MAIN GET MAX FILE NUMBER 
# import os

# # Percorso della directory
# directory_path = '../games'

# # Lista dei file nella directory
# files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# # Funzione per estrarre il numero dalla stringa
# def extract_number(file_name):
#     try:
#         return int(file_name.split('_')[1].split('.csv')[0])
#     except (IndexError, ValueError):
#         return 0

# # Inizializza la variabile per il massimo valore
# max_value = 0

# # Itera attraverso i file e trova il massimo valore
# for file_name in files:
#     current_value = extract_number(file_name)
#     if current_value > max_value:
#         max_value = current_value

# print("Il numero più grande nei nomi dei file è:", max_value)
# MAIN COUNT ROWS
# with open('../games/games_0.csv', 'r') as file:
#     line_count = sum(1 for line in file)

# print(f'Number of lines: {line_count}')

# MAIN merge names to check with new names
# import pandas as pd
# set_names_to_check = set(pd.read_csv('../csv/namesToCheck.csv').iloc[:, 0].tolist())
# set_new_names = set(pd.read_csv('../csv/namesChecked.csv').iloc[:, 0].tolist())
# set_names_to_check.update(set_new_names)
# df_names_to_check = pd.DataFrame(list(set_names_to_check))
# df_names_to_check.to_csv('../csv/namesToCheck.csv', header=["Name"], index=False)


# MAIN CHECK EMPTY COLUMN
# import pandas as pd

# # Assuming 'your_file.csv' is the name of your CSV file
# df = pd.read_csv('../games/games_1.csv')

# # Assuming 'column_name' is the name of the column you want to check
# empty_rows = df[df['moves'].isnull()]

# # Display the rows where the column is empty
# print(empty_rows)
