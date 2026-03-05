class PlanningAgent:
    def __init__(self, memory, knowledge_graph=None):
        self.memory = memory
        self.kg = knowledge_graph

    def plan(self, goal):
        # very simple placeholder
        return { 'goal': goal, 'steps': ['analyze', 'research', 'propose'] }
