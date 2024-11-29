import os
import json
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data(file: str) -> dict:
    try:
        return json.load(open(file))
    except:
        return {}

def save_data(file: str, data: dict):
    try:
        json.dump(data, open(file, "w"), indent=4)
    except:
        print("Cannot save data:", json.dumps(data))

def get_file() -> str:
    return "./data.json" if len(sys.argv) < 2 else sys.argv[1]