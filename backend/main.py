from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any

from backend.ai.core import AICore
from backend.memory.memory_manager import MemoryManager
from backend.memory.vector_store import VectorStore
from backend.memory.knowledge_graph import KnowledgeGraph
from backend.learning.learning_loop import LearningLoop
from backend.agents.visual_evolver import VisualEvolver

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai = AICore()
memory_mgr = MemoryManager()
vector_store = VectorStore()
kg = KnowledgeGraph()
learning_loop = LearningLoop()


class Message(BaseModel):
    message: str


@app.get('/health')
async def health() -> Any:
    return { 'status': 'ok' }


@app.post('/chat')
async def chat(msg: Message):
    user_text = msg.message
    reply = ai.process(user_text)
    return { 'reply': reply }


@app.get('/debug/state')
async def debug_state():
    # return small snapshots of memory, vectors and knowledge graph
    mem = memory_mgr.load()
    vectors = vector_store.load()
    kg_data = kg.load()

    return {
        'memory_tail': mem[-40:],
        'vectors_count': len(vectors),
        'vectors_head': vectors[:10],
        'knowledge_graph': kg_data
    }


@app.post('/learn/run_once')
async def learn_run_once():
    patterns = learning_loop.run_once()
    return { 'patterns': patterns }


@app.post('/evolve')
async def trigger_evolution():
    """Trigger a single evolution step performed by the EvolutionAgent.

    NOTE: this will modify repository files (creates backups). Use with caution.
    """
    from backend.learning.evolution_loop import run_evolution_step
    result = run_evolution_step()
    return { 'status': 'Evolution triggered', 'details': result }


@app.post('/ui/evolve')
async def trigger_ui_evolution():
    """Trigger UI evolution: VisualEvolver reads `database/knowledge.json` and writes `frontend/evolution.css`.

    NOTE: safe operation (only writes CSS file) — no source files overwritten.
    """
    ve = VisualEvolver()
    res = ve.evolve_ui()
    return { 'status': 'UI evolution triggered', 'details': res }


@app.post('/autoevolve')
async def trigger_autonomous_evolution():
    """Trigger combined UI evolution + architect injection step.

    This will update CSS and may inject HTML components into `frontend/index.html`.
    Backups are created for modified files.
    """
    from backend.learning.evolution_loop import run_autonomous_evolution
    result = run_autonomous_evolution()
    return { 'status': 'Autonomous evolution triggered', 'details': result }


@app.post('/excellence')
async def trigger_excellence():
    """Trigger excellence loop: pruning + motor injection when appropriate."""
    from backend.learning.evolution_loop import strive_for_excellence
    res = strive_for_excellence()
    return { 'status': 'Excellence run complete', 'details': res }


@app.post('/evolution/validate')
async def trigger_evolution_validation():
    """Trigger evolution step with pre-deployment validation (tests + rollback).

    This will inject a proposed component, run tests, and rollback if tests fail.
    """
    from backend.learning.evolution_loop import evolution_with_validation
    res = evolution_with_validation()
    return { 'status': 'Evolution validation complete', 'details': res }
