class PlanningEngine:
    """Simple planning engine producing high-level steps for a goal."""
    def plan(self, goal: str):
        g = (goal or '').lower()
        steps = []
        if 'build' in g or 'zbud' in g:
            steps = [
                'analyze requirements',
                'design architecture',
                'implement modules',
                'test system'
            ]
        elif 'research' in g or 'badanie' in g:
            steps = [
                'collect sources',
                'analyze data',
                'summarize knowledge'
            ]
        else:
            steps = ['analyze', 'research', 'propose']
        return steps
