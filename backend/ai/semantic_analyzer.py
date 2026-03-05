class SemanticAnalyzer:
    """Very small semantic analyzer that extracts 'entities' and 'actions'."""

    def analyze(self, text: str):
        words = (text or '').lower().split()
        entities = []
        actions = []
        for w in words:
            if len(w) > 6:
                entities.append(w)
            if w.endswith('ing'):
                actions.append(w)
        return { 'entities': entities, 'actions': actions }
