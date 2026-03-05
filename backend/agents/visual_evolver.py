import json
import os

class VisualEvolver:
    """Generuje i zapisuje plik CSS na podstawie bazy wiedzy (database/knowledge.json).

    VisualEvolver przelicza "głębię wiedzy" na parametry wizualne i nadpisuje
    `frontend/evolution.css`.
    """

    def __init__(self, knowledge_path=None, css_path=None, repo_root=None):
        repo_root = repo_root or os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.knowledge_path = knowledge_path or os.path.join(repo_root, 'database', 'knowledge.json')
        self.css_path = css_path or os.path.join(repo_root, 'frontend', 'evolution.css')

    def analyze_knowledge_depth(self) -> int:
        try:
            with open(self.knowledge_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # jeśli struktura jest listą prostych konceptów
                if isinstance(data, list):
                    return len(data)
                # jeśli jest dict z kluczem 'concepts'
                if isinstance(data, dict) and 'concepts' in data:
                    return len(data.get('concepts') or [])
                # fallback: surowa długość listy elementów
                return len(data)
        except Exception:
            return 0

    def evolve_ui(self) -> str:
        depth = self.analyze_knowledge_depth()
        glow_intensity = min(depth * 5, 80)
        color = '#ffd700' if depth > 10 else '#00f2fe'
        blur = min(depth, 20)

        new_css = f"""/* Autonomiczna ewolucja - Poziom wiedzy: {depth} */
:root {{
    --evolution-level: {depth};
    --brain-glow: {color};
}}

body {{
    background: radial-gradient(circle at center, #111 0%, #000 100%);
    color: #e6eef8;
}}

.chat-container, #chat-container {{
    border: 1px solid {color}44;
    backdrop-filter: blur({blur}px);
    box-shadow: inset 0 0 {glow_intensity}px {color};
}}

#evolution-status {{
    background: {color};
    color: #001;
    padding: 6px 10px;
    border-radius: 6px;
    font-weight:700;
}}
"""
        os.makedirs(os.path.dirname(self.css_path), exist_ok=True)
        with open(self.css_path, 'w', encoding='utf-8') as f:
            f.write(new_css)
        return f"Interfejs ewoluował do poziomu {depth}. CSS zapisany w {self.css_path}"
