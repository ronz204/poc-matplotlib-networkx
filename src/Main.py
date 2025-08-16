import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def create_organogram_figure():
    """
    Crea la figura del organigrama (sin mostrarla) para incrustar en Tkinter.
    """
    # Crea un grafo dirigido
    G = nx.DiGraph()

    # Añade los nodos (puestos/personas)
    G.add_node("CEO", pos=(0, 2))
    G.add_node("Team A Lead", pos=(-1, 1))
    G.add_node("Team B Lead", pos=(1, 1))
    G.add_node("Staff A", pos=(-1.5, 0))
    G.add_node("Staff B", pos=(-0.5, 0))
    G.add_node("Staff C", pos=(0.5, 0))
    G.add_node("Staff D", pos=(1.5, 0))
    G.add_node("Staff E", pos=(2.5, 0))

    # Añade los bordes (relaciones jerárquicas) y atributos de color
    G.add_edge("CEO", "Team A Lead", color="blue")
    G.add_edge("CEO", "Team B Lead", color="red")
    G.add_edge("Team A Lead", "Staff A", color="blue")
    G.add_edge("Team A Lead", "Staff B", color="blue")
    G.add_edge("Team B Lead", "Staff C", color="red")
    G.add_edge("Team B Lead", "Staff D", color="red")
    G.add_edge("Team B Lead", "Staff E", color="red")

    # Extrae la posición de los nodos
    pos = nx.get_node_attributes(G, 'pos')

    # Extrae los colores de los bordes
    edge_colors = [G[u][v]['color'] for u, v in G.edges()]

    # Dibuja los nodos con colores basados en el equipo
    node_colors = {
        "CEO": "#f0f0f0",
        "Team A Lead": "#b3e0ff",
        "Staff A": "#b3e0ff",
        "Staff B": "#b3e0ff",
        "Team B Lead": "#ffd9d9",
        "Staff C": "#ffd9d9",
        "Staff D": "#ffd9d9",
        "Staff E": "#ffd9d9"
    }

    # Crea la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    for node, color in node_colors.items():
        if node in G.nodes():
            nx.draw_networkx_nodes(
                G, pos, nodelist=[node], node_color=color, node_shape='s',
                ax=ax, edgecolors='black', linewidths=1.5, node_size=2000
            )

    # Dibuja los bordes y las etiquetas
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2.0, arrows=True, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Añade las etiquetas de los bordes (A y B)
    edge_labels = {("CEO", "Team A Lead"): "A", ("CEO", "Team B Lead"): "B"}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=14, label_pos=0.5)

    # Título del gráfico
    ax.set_title("Pruebas", fontsize=12)

    # Oculta los ejes para un aspecto más limpio
    ax.axis('off')
    
    return fig

def main():
    """
    Configura la ventana principal de Tkinter y el lienzo para el gráfico.
    """
    root = tk.Tk()
    root.title("Organigrama de Empresa")
    
    def on_closing():
        plt.close('all')
        root.destroy()
        
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Crea la figura del organigrama
    fig = create_organogram_figure()

    # Crea el lienzo (canvas) de Matplotlib para Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # Inicia el bucle de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()