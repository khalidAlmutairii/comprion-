from storage import ensure_folders
from ui import start_app

def main():
    ensure_folders()
    start_app()

if __name__ == "__main__":
    main()
