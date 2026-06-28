import json, os, secrets
import qrcode
from config import TOKENS_FILE, QR_DIR


def tok(data=None):
    if data is None:
        if TOKENS_FILE.exists():
            with open(TOKENS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    else:
        with open(TOKENS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)


def new_token():
    return secrets.token_urlsafe(10)


def save_token(token, enc_path, key_hex):
    t = tok()
    t[token] = [enc_path, key_hex]
    tok(t)

    qr_path = QR_DIR / f"qr_{token}.png"
    qrcode.make(token).save(qr_path)

    return qr_path


def get_token(token):
    return tok().get(token)
