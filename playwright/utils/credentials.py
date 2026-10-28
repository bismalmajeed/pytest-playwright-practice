import json
from pathlib import Path

CREDENTIALS_FILE = Path(__file__).parent.parent / "data" / "credentials.json"


def load():
    with open(CREDENTIALS_FILE) as f:
        return json.load(f)


def default_user():
    return load()["user_credentials"][0]


def practice_site():
    return load()["practice_site"]
