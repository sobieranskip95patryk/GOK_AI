from backend.ai.embedding_engine import EmbeddingEngine
from backend.memory.vector_store import VectorStore
from backend.ai.reasoning_engine import ReasoningEngine
from backend.ai.semantic_analyzer import SemanticAnalyzer
from backend.ai.planning_engine import PlanningEngine

from backend.agents.conversation_agent import ConversationAgent
from backend.agents.research_agent import ResearchAgent
from backend.agents.planning_agent import PlanningAgent
from backend.agents.agent_manager import AgentManager
from backend.ai.cognitive_loop import CognitiveLoop
from backend.memory.memory_manager import MemoryManager
from backend.memory.knowledge_graph import KnowledgeGraph
from backend.learning.knowledge_extractor import KnowledgeExtractor


class AICore:
    """Integrated AI core (v3) composing embedding, vector memory, reasoning, agents and cognitive loop."""
    def __init__(self):
        self.memory = MemoryManager()
        self.embed = EmbeddingEngine()
        self.vector = VectorStore()
        self.reason = ReasoningEngine()
        self.semantic = SemanticAnalyzer()
        self.planner_engine = PlanningEngine()

        # agents
        conv = ConversationAgent(self.memory, self.reason)
        research = ResearchAgent(self.memory, vector_store=self.vector)
        planner = PlanningAgent(self.memory, knowledge_graph=KnowledgeGraph())

        self.agent_manager = AgentManager(conv, research, planner)

        self.loop = CognitiveLoop(self.embed, self.vector, self.reason, self.agent_manager)
        self.kg = KnowledgeGraph()
        self.extractor = KnowledgeExtractor()

    def process(self, text: str) -> str:
        # semantic parse (optional)
        sem = self.semantic.analyze(text)

        # cognitive loop
        result = self.loop.process(text)

        # extract some concepts and update knowledge graph
        concepts = self.extractor.extract(text)
        for c in concepts:
            self.kg.add_concept(c)

        # also store in conversation memory
        try:
            self.memory.store_user(text)
        except Exception:
            pass

        # result['response'] may be a string
        resp = result.get('response') if isinstance(result, dict) else str(result)

        try:
            self.memory.store_ai(resp)
        except Exception:
            pass

        return resp
