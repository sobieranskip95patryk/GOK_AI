from backend.ai.embedding_engine import EmbeddingEngine
from backend.memory.vector_store import VectorStore
from backend.ai.reasoning_engine import ReasoningEngine

class CognitiveLoop:
    """Cognitive perception-action loop combining embedding, memory search, reasoning and agents."""

    def __init__(self, embed: EmbeddingEngine, vector: VectorStore, reason: ReasoningEngine, agents):
        self.embed = embed
        self.vector = vector
        self.reason = reason
        self.agents = agents

    def process(self, text: str) -> dict:
        embedding = self.embed.create_embedding(text)
        memory_hits = self.vector.search(embedding)
        topic = self.reason.analyze(text)
        response = self.agents.run(text)
        # store new memory item
        try:
            self.vector.add(text, embedding)
        except Exception:
            pass
        return {
            'topic': topic,
            'memory': memory_hits,
            'response': response
        }
