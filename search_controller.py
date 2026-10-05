# search_controller.py — Level 2 Container: Search Controller

from dijkstra_engine import dijkstra
from greedy_engine import greedy

def run_search(algorithm, graph, heuristic, start, goal):
    if algorithm == "dijkstra":
        return dijkstra(graph, start, goal)
    elif algorithm == "greedy":
        return greedy(graph, heuristic, start, goal)
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")