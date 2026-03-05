import os
import shutil
import time

class EvolutionAgent:
    """Agent umożliwiający czytanie i bezpieczne (proste) nadpisywanie plików repozytorium.

    UWAGA: Ten komponent nadpisuje pliki źródłowe. Upewnij się, że masz kopię zapasową
    lub używasz systemu kontroli wersji (git)."""

    def __init__(self, repo_path: str = None):
        self.repo_path = os.path.normpath(repo_path or os.path.join(os.path.dirname(__file__), '..', '..'))

    def _full(self, file_path: str) -> str:
        return os.path.normpath(os.path.join(self.repo_path, file_path))

    def read_source_code(self, file_path: str) -> str:
        full_path = self._full(file_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()

    def apply_evolution(self, file_path: str, new_code: str) -> str:
        """Nadpisuje plik nowym kodem, tworząc kopię zapasową z sufiksem .bak.<timestamp>

        Zwraca informację o wyniku.
        """
        full_path = self._full(file_path)
        if not os.path.exists(full_path):
            return f"Plik nie istnieje: {file_path}"

        # stwórz kopię zapasową z timestampem
        ts = int(time.time())
        bak_path = full_path + f'.bak.{ts}'
        shutil.copy2(full_path, bak_path)

        # zapisz nowy plik
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_code)

        return f"Ewolucja pliku {file_path} zakończona sukcesem. Backup: {os.path.basename(bak_path)}"
