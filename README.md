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

API endpoints:

- `POST /chat` — wysyłasz {"message":"..."}, otrzymujesz {"reply":"..."}
- `GET /health` — szybkiego check-a stanu
- `GET /debug/state` — snapshot pamięci/wektorów/grafu wiedzy (do debugowania)
- `POST /learn/run_once` — uruchamia jednorazowy krok pętli uczenia (detekcja wzorców)

Przykład uruchomienia backendu z poziomu repozytorium:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
