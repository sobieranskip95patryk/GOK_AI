class AgentManager:
    """Agent manager v2: decides which agent should handle a request and runs it."""
    def __init__(self, conversation, research, planner):
        self.conversation = conversation
        self.research = research
        self.planner = planner

    def decide(self, text: str) -> str:
        t = (text or '').lower()
        if 'plan' in t or 'zaplanuj' in t:
            return 'planner'
        if 'research' in t or 'badanie' in t:
            return 'research'
        return 'conversation'

    def run(self, text: str):
        agent = self.decide(text)
        if agent == 'planner':
            return self.planner.respond(text)
        if agent == 'research':
            return self.research.respond(text)
        return self.conversation.respond(text)
