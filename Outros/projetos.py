from pathlib import Path
import json
import sys

ROOT_FILE = Path(__file__).parent
FILE = ROOT_FILE / 'data.json'

with open(FILE, 'r', encoding='utf8') as file:
    try:
        data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = {}

sys.exit()
with open(FILE, 'w', encoding='utf8') as file:
    data = {
        'bruno': {'password': '123456'}
    }
    json.dump(
        data, file, ensure_ascii=False, indent=2
    )

with open(FILE, 'w', encoding='utf8') as file:
    data = {
        'igor': {'password': '123456'}
    }
    json.dump(
        data, file, ensure_ascii=False, indent=2
    )
