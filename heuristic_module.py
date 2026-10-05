# heuristic_module.py — Level 2 Container: Heuristic Module

HEURISTIC = {
    'A': 8, 'B': 6, 'C': 5, 'D': 4,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}

def get_heuristic(node):
    """Return the heuristic estimate from node to goal."""
    return HEURISTIC.get(node, float('inf'))