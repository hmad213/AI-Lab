def ucs(graph, start, goal):
    frontier = [(0, start)]
    visited = set()

    while(frontier):
        frontier.sort(key=lambda x: x[0])
        cost, node = frontier.pop(0)

        if node in visited:
            continue

        print(f"Visited: {node}")

        if(node == goal):
            print(f"Goal {goal} found! Cost {cost}")
            return
        
        visited.add(node)

        for next_node, edge_cost in graph.get(node, {}).items():
            if(next_node not in visited):
                frontier.append((edge_cost + cost, next_node))

    print("Goal not found!")


graph = {
    "Earth": {"Moon Base": 10, "Orbital Platform": 5},
    "Orbital Platform": {"Moon Base": 2, "Mars": 60},
    "Moon Base": {"Mars": 50}
}

ucs(graph, "Earth", "Mars")