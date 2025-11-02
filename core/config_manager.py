import json
from pathlib import Path


data_template = {
        "vault_url": "",
        "vault_folder":"",
    }

def load_config():
    file = Path("config.json")
    if not file.exists():
        create_config()
    return read_config()


def create_config():
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(data_template, f, ensure_ascii=False, indent=4)


def read_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def write_config(url, folder):
    data = data_template.copy()
    data["vault_url"] = url
    data["vault_folder"] = folder
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)