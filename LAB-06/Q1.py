graph = {
    "S": {"A": 2, "B": 5, "C": 4},
    "A": {"D": 7, "E": 3},
    "B": {"F": 6},
    "C": {"G": 2},
    "D": {"T": 4},
    "E": {"T": 6},
    "F": {"T": 6}
}

def beam_search(graph: dict[dict], start: str, goal: str, k: int):
    beam = [([start], 0)]

    while beam:
        candidates = []
        for path, cost in beam:
            node = path[-1]
            if node == goal:
                return path, cost
            
            for neighbor, edge_cost in graph.get(node, {}).items():
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                candidates.append((new_path, new_cost))

        candidates.sort(key=lambda x: x[1])
        beam = candidates[:k]

    return [], 0

path, cost = beam_search(graph, "S", "T", 1)
print(f"k: 1, path: {path}, Cost: {cost}")
path, cost = beam_search(graph, "S", "T", 2)
print(f"k: 2, path: {path}, Cost: {cost}")        
path, cost = beam_search(graph, "S", "T", 3)
print(f"k: 3, path: {path}, Cost: {cost}")    