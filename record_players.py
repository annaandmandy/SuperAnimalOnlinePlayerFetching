import requests
from datetime import datetime

API_URL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
APPID = 367520  # Hollow Knight

def fetch():
    try:
        r = requests.get(API_URL, params={"appid": APPID})
        count = r.json()["response"]["player_count"]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("player_data.csv", "a") as f:
            f.write(f"{now},{count}\n")
        print(f"[{now}] Players: {count}")
    except Exception as e:
        print("Error:", e)

fetch()
