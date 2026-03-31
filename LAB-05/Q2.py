graph = {
    "S": {"A": 1, "G": 10},
    "A": {"B": 2, "C": 1},
    "B": {"D": 5},
    "C": {"D": 3, "G": 4},
    "D": {"G": 3}               #Random value since it is missing
}

heuristic = {
    "A": 3,
    "B": 4,
    "C": 2,
    "D": 6,
    "S": 5,
    "G": 0
}

def a_star_search(graph: dict, heuristic: dict, start: str, goal: str):
    frontier = [(start, heuristic.get(start, 0))]
    came_from = {start: None}
    g_costs = {start: 0}

    while(frontier):
        frontier.sort(key=lambda x: x[1])
        node, cost = frontier.pop(0)
        
        print(f"{node}, {cost}")

        if node == goal:
            path = []
            currentNode = node
            while currentNode:
                path.append(currentNode)
                currentNode = came_from[currentNode]
            path.reverse()
            return path

        for key, g in graph.get(node, {}).items():
            new_g = g + g_costs[node]
            if key not in g_costs or new_g < g_costs[key]:
                frontier.append((key, heuristic.get(key, 1000) + new_g))
                g_costs[key] = new_g
                came_from[key] = node

print(a_star_search(graph, heuristic, "S", "G"))