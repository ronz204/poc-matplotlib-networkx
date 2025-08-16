
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Any
from Data import OrganogramData

class OrganogramGraph:
    """Clase para construir y dibujar el organigrama usando NetworkX y Matplotlib."""
    def __init__(self, data: OrganogramData) -> None:
        self.data = data
        self.G = self._build_graph()
        self.pos = self._get_positions()
        self.node_colors = self._get_node_colors()
        self.edge_colors = self._get_edge_colors()
        self.edge_labels = self._get_edge_labels()

    def _build_graph(self) -> nx.DiGraph:
        G = nx.DiGraph()
        for node in self.data.nodes:
            G.add_node(node["name"], pos=node["pos"], color=node["color"])
        for src, dst, color, _ in self.data.edges:
            G.add_edge(src, dst, color=color)
        return G

    def _get_positions(self) -> Dict[str, Any]:
        return {node["name"]: node["pos"] for node in self.data.nodes}

    def _get_node_colors(self) -> Dict[str, str]:
        return {node["name"]: node["color"] for node in self.data.nodes}

    def _get_edge_colors(self) -> list:
        return [self.G[u][v]['color'] for u, v in self.G.edges()]

    def _get_edge_labels(self) -> Dict:
        return {(src, dst): label for src, dst, _, label in self.data.edges if label}

    def draw(self) -> plt.Figure:
        fig, ax = plt.subplots(figsize=self.data.fig_size)
        for node, color in self.node_colors.items():
            nx.draw_networkx_nodes(
                self.G, self.pos, nodelist=[node], node_color=color, node_shape='s',
                ax=ax, edgecolors='black', linewidths=1.5, node_size=self.data.node_size
            )
        nx.draw_networkx_edges(self.G, self.pos, edge_color=self.edge_colors, width=2.0, arrows=True, arrowsize=20)
        nx.draw_networkx_labels(self.G, self.pos, font_size=10)
        if self.edge_labels:
            nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=self.edge_labels, font_color='black', font_size=14, label_pos=0.5)
        ax.set_title(self.data.title, fontsize=16)
        ax.axis('off')
        return fig

def create_organogram_figure() -> plt.Figure:
    """Función de conveniencia para crear la figura del organigrama."""
    data = OrganogramData()
    graph = OrganogramGraph(data)
    return graph.draw()
