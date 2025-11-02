import subprocess
from core import load_config
from gui import load_gui

def main():
    config = load_config()
    load_gui(config["vault_url"], config["vault_folder"])

if __name__ == "__main__":
    main()