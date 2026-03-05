class ReasoningEngine:
    """Prosty silnik wnioskowania/klasyfikacji tematów."""
    def analyze(self, text: str) -> str:
        t = (text or '').lower()
        if 'ai' in t or 'sztuczn' in t:
            return 'topic_ai'
        if 'future' in t or 'przysz' in t:
            return 'topic_future'
        return 'general'
