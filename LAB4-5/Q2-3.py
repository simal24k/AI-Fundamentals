#Q2&3
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def dls(node, goal, limit, visited_nodes):
    visited_nodes.append(node)
    if node == goal:
        return [node]
    if limit <= 0:
        return None
    
    for neighbor in graph.get(node, []):
        path = dls(neighbor, goal, limit - 1, visited_nodes)
        if path:
            return [node] + path
    return None

print("\nTASK 2: Depth-Limited Search\n")
for L in [2, 3]:
    visited = []
    result = dls('A', 'H', L, visited)
    print(f"Limit {L}:")
    print(f"Nodes Visited: {visited}")
    print(f"Path Found: {result}\n")

print("\nTASK 3: Iterative Deepening Search\n")
target = 'G'
found_path = None
for depth in range(5):
    visited = []
    found_path = dls('A', target, depth, visited)
    print(f"Depth Level {depth}: Visited {visited}")
    if found_path:
        print(f"Final Path to {target}: {found_path}")
        break
