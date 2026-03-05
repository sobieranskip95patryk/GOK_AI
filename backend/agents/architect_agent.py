import os

class ArchitectAgent:
    """Agent odpowiedzialny za wstrzykiwanie nowych komponentów HTML do `frontend/index.html`.

    Uwaga: modyfikuje plik HTML. Tworzy backup przed zapisem.
    """
    def __init__(self, html_path=None, repo_root=None):
        repo_root = repo_root or os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.html_path = html_path or os.path.join(repo_root, 'frontend', 'index.html')

    def read_html(self) -> str:
        with open(self.html_path, 'r', encoding='utf-8') as f:
            return f.read()

    def inject_component(self, component_name: str, html_content: str) -> bool:
        """Wstrzykuje nowy komponent przed zamknięciem `</body>` jeśli nie istnieje.

        Zwraca True jeśli wstrzyknięto nowy komponent, False jeśli już istniał.
        """
        content = self.read_html()
        if f'id="{component_name}"' in content or f"id='{component_name}'" in content:
            return False

        # backup
        bak = self.html_path + '.bak'
        try:
            if not os.path.exists(bak):
                with open(bak, 'w', encoding='utf-8') as bf:
                    bf.write(content)
        except Exception:
            # ignorujemy błąd backupu
            pass

        new_content = content.replace(
            '</body>',
            f"\n<section id='{component_name}' class='evolution-module'>\n{html_content}\n</section>\n</body>"
        )

        with open(self.html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True
