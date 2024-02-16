import chessdotcom
import pandas as pd

from chessdotcom import Client

Client.request_config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
)

i = 0

names_list = []

countries = pd.read_csv("listCountries.csv")['Country']
for country in countries:
    try:
        players = chessdotcom.get_country_players(country).json
        for player in players["players"]:
            names_list.append(player)
            i += 1
    except Exception as e:
        continue
    
df= pd.DataFrame({'Name': names_list})
df.to_csv('listNames.csv', index=False)

print(i)