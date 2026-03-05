import os

ROOT = os.path.dirname(os.path.dirname(__file__))
DATABASE_DIR = os.path.normpath(os.path.join(ROOT, '..', 'database'))
EMBEDDING_DIM = 128

# file names
CONVERSATIONS_FILE = os.path.join(DATABASE_DIR, 'conversations.json')
VECTORS_FILE = os.path.join(DATABASE_DIR, 'vectors.json')
KNOWLEDGE_GRAPH_FILE = os.path.join(DATABASE_DIR, 'knowledge_graph.json')
KNOWLEDGE_FILE = os.path.join(DATABASE_DIR, 'knowledge.json')
