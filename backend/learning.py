import memory
from collections import Counter


def learn_from_history():
    data = memory.load_memory()
    words = []
    for entry in data:
        words.extend(entry.get('text','').lower().split())
    freq = Counter(words)
    return freq.most_common(20)
