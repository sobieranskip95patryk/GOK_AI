import json
import math
import os

class VectorStore:
    """File-backed vector store using cosine similarity.
    Stores items in `database/vectors.json` as list of {"text":..., "vector":[...]}
    """
    def __init__(self, file_path=None):
        base = os.path.dirname(os.path.dirname(__file__))
        default = os.path.normpath(os.path.join(base, '..', 'database', 'vectors.json'))
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

    def add(self, text, vector):
        data = self.load()
        data.append({ 'text': text, 'vector': vector })
        self.save(data)

    def _cosine(self, a, b):
        dot = sum(x*y for x,y in zip(a,b))
        norma = math.sqrt(sum(x*x for x in a))
        normb = math.sqrt(sum(x*x for x in b))
        if norma == 0 or normb == 0:
            return 0.0
        return dot / (norma * normb)

    def search(self, query_vector, top_k=5):
        data = self.load()
        results = []
        for item in data:
            try:
                score = self._cosine(query_vector, item.get('vector', []))
            except Exception:
                score = 0.0
            results.append((score, item.get('text')))
        results.sort(key=lambda x: x[0], reverse=True)
        return results[:top_k]
