# dijkstra_engine.py — Level 2/3/4 Container: Dijkstra Search Engine

import heapq

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

def dijkstra(graph, start, goal):
    # Initialize frontier & cost table
    pq = [(0, start, [start])]
    best_cost = {start: 0}
    nodes_expanded = 0

    while pq:
        cost, node, path = heapq.heappop(pq)
        nodes_expanded += 1

        if is_goal(node, goal):
            return return_result(path, cost, nodes_expanded)

        if cost > best_cost.get(node, float('inf')):
            continue

        for neighbor, weight in get_neighbors(graph, node):
            new_cost = cost + weight
            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return return_result(None, float('inf'), nodes_expanded)