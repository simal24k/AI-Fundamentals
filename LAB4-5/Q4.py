#Q4
import heapq

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    cheapest_costs = {start: 0}

    while frontier:
        (cost, current, path) = heapq.heappop(frontier)

        if current == goal:
            return path, cost

        for neighbor, weight in graph[current].items():
            new_cost = cost + weight
            if neighbor not in cheapest_costs or new_cost < cheapest_costs[neighbor]:
                cheapest_costs[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))
    return None, float('inf')

delivery_graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

path, total_cost = ucs(delivery_graph, 'S', 'G')
print(f"Shortest Delivery Route: {path}")
print(f"Total Cost: {total_cost}")
