import json
import os

class KnowledgeExtractor:
    def __init__(self, file_path=None):
        base = os.path.dirname(os.path.dirname(__file__))
        default = os.path.normpath(os.path.join(base, '..', 'database', 'knowledge.json'))
        self.file = file_path or default
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        if not os.path.exists(self.file):
            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)

    def extract(self, text):
        words = (text or '').split()
        concepts = [w for w in words if len(w) > 6]
        return concepts

    def store(self, concepts):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            data = []
        data += concepts
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
*** End Patch