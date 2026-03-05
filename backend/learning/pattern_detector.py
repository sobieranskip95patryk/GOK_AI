import json
from collections import Counter
import os

def detect_patterns(file_path=None, top_n=20):
    base = os.path.dirname(os.path.dirname(__file__))
    default = os.path.normpath(os.path.join(base, '..', 'database', 'conversations.json'))
    fp = file_path or default
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        return []
    words = []
    for entry in data:
        words += (entry.get('text','') or '').lower().split()
    freq = Counter(words)
    return freq.most_common(top_n)
