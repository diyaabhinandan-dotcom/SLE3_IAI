# input_module.py — Level 2 Container: Input Module

def accept_input(graph, start, goal):
    """Validate the user's input before passing to the controller."""
    if not graph:
        raise ValueError("Graph is empty")
    if start not in graph:
        raise ValueError(f"Start node '{start}' not in graph")
    if goal not in graph:
        raise ValueError(f"Goal node '{goal}' not in graph")
    return graph, start, goal