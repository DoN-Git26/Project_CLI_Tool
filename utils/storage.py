import json
import os

DB_FILE = "data/database.json"

def load_data():
    """
    Load data from the JSON file.
    Ensures the structure always contains a 'users' key.
    Returns a dictionary with 'users' list.
    """
    if not os.path.exists(DB_FILE):
        return {"users": []}
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            # Guarantee structure
            if "users" not in data:
                data["users"] = []
            return data
    except (json.JSONDecodeError, IOError):
        # If file is empty or corrupted, reset structure
        return {"users": []}

def save_data(data):
    """
    Save data back to the JSON file.
    """
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
