import tkinter as tk
import matplotlib.pyplot as plt
from Organogram import create_organogram_figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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