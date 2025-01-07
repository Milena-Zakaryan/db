import requests
import random
from faker import Faker
BASE_URL = "http://localhost:5467"
fake = Faker()

def add_teams(count=10):
    url = f"{BASE_URL}/teams"
    for _ in range(count):
        data = {
            "nazvanie": fake.company(),
            "vuz": fake.university(),
            "gorod": fake.city(),
        }
        requests.post(url, json=data)

def add_games(count=10):
    url = f"{BASE_URL}/games"
    for _ in range(count):
        data = {
            "nazvanie": fake.word().capitalize(),
            "liga": random.randint(1, 5),
            "data": fake.date(),
            "mesto": fake.city(),
        }
        requests.post(url, json=data)

def add_results(count=10):
    teams = requests.get(f"{BASE_URL}/teams").json()
    games = requests.get(f"{BASE_URL}/games").json()
    url = f"{BASE_URL}/results"

    for _ in range(count):
        data = {
            "mesto": random.randint(1, len(teams)),
            "balli": random.randint(0, 100),
            "vixod_v_sled_etap": random.choice(["Да", "Нет"]),
            "komanda_id": random.choice(teams)['id'],
            "igra_id": random.choice(games)['id'],
        }
        requests.post(url, json=data)

if __name__ == "__main__":
    add_teams(10)
    add_games(10)
    add_results(10)
