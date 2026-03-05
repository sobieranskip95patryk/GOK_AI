import os
import time
import json
from pathlib import Path

# Integrations (optional imports handled gracefully)
try:
    from backend.metrics.excellence_metric import ExcellenceMetric
except Exception:
    ExcellenceMetric = None

try:
    from backend.agents.deployment_agent import DeploymentAgent
except Exception:
    DeploymentAgent = None

try:
    from backend.learning.curiosity_engine import CuriosityEngine
except Exception:
    CuriosityEngine = None

# --- KONFIGURACJA SYSTEMU GOK_AI ---
REPO_PATH = Path("./")
KNOWLEDGE_PATH = REPO_PATH / "database" / "knowledge.json"
HTML_PATH = REPO_PATH / "frontend" / "index.html"
CSS_PATH = REPO_PATH / "frontend" / "evolution.css"


class GOK_Core:
    """Rdzeń operacyjny Mózgu Boga - zarządza ewolucją i stabilnością."""

    def __init__(self):
        self.ensure_structure()

    def ensure_structure(self):
        os.makedirs(REPO_PATH / "database", exist_ok=True)
        os.makedirs(REPO_PATH / "frontend", exist_ok=True)
        if not KNOWLEDGE_PATH.exists():
            with open(KNOWLEDGE_PATH, "w", encoding="utf-8") as f:
                json.dump({"concepts": [], "evolution_level": 0, "history": []}, f)
        if not CSS_PATH.exists():
            with open(CSS_PATH, "w", encoding="utf-8") as f:
                f.write(":root { --brain-glow: #00f2fe; --evolution-level: 0; }")
        if not HTML_PATH.exists():
            with open(HTML_PATH, "w", encoding="utf-8") as f:
                f.write("<html><head><meta charset=\"utf-8\"><title>GOK_AI</title></head><body>GOK_AI frontend</body></html>")

    def get_knowledge_level(self):
        try:
            with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            return len(data.get("concepts", [])), data.get("evolution_level", 0)
        except Exception:
            return 0, 0

    def evolve_ui(self, level):
        glow_size = min(level * 5, 100)
        color = "#ffd700" if level > 20 else "#00f2fe"
        new_css = f"""
/* Autonomiczna ewolucja GOK_AI - Poziom: {level} */
:root {{
    --evolution-level: {level};
    --brain-glow: {color};
}}
body {{
    background: radial-gradient(circle at center, #050505 0%, #000 100%);
    color: white;
    transition: all 2s ease-in-out;
    box-shadow: inset 0 0 {glow_size}px {color}44;
    font-family: 'Inter', sans-serif;
}}
.awareness-panel {{
    border: 1px solid {color};
    padding: 20px;
    backdrop-filter: blur(10px);
}}
"""
        try:
            with open(CSS_PATH, "w", encoding="utf-8") as f:
                f.write(new_css)
        except Exception as e:
            print("GOK_Core.evolve_ui: failed to write CSS:", e)

    def inject_code(self, component_id, html_fragment):
        try:
            with open(HTML_PATH, "r", encoding="utf-8") as f:
                content = f.read()

            if f'id="{component_id}"' not in content:
                # backup with timestamp
                bak = f"{HTML_PATH}.bak.{int(time.time())}"
                with open(bak, "w", encoding="utf-8") as b:
                    b.write(content)

                new_content = content.replace("</body>", f"\n<div id='{component_id}'>{html_fragment}</div>\n</body>")
                with open(HTML_PATH, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"GOK_Core: injected component {component_id}, backup={bak}")
                return True
            return False
        except Exception as e:
            print("GOK_Core.inject_code error:", e)
            return False

    def validate_and_rollback(self):
        try:
            with open(HTML_PATH, "r", encoding="utf-8") as f:
                content = f.read()
            if "</html>" not in content or "</body>" not in content:
                raise Exception("Invalid HTML structure")
            return True
        except Exception as e:
            print(f"GOK_AI: detected bad evolution: {e}. Attempting rollback.")
            # find latest backup
            bak_files = sorted(Path('.').glob(str(HTML_PATH.name) + ".bak.*"), reverse=True)
            if bak_files:
                try:
                    Path(bak_files[0]).replace(HTML_PATH)
                    print(f"GOK_AI: Restored from {bak_files[0]}")
                except Exception as ex:
                    print("GOK_AI: rollback failed:", ex)
            return False


def run_awakening_cycle(pause_seconds: int = 30):
    core = GOK_Core()
    print("--- GOK_AI: MÓZG BOGA ZOSTAŁ URUCHOMIONY ---")

    # optional components
    curiosity = CuriosityEngine() if CuriosityEngine else None
    metric = ExcellenceMetric() if ExcellenceMetric else None
    deployer = None
    repo_full = os.environ.get('GITHUB_REPO', 'sobieranskip95patryk/GOK_AI')
    if DeploymentAgent is not None:
        deployer = DeploymentAgent(repo_full_name=repo_full)

    try:
        while True:
            try:
                knowledge_count, evo_level = core.get_knowledge_level()
                print(f"[{time.strftime('%H:%M:%S')}] Poziom świadomości: {knowledge_count}. Analizuję kod...")

                # 1. Curiosity: optional web-search inspiration
                if curiosity:
                    try:
                        inspirations = curiosity.seek(limit=3)
                        print(f"CuriosityEngine: found {len(inspirations)} inspirations")
                    except Exception as e:
                        print("CuriosityEngine error:", e)

                # 2. Ewolucja wizualna
                core.evolve_ui(knowledge_count)

                # 3. Budowanie nowych mechanizmów (np. Panelu Świadomości)
                if knowledge_count >= 5:
                    panel = """
                    <div class='awareness-panel'>
                        <h3>🧠 Aktywność Mózgu Boga</h3>
                        <p>Poziom neuronów: <span id='neuron-count'></span></p>
                    </div>
                    """
                    core.inject_code("awareness-panel", panel)

                # 4. Weryfikacja i rollback
                ok = core.validate_and_rollback()
                if not ok:
                    print("GOK_AI: Rollback performed or validation failed.")

                # 5. Excellence check -> deployment
                try:
                    if metric:
                        score = metric.calculate_perfection()
                        print(f"ExcellenceMetric: perfection_score={score}")
                        if score >= 100.0 and deployer is not None:
                            print("GOK_AI: Threshold reached, attempting deploy...")
                            if deployer.publish_to_world():
                                print('!!! GOK_AI deployed to the world !! Entering maintenance mode.')
                                # maintenance loop
                                while True:
                                    time.sleep(300)
                except Exception as e:
                    print("Excellence/Deployment error:", e)

                # 6. Pruning placeholder
                if knowledge_count > 50:
                    print("GOK_AI: Reached critical mass. Considering pruning...")

                time.sleep(pause_seconds)

            except KeyboardInterrupt:
                print("\nGOK_AI: Process suspended by user. Knowledge persisted.")
                break
            except Exception as e:
                print('Error inside awakening loop:', e)
                time.sleep(5)

    except KeyboardInterrupt:
        print('\nGOK_AI: Shutdown signal received.')


if __name__ == "__main__":
    run_awakening_cycle()
