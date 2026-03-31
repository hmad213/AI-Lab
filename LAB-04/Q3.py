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
        return "Goal not found!"


graph = {
    "Entrance": ["Hallway_A", "Hallway_B"],
    "Hallway_A": ["Storage"],
    "Hallway_B": ["Target"],
    "Storage": ["Deep_Vault"]
}

print(dls(graph, "Entrance", "Target", 3))