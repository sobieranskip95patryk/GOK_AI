import hashlib
import random

class EmbeddingEngine:
    """Prosty symulowany engine embeddingów (deterministyczny na podstawie text hash)."""

    def __init__(self, dim: int = 128):
        self.dim = dim

    def create_embedding(self, text: str):
        seed = int(hashlib.md5((text or '').encode('utf-8')).hexdigest(), 16) % (2**32)
        rnd = random.Random(seed)
        return [rnd.random() for _ in range(self.dim)]
