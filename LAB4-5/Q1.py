#Q1
from collections import deque

def BFS():
    grid = [
        [1, 1, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1]
    ]
    start, goal = (0, 0), (3, 3)
    rows, cols = 4, 4

    def get_neighbors(pos):
        r, c = pos

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                yield (nr, nc)

    queue = deque([start])
    visited = {start: None}
    traversal_order = []

    while queue:
        curr = queue.popleft()
        traversal_order.append(curr)
        if curr == goal: break

        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                visited[neighbor] = curr
                queue.append(neighbor)

    path, temp = [], goal
    while temp:
        path.append(temp)
        temp = visited[temp]

    print(f"Traversal Order: {traversal_order}")
    print(f"Shortest Path: {path[::-1]}")

BFS()
