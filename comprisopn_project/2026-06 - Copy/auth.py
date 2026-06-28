import json
import hashlib
from config import USERS_FILE

def load_users():
    if USERS_FILE.exists():
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f)

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()
