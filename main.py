# main.py — Entry point — wires all containers together.

from common import GRAPH, HEURISTIC, START, GOAL
from input_module import accept_input
from search_controller import run_search
from result_module import format_result

def main():
    graph, start, goal = accept_input(GRAPH, START, GOAL)

    result_d = run_search("dijkstra", graph, HEURISTIC, start, goal)
    print(format_result(result_d, "Dijkstra"))

    result_g = run_search("greedy", graph, HEURISTIC, start, goal)
    print(format_result(result_g, "Greedy"))

if __name__ == "__main__":
    main()