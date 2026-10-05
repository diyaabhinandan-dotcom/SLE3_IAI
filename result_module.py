# result_module.py — Level 2 Container: Result Module

def format_result(result, algorithm):
    if result["path"] is None:
        return f"[{algorithm}] No path found. Nodes expanded: {result['nodes_expanded']}"

    return (
        f"[{algorithm}] Path: {' -> '.join(result['path'])}\n"
        f"           Cost: {result['cost']}\n"
        f"           Nodes expanded: {result['nodes_expanded']}"
    )