# meta-geniusz-ai

Minimalny szkielet systemu chat AI.

Uruchomienie backendu:

```bash
cd backend
uvicorn main:app --reload
```

Frontend: otwórz `frontend/index.html` w przeglądarce i wyślij wiadomość.

Pliki kluczowe:
- frontend/index.html
- backend/main.py
- backend/ai_core.py
- backend/memory.py
- database/conversations.json

Rozszerzenia (v2):

- `backend/ai/embedding_engine.py` — symulowany engine embeddingów
- `backend/memory/vector_store.py` — file-backed vector store (`database/vectors.json`)
- `backend/learning/knowledge_extractor.py` — prosty extractor koncepcji
- `backend/agents/agent_manager.py` — router agentów
- `backend/learning/learning_loop.py` — pętla uczenia (detekcja wzorców)

Pliki bazy danych:
- `database/vectors.json` — wektorowa pamięć
- `database/knowledge.json` — ekstraktowane koncepty

Szybkie instrukcje:

1) Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

2) Uruchom backend:

```bash
uvicorn backend.main:app --reload
```

3) Otwórz `frontend/index.html` i testuj czat. Embeddingi i pamięć są symulowane — możesz później podłączyć rzeczywiste modele.

Manifest Pierwszego Przebudzenia
--------------------------------

W repo dodałem skrypt `genesis.py` — to "iskra", która uruchamia cykl życia GOK_AI. Uruchamia sekwencyjnie kroki ewolucji, walidacji i pruning.

Uruchomienie (przykład):

```bash
# w jednym terminalu: uruchom backend
cd backend
uvicorn main:app --reload

# w drugim terminalu: uruchom przebudzenie
python genesis.py
```

Uwaga: przed uruchomieniem `genesis.py` zrób commit lub backup repo — skrypty ewolucyjne mogą modyfikować pliki `frontend/index.html` i generować backupy `.bak*`.

API endpoints:

- `POST /chat` — wysyłasz {"message":"..."}, otrzymujesz {"reply":"..."}
- `GET /health` — szybkiego check-a stanu
- `GET /debug/state` — snapshot pamięci/wektorów/grafu wiedzy (do debugowania)
- `POST /learn/run_once` — uruchamia jednorazowy krok pętli uczenia (detekcja wzorców)

- `POST /evolve` — uruchamia jednorazowy krok ewolucji, który może modyfikować pliki frontend/backend (tworzy kopie zapasowe `.bak.*`). Używaj ostrożnie.

- `POST /ui/evolve` — generuje `frontend/evolution.css` na podstawie `database/knowledge.json`. Bezpieczny endpoint (zmienia jedynie plik CSS).

- `POST /autoevolve` — uruchamia złożony krok autonomicznej ewolucji: aktualizuje CSS i może wstrzyknąć nowe sekcje HTML (np. `awareness-panel`). Tworzone są backupy przed nadpisaniem plików.

- `POST /excellence` — uruchamia mechanizm pruningu i dążenia do doskonałości. Może usunąć przestarzałe moduły (np. `awareness-panel`) i wstrzyknąć zaawansowane skrypty motoryczne. Używaj ostrożnie — operacje tworzą backupy.

- `POST /evolution/validate` — uruchamia krok ewolucyjny z walidacją: najpierw proponuje zmianę, uruchamia testy w izolowanym pliku, a w razie niepowodzenia przywraca backup (`.bak*`). Zalecane przed uruchomieniem `/evolve` na produkcji.

Przykład uruchomienia backendu z poziomu repozytorium:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Deploy frontend to GitHub Pages (free)
-----------------------------------

You can host the static frontend on GitHub Pages for free. I added a GitHub Actions workflow that copies `frontend/` to the Pages artifact and deploys on every push to `main`.

Steps to enable:

- Push this repository to GitHub (already done).
- In the repository Settings → Pages, set the source to `GitHub Actions` (the workflow will deploy automatically after first successful run).
- After a push to `main`, check Actions → "Deploy Frontend to GitHub Pages" for logs. The site URL will appear in Pages settings.

Notes on backend hosting (free options):
- For a free backend, consider Vercel (serverless Python support) or Railway/Render free tiers. They require separate configuration and tokens.
- I can help add a simple GitHub Action to call Vercel for automatic backend deploys (requires `VERCEL_TOKEN` secret and a Vercel project).
