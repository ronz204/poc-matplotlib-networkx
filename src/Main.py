import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

NODES = [
  {"name": "CEO", "pos": (0, 2), "color": "#f0f0f0"},
  {"name": "Team A Lead", "pos": (-1, 1), "color": "#b3e0ff"},
  {"name": "Team B Lead", "pos": (1, 1), "color": "#ffd9d9"},
  {"name": "Staff A", "pos": (-1.5, 0), "color": "#b3e0ff"},
  {"name": "Staff B", "pos": (-0.5, 0), "color": "#b3e0ff"},
  {"name": "Staff C", "pos": (0.5, 0), "color": "#ffd9d9"},
  {"name": "Staff D", "pos": (1.5, 0), "color": "#ffd9d9"},
  {"name": "Staff E", "pos": (2.5, 0), "color": "#ffd9d9"},
]

EDGES = [
  ("CEO", "Team A Lead", "blue", "A"),
  ("CEO", "Team B Lead", "red", "B"),
  ("Team A Lead", "Staff A", "blue", None),
  ("Team A Lead", "Staff B", "blue", None),
  ("Team B Lead", "Staff C", "red", None),
  ("Team B Lead", "Staff D", "red", None),
  ("Team B Lead", "Staff E", "red", None),
]

NODE_SIZE = 2000
FIG_SIZE = (10, 6)
TITLE = "Pruebas"

def build_graph(nodes, edges):
    """Crea y retorna un DiGraph de NetworkX con nodos y bordes configurados."""
    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node["name"], pos=node["pos"], color=node["color"])
    for src, dst, color, _ in edges:
        G.add_edge(src, dst, color=color)
    return G

def get_positions(nodes):
    """Devuelve un diccionario de posiciones para los nodos."""
    return {node["name"]: node["pos"] for node in nodes}

def get_node_colors(nodes):
    """Devuelve un diccionario de colores para los nodos."""
    return {node["name"]: node["color"] for node in nodes}

def get_edge_colors(G):
    """Devuelve una lista de colores de los bordes en el grafo G."""
    return [G[u][v]['color'] for u, v in G.edges()]

def get_edge_labels(edges):
    """Devuelve un diccionario de etiquetas para los bordes que las tengan."""
    return {(src, dst): label for src, dst, _, label in edges if label}

def draw_organogram(G, pos, node_colors, edge_colors, edge_labels, node_size=NODE_SIZE, fig_size=FIG_SIZE, title=TITLE):
    """Dibuja el organigrama y retorna la figura de Matplotlib."""
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
    """Crea la figura del organigrama usando los datos y funciones auxiliares."""
    G = build_graph(NODES, EDGES)
    pos = get_positions(NODES)
    node_colors = get_node_colors(NODES)
    edge_colors = get_edge_colors(G)
    edge_labels = get_edge_labels(EDGES)
    return draw_organogram(G, pos, node_colors, edge_colors, edge_labels)

def main():
    """Configura la ventana principal de Tkinter y el lienzo para el gráfico."""
    root = tk.Tk()
    root.title("Organigrama de Empresa")

    def on_closing():
        plt.close('all')
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    fig = create_organogram_figure()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()