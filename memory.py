# memory.py — Level 2 Container: Visited / Cost Memory

class Memory:
    def __init__(self):
        self.visited = set()
        self.best_cost = {}

    def mark_visited(self, node):
        self.visited.add(node)

    def set_cost(self, node, cost):
        self.best_cost[node] = cost

    def get_cost(self, node):
        return self.best_cost.get(node, float('inf'))

    def is_visited(self, node):
        return node in self.visited