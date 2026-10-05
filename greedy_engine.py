# greedy_engine.py — Level 2/3/4 Container: Greedy Search Engine

import heapq
from heuristic_module import get_heuristic

def is_goal(node, goal):
    return node == goal

def get_neighbors(graph, node):
    return graph.get(node, [])

def reconstruct_path(parent, goal):
    path = [goal]
    while path[-1] in parent:
        path.append(parent[path[-1]])
    return list(reversed(path))

def return_result(path, cost, nodes):
    return {"path": path, "cost": cost, "nodes_expanded": nodes}

def greedy(graph, heuristic, start, goal):
    pq = [(get_heuristic(start), start, [start], 0)]
    visited = set()
    parent = {}
    nodes_expanded = 0

    while pq:
        h, node, path, cost = heapq.heappop(pq)
        nodes_expanded += 1

        if is_goal(node, goal):
            return return_result(path, cost, nodes_expanded)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in get_neighbors(graph, node):
            if neighbor not in visited:
                parent[neighbor] = node
                heapq.heappush(
                    pq,
                    (get_heuristic(neighbor), neighbor,
                     path + [neighbor], cost + weight)
                )

    return return_result(None, float('inf'), nodes_expanded)