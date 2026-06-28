from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / "storage"

ENCRYPTED_DIR = STORAGE_DIR / "encrypted"
DECRYPTED_DIR = STORAGE_DIR / "decrypted"
QR_DIR = STORAGE_DIR / "qr"
DATA_DIR = STORAGE_DIR / "data"

USERS_FILE = DATA_DIR / "users.json"
TOKENS_FILE = DATA_DIR / "tokens.json"
