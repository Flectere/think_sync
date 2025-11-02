import subprocess
from pathlib import Path
from .config_manager import read_config
from datetime import date


def clone_vault():
    config = read_config()
    url = config["vault_url"]
    path = config["vault_folder"]
    subprocess.run(["git", "clone", url, path])


def pull_vault():
    config = read_config()
    path = config["vault_folder"]
    vault = Path(path)
    if not vault.exists():
        clone_vault()
        return
    subprocess.run(["git", "pull"], cwd=path)


def push_vault():
    today = f"{date.today()}"
    config = read_config()
    path = config["vault_folder"]
    subprocess.run(["git", "add", "."], cwd=path)
    subprocess.run(["git", "commit", "-m", today], cwd=path)
    subprocess.run(["git", "push"], cwd=path)