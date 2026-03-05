import os
import json
import subprocess
from pathlib import Path


class ExcellenceMetric:
    """Calculate a 'perfection' score based on knowledge, tests and UI complexity.

    Safe, best-effort metrics:
    - knowledge depth: derived from database/knowledge.json (node count)
    - test success rate: runs pytest if available (returns 0-1)
    - css size: size of frontend/evolution.css in kilobytes

    Requires repository located at workspace root.
    """

    def __init__(self, workspace_root: str = None):
        self.workspace = Path(workspace_root or Path.cwd())

    def get_knowledge_depth(self) -> float:
        try:
            kp = self.workspace / "database" / "knowledge.json"
            if not kp.exists():
                return 0.0
            with open(kp, "r", encoding="utf-8") as f:
                data = json.load(f)
            # simple proxy: number of knowledge items (nodes)
            if isinstance(data, dict):
                depth = float(len(data.get("nodes", data)))
            elif isinstance(data, list):
                depth = float(len(data))
            else:
                depth = 0.0
            return max(0.0, depth)
        except Exception:
            return 0.0

    def get_test_success_rate(self) -> float:
        """Try to run pytest and return a success rate 0.0-1.0 (best-effort).

        If pytest is not available or fails, return 0.0.
        """
        try:
            proc = subprocess.run(["pytest", "-q"], cwd=str(self.workspace), capture_output=True, text=True, timeout=60)
            return 1.0 if proc.returncode == 0 else 0.0
        except Exception:
            return 0.0

    def get_css_size(self) -> float:
        try:
            cssp = self.workspace / "frontend" / "evolution.css"
            if not cssp.exists():
                return 0.0
            size_kb = cssp.stat().st_size / 1024.0
            return float(size_kb)
        except Exception:
            return 0.0

    def calculate_perfection(self) -> float:
        knowledge_depth = self.get_knowledge_depth()
        code_stability = self.get_test_success_rate()
        visual_complexity = self.get_css_size()

        # User-provided formula; code_stability expected 0..1
        perfection_score = (knowledge_depth * 0.5) + (code_stability * 30.0) + (visual_complexity * 0.2)
        return float(perfection_score)
