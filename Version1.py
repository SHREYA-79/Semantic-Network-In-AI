!pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt

class SemanticNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_relationship(self, subject, relation, obj):
        self.graph.add_edge(subject, obj, label=relation)

    def show_network(self):
        pos = nx.spring_layout(self.graph)
        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Semantic Network")
        plt.show()

    def query(self, concept):
        print(f"\nKnowledge about '{concept}':")
        if concept not in self.graph:
            print(" - Concept not found.")
            return

        for neighbor in self.graph[concept]:
            relation = self.graph[concept][neighbor]['label']
            print(f" - {concept} {relation} {neighbor}")

# Example usage
if __name__ == "__main__":
    sn = SemanticNetwork()

    # Add some relationships
    sn.add_relationship("Dog", "is-a", "Mammal")
    sn.add_relationship("Dog", "can", "Bark")
    sn.add_relationship("Mammal", "has-part", "Tail")
    sn.add_relationship("Bird", "can", "Fly")
    sn.add_relationship("Bird", "is-a", "Animal")

    # Query
    sn.query("Dog")
    sn.query("Bird")

    # Visualize
    sn.show_network()
