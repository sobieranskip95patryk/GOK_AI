import json
import os

class KnowledgeGraph:
    """File-backed simple knowledge graph stored in `database/knowledge_graph.json`.
    Nodes are simple strings, edges are dicts {from:..., to:...}.
    """
    def __init__(self, file_path=None):
        base = os.path.dirname(os.path.dirname(__file__))
        default = os.path.normpath(os.path.join(base, '..', 'database', 'knowledge_graph.json'))
        self.file = file_path or default
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        if not os.path.exists(self.file):
            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump({'nodes': [], 'edges': []}, f, ensure_ascii=False)

    def load(self):
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {'nodes': [], 'edges': []}

    def save(self, data):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_concept(self, concept):
        data = self.load()
        if concept not in data.get('nodes', []):
            data['nodes'].append(concept)
            self.save(data)

    def add_relation(self, a, b):
        data = self.load()
        relation = {'from': a, 'to': b}
        if relation not in data.get('edges', []):
            data['edges'].append(relation)
            self.save(data)
