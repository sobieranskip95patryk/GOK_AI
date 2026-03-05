import json
import os

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'database', 'conversations.json')
DB_FILE = os.path.normpath(DB_FILE)


def load_memory():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_message(role, text):
    data = load_memory()
    data.append({
        'role': role,
        'text': text
    })
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
