import time
from backend.learning.pattern_detector import detect_patterns

class LearningLoop:
    def __init__(self, interval: int = 60):
        self.interval = interval
        self.running = False

    def run_once(self):
        patterns = detect_patterns()
        print('Detected patterns:', patterns[:10])
        return patterns

    def run(self):
        self.running = True
        try:
            while self.running:
                self.run_once()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.running = False
