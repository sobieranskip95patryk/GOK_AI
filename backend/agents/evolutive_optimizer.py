import os
import re

class EvolutiveOptimizer:
    """Narzędzie do redukcji przestarzałych komponentów HTML (pruning).

    Uwaga: modyfikuje `frontend/index.html`. Tworzy kopię zapasową przed zmianą.
    """

    def __init__(self, html_path=None, repo_root=None):
        repo_root = repo_root or os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.html_path = html_path or os.path.join(repo_root, 'frontend', 'index.html')

    def read_html(self) -> str:
        with open(self.html_path, 'r', encoding='utf-8') as f:
            return f.read()

    def reduce_complexity(self, component_id: str) -> bool:
        """Usuwa cały sekcyjny blok o podanym ID, zwraca True jeśli dokonano zmiany."""
        content = self.read_html()
        # Obsługa zarówno pojedynczych jak i podwójnych cudzysłowów
        pattern = rf"<section\s+[^>]*id=(?:'|\"){re.escape(component_id)}(?:'|\")[\s\S]*?</section>"
        new_content, count = re.subn(pattern, '', content, flags=re.IGNORECASE)
        if count > 0 and new_content != content:
            # backup
            bak = self.html_path + '.bak'
            try:
                if not os.path.exists(bak):
                    with open(bak, 'w', encoding='utf-8') as bf:
                        bf.write(content)
            except Exception:
                pass

            with open(self.html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"GOK_AI: Redukcja komponentu '{component_id}' wykonana ({count} bloków usuniętych).")
            return True
        return False
