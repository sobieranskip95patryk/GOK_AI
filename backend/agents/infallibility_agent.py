import subprocess
import os
import sys
import glob

class InfallibilityAgent:
    """Agent walidujący zmiany poprzez uruchamianie testów w izolowanym pliku,
    oraz przywracający backup, jeśli walidacja nie przejdzie.
    """

    def __init__(self, repo_root: str = None):
        self.repo_root = repo_root or os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))

    def run_unit_test(self, test_code: str, timeout: int = 5) -> (bool, str):
        """Wykonuje tymczasowy plik testowy z podanym kodem Pythona.

        Zwraca tuple (success: bool, output: str).
        """
        test_filename = os.path.join(self.repo_root, 'temp_evolution_test.py')
        try:
            with open(test_filename, 'w', encoding='utf-8') as f:
                f.write(test_code)

            # Uruchamiamy w tym samym interpreterze co serwer
            result = subprocess.run([sys.executable, test_filename], capture_output=True, timeout=timeout)
            stdout = (result.stdout or b'').decode('utf-8', errors='ignore')
            stderr = (result.stderr or b'').decode('utf-8', errors='ignore')
            output = stdout + stderr
            success = result.returncode == 0
            return success, output
        except Exception as e:
            return False, str(e)
        finally:
            try:
                if os.path.exists(test_filename):
                    os.remove(test_filename)
            except Exception:
                pass

    def perform_rollback(self, file_path: str) -> (bool, str):
        """Przywraca najbardziej aktualny backup dla `file_path`.

        Szuka plików `file_path.bak.*` lub `file_path.bak` i przywraca najnowszy.
        """
        full = os.path.normpath(os.path.join(self.repo_root, file_path))
        if not os.path.exists(full):
            return False, f'File not found: {full}'

        pattern_ts = full + '.bak.*'
        candidates = glob.glob(pattern_ts)
        bak_to_use = None
        if candidates:
            # wybierz najnowszy
            candidates.sort(key=os.path.getmtime, reverse=True)
            bak_to_use = candidates[0]
        else:
            simple = full + '.bak'
            if os.path.exists(simple):
                bak_to_use = simple

        if not bak_to_use:
            return False, 'No backup found to rollback.'

        try:
            os.replace(bak_to_use, full)
            return True, f'Rollback successful from {os.path.basename(bak_to_use)}'
        except Exception as e:
            return False, str(e)
