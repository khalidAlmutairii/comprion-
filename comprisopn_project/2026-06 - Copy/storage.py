from pathlib import Path
from config import ENCRYPTED_DIR, DECRYPTED_DIR, QR_DIR, DATA_DIR

def ensure_folders():
    for d in [ENCRYPTED_DIR, DECRYPTED_DIR, QR_DIR, DATA_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def make_encrypted_output_path(original_file_path: str) -> Path:
    """
    Encrypt output name:
      <original_name><original_suffixes>.enc
    Example:
      report.pdf -> report.pdf.enc
      photo.jpg -> photo.jpg.enc
    """
    p = Path(original_file_path)
    return ENCRYPTED_DIR / (p.name + ".enc")

def make_decrypted_output_path(encrypted_file_path: str) -> Path:
    """
    Decrypt output name:
      remove ONLY the last '.enc'
    Example:
      report.pdf.enc -> report.pdf
      archive.zip.enc -> archive.zip
    """
    p = Path(encrypted_file_path)
    name = p.name

    if name.lower().endswith(".enc"):
        original_name = name[:-4]  # remove ".enc"
    else:
        # fallback (shouldn't happen if file picker enforces *.enc)
        original_name = name

    return DECRYPTED_DIR / original_name
