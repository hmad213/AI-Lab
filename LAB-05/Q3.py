import math

maze = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
]

G_COST = 1
ROWS = 7
COLS = 12

def get_heuristic(node: tuple, goal: tuple):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def get_valid_squares(maze: list[list], node):
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    squares = []
    for move in moves:
        x = node[0] + move[0]
        y = node[1] + move[1]
        if x >= ROWS or x < 0:
            continue
        if y >= COLS or y < 0:
            continue
        if maze[x][y] == 0:
            continue

        squares.append((x, y))
    return squares

def greedy_bfs(maze: list[list], start: tuple[int, int], goal: tuple[int, int]):
    frontier = [(start, get_heuristic(start, goal))]
    visited = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        node, cost = frontier.pop(0)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            path = []
            current_node = node
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            return path

        for square in get_valid_squares(maze, node):
            if square not in visited:
                frontier.append((square, get_heuristic(square, goal)))
                came_from[square] = node

def a_star(maze: list[list], start: tuple[int, int], goal: tuple[int, int]):
    frontier = [(start, get_heuristic(start, goal))]
    came_from = {start: None}
    g_costs = {start: 0}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        node, cost = frontier.pop(0)

        if node == goal:
            path = []
            current_node = node
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            return path

        for square in get_valid_squares(maze, node):
            new_g_cost = G_COST + g_costs[node]
            if square not in g_costs or new_g_cost < g_costs[square]:
                g_costs[square] = new_g_cost
                frontier.append((square, get_heuristic(square, goal) + new_g_cost))
                came_from[square] = node



print(greedy_bfs(maze, (6, 0), (0, 11)))
print(a_star(maze, (6, 0), (0, 11)))