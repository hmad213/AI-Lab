def dls(graph, start, goal, depth_limit):
    def dfs(node, depth, current_path):
        if depth > depth_limit:
            return None

        if node == goal:
            return current_path + [node]

        for neighbor in graph.get(node, []):
            if neighbor not in current_path:
                path = dfs(neighbor, depth + 1, current_path + [node])
                if path:
                    return path

        return None
    
    path = dfs(start, 0, [])
    if path:
        return path
    else:
        return None
    
def iterative_deepening(graph, start, goal, maximum_depth):
    for i in range(maximum_depth + 1):
        print(f"Searching at depth {i}")
        path = dls(graph, start, goal, i)
        if path:
            print(path)
            return
        print(f"Goal not found at depth {i}")

graph = {
    "Main Box": ["Zone A", "Zone B"],
    "Zone A": ["Switch 1", "Switch 2"],
    "Zone B": ["Breaker 101"]
}

iterative_deepening(graph, "Main Box", "Breaker 101", 3)
        