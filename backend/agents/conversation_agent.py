class ConversationAgent:
    def __init__(self, memory, reasoning):
        self.memory = memory
        self.reasoning = reasoning

    def respond(self, text: str) -> str:
        topic = self.reasoning.analyze(text)
        if topic == 'topic_ai':
            return 'Sztuczna inteligencja rozwija się poprzez dane i algorytmy.'
        if topic == 'topic_future':
            return 'Przyszłość AI zależy od systemów uczących się i sieci wiedzy.'
        return 'Interesujący pomysł. Opowiedz więcej.'
