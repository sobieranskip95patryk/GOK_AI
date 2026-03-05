class ResearchAgent:
    def __init__(self, memory, vector_store=None):
        self.memory = memory
        self.vs = vector_store

    def find_related(self, query_embedding):
        if not self.vs:
            return []
        return self.vs.search(query_embedding)
