import networkx as nx
import matplotlib.pyplot as plt
from Data import NODES, EDGES, NODE_SIZE, FIG_SIZE, TITLE

def build_graph(nodes=NODES, edges=EDGES):
    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node["name"], pos=node["pos"], color=node["color"])
    for src, dst, color, _ in edges:
        G.add_edge(src, dst, color=color)
    return G

def get_positions(nodes=NODES):
    return {node["name"]: node["pos"] for node in nodes}

def get_node_colors(nodes=NODES):
    return {node["name"]: node["color"] for node in nodes}

def get_edge_colors(G):
    return [G[u][v]['color'] for u, v in G.edges()]

def get_edge_labels(edges=EDGES):
    return {(src, dst): label for src, dst, _, label in edges if label}

def draw_organogram(
    G, pos, node_colors, edge_colors, edge_labels,
    node_size=NODE_SIZE, fig_size=FIG_SIZE, title=TITLE
):
    fig, ax = plt.subplots(figsize=fig_size)
    for node, color in node_colors.items():
        nx.draw_networkx_nodes(
            G, pos, nodelist=[node], node_color=color, node_shape='s',
            ax=ax, edgecolors='black', linewidths=1.5, node_size=node_size
        )
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2.0, arrows=True, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10)
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=14, label_pos=0.5)
    ax.set_title(title, fontsize=16)
    ax.axis('off')
    return fig

def create_organogram_figure():
    G = build_graph()
    pos = get_positions()
    node_colors = get_node_colors()
    edge_colors = get_edge_colors(G)
    edge_labels = get_edge_labels()
    return draw_organogram(G, pos, node_colors, edge_colors, edge_labels)
