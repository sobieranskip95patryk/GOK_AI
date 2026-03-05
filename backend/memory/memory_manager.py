import json
import os

class MemoryManager:
    def __init__(self, file_path=None):
        base = os.path.dirname(os.path.dirname(__file__))
        default = os.path.normpath(os.path.join(base, '..', 'database', 'conversations.json'))
        self.file = file_path or default
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        if not os.path.exists(self.file):
            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)

    def load(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []

    def save(self, data):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def store_user(self, text):
        data = self.load()
        data.append({ 'role': 'user', 'text': text })
        self.save(data)

    def store_ai(self, text):
        data = self.load()
        data.append({ 'role': 'ai', 'text': text })
        self.save(data)
