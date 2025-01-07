import requests
import random
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

def create_teams():
    teams = [
        {"nazvanie": "Team A", "vuz": "University X", "gorod": "City Y"},
        {"nazvanie": "Team B", "vuz": "University Y", "gorod": "City Z"},
        {"nazvanie": "Team C", "vuz": "University Z", "gorod": "City W"},
    ]
    for team in teams:
        response = requests.post(f"{BASE_URL}/teams", json=team)
        print(f"Added team: {response.json()}")

def create_games():
    start_date = datetime(2025, 1, 1)
    games = [
        {"nazvanie": f"Game {i+1}", 
         "liga": random.randint(1, 3), 
         "data": (start_date + timedelta(days=i*7)).strftime('%Y-%m-%d'), 
         "mesto": f"City {chr(65 + i)}"} 
        for i in range(10)
    ]
    for game in games:
        response = requests.post(f"{BASE_URL}/games", json=game)
        print(f"Added game: {response.json()}")

def create_results():
    teams = requests.get(f"{BASE_URL}/teams").json()
    games = requests.get(f"{BASE_URL}/games").json()

    if not teams or not games:
        print("Teams or games not found. Please add them first.")
        return

    for game in games:
        for team in teams:
            result = {
                "mesto": random.randint(1, 10),
                "balli": random.randint(0, 100),
                "vixod_v_sled_etap": "yes" if random.random() > 0.5 else "no",
                "komanda_id": team['id'],
                "igra_id": game['id']
            }
            response = requests.post(f"{BASE_URL}/results", json=result)
            print(f"Added result: {response.json()}")

if __name__ == "__main__":
    print("Adding teams...")
    create_teams()
    print("Adding games...")
    create_games()
    print("Adding results...")
    create_results()
