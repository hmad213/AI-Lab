graph = {
    "S": {"A": 3, "B": 2},
    "A": {"C": 4, "D": 1},
    "B": {"E": 3, "F": 1},
    "E": {"H": 5},
    "F": {"I": 2, "G": 3}
}

heuristic = {
    "A": 12,
    "B": 4,
    "C": 7,
    "D": 3,
    "E": 8,
    "F": 2,
    "H": 4,
    "I": 9,
    "S": 13,
    "G": 0
}

def greedy_bfs(graph: dict, heuristic: dict, start: str, goal: str):
    frontier = [(start, heuristic.get(start, 0))]
    came_from = {start: None}
    visited = set()

    while(frontier):
        frontier.sort(key=lambda x: x[1])
        node, cost = frontier.pop(0)
        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            currentNode = node
            while currentNode:
                path.append(currentNode)
                currentNode = came_from[currentNode]
            path.reverse()
            return path

        for key in graph.get(node, {}):
            if key not in visited:
                frontier.append((key, heuristic.get(key, 1000)))
                came_from[key] = node

print(greedy_bfs(graph, heuristic, "S", "G"))