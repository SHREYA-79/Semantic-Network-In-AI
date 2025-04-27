!pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt

class SemanticNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_relationship(self, subject, relation, obj):
        self.graph.add_edge(subject, obj, label=relation)

    def show_network(self, save_path=None):
        pos = nx.spring_layout(self.graph)
        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Semantic Network")

        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            print(f"📁 Graph saved as: {save_path}")

        plt.show()

    def query(self, concept):
        print(f"\nKnowledge about '{concept}':")
        if concept not in self.graph:
            print(" - Concept not found.")
            return

        for neighbor in self.graph[concept]:
            relation = self.graph[concept][neighbor]['label']
            print(f" - {concept} {relation} {neighbor}")

# Main driver code
sn = SemanticNetwork()

# --- Input relationships ---
print("📘 Enter relationships (format: subject relation object). Type 'done' to finish.\n")
while True:
    line = input(">> ")
    if line.lower() == 'done':
        break
    try:
        subject, relation, obj = line.strip().split()
        sn.add_relationship(subject, relation, obj)
    except ValueError:
        print("⚠️ Please enter exactly 3 words (subject relation object)")

# --- Input queries ---
print("\n🔍 Query concepts (type 'exit' to stop querying):")
while True:
    concept = input("Query >> ")
    if concept.lower() == 'exit':
        break
    sn.query(concept)

# --- Show and save graph ---
sn.show_network(save_path="semantic_network.png")
