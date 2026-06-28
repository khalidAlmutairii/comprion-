from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_file(input_path: str, key: bytes, output_path: str) -> None:
    """Encrypt file using AES-CBC. Writes IV + ciphertext to output_path."""
    input_path = Path(input_path)
    output_path = Path(output_path)

    with open(input_path, "rb") as f:
        original = f.read()

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(original, AES.block_size))

    with open(output_path, "wb") as f:
        f.write(iv + encrypted)

def decrypt_file(input_path: str, key: bytes, output_path: str) -> bool:
    """Decrypt AES-CBC file (expects IV + ciphertext). Returns True if OK."""
    input_path = Path(input_path)
    output_path = Path(output_path)

    with open(input_path, "rb") as f:
        data = f.read()

    if len(data) < 16:
        return False

    iv = data[:16]
    enc = data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        dec = unpad(cipher.decrypt(enc), AES.block_size)
    except Exception:
        return False

    with open(output_path, "wb") as f:
        f.write(dec)

    return True
