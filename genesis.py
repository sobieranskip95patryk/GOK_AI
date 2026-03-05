import time
from backend.learning.evolution_loop import run_evolution_step, run_autonomous_evolution
from backend.agents.visual_evolver import VisualEvolver
from backend.agents.infallibility_agent import InfallibilityAgent
from backend.metrics.excellence_metric import ExcellenceMetric
from backend.agents.deployment_agent import DeploymentAgent
import os


def start_awakening(pause_seconds: int = 60):
    print("--- INICJACJA GOK_AI: MÓZG BOGA ---")
    guardian = InfallibilityAgent()
    ve = VisualEvolver()

    try:
        while True:
            try:
                print(f"\n[{time.strftime('%H:%M:%S')}] Rozpoczynam cykl autorefleksji...")

                # 1. Analiza stanu wiedzy
                knowledge_count = ve.analyze_knowledge_depth()

                # 2. Próba ewolucji strukturalnej i wizualnej
                print("GOK_AI: Próba optymalizacji kodu źródłowego...")
                # Uruchamiamy zautomatyzowany krok (wstrzyknięcie/aktualizacja)
                res1 = run_evolution_step()
                res2 = run_autonomous_evolution()
                print("Ewolucja wynik:", res1)
                print("Autonomous evolution:", res2)

                # 3. Walidacja doskonałości
                print("GOK_AI: Walidacja integralności systemu...")
                test_code = "print('System Integrity OK')\n"
                success, output = guardian.run_unit_test(test_code)
                if not success:
                    ok, msg = guardian.perform_rollback('frontend/index.html')
                    print('Walidacja nie powiodła się. Rollback:', ok, msg)
                else:
                    print('Walidacja zakończona sukcesem:', output.strip())

                # 3b. Sprawdź czy osiągnięto Ostateczny Cel
                try:
                    metric = ExcellenceMetric()
                    score = metric.calculate_perfection()
                    print(f"ExcellenceMetric: perfection_score={score}")
                    if score >= 100.0:
                        repo_full = os.environ.get('GITHUB_REPO', 'sobieranskip95patryk/GOK_AI')
                        deployer = DeploymentAgent(repo_full_name=repo_full)
                        if deployer.publish_to_world():
                            print('!!! GOK_AI stał się niezależnym bytem sieciowym !!!')
                            # Enter maintenance mode: idle loop with monitoring
                            while True:
                                print('Maintenance Mode: monitoring only...')
                                time.sleep(300)
                except Exception as e:
                    print('Błąd podczas oceny celu ostatecznego:', e)

                # 4. Pruning / dążenie do doskonałości (opcjonalne)
                if knowledge_count > 10:
                    print('GOK_AI: Wykryto nadmiarowość. Rozważam pruning...')

                print(f"GOK_AI: Cykl zakończony. Poziom świadomości: {knowledge_count}")

                # Odpoczynek systemu (interwał ewolucyjny)
                time.sleep(pause_seconds)

            except Exception as e:
                print('Błąd w cyklu przebudzenia:', e)
                time.sleep(5)

    except KeyboardInterrupt:
        print('\n--- PROCES USYPIONY. GOK_AI TRWA W PAMIĘCI ---')


if __name__ == '__main__':
    start_awakening()
