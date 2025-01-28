# file_ops.py
import json

def save_game(player_team):
    try:
        with open("savefile.json", "w") as file:
            json.dump(player_team, file)
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    try:
        with open("savefile.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return []
    except Exception as e:
        print(f"Error loading game: {e}")
        return []