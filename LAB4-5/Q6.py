#Q6
import heapq

def a_star(graph, heuristics, start, goal):
    frontier = [(heuristics[start], 0, start, [start])]
    visited = {}

    while frontier:
        f, g, curr, path = heapq.heappop(frontier)

        if curr == goal:
            return path, g

        if curr not in visited or g < visited[curr]:
            visited[curr] = g
            for neighbor, cost in graph[curr].items():
                newg = g + cost
                newf = newg + heuristics[neighbor]
                heapq.heappush(frontier, (newf, newg, neighbor, path + [neighbor]))
    return None, 0

gdata = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

hvalues = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

path1, cost1 = a_star(gdata, hvalues, 'A', 'G')
print(f"Initial Optimal Path: {path1} (Cost: {cost1})")

gdata['A']['B'] = 8
gdata['B']['E'] = 7

path2, cost2 = a_star(gdata, hvalues, 'A', 'G')
print(f"Adjusted Path after cost changes: {path2} (Cost: {cost2})")
