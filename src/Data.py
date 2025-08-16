# Datos del organigrama
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
TITLE = "Organigrama de Company X"
