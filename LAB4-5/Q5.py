#Q5
def best_first_search(graph, start, goals):
    remaining_goals = set(goals)
    current_pos = start
    complete_path = [start]

    while remaining_goals:
        frontier = [(0, current_pos, [current_pos])]
        visited = set()
        nearest_goal_path = None

        while frontier:
            _, curr, path = heapq.heappop(frontier)
            if curr in remaining_goals:
                nearest_goal_path = (curr, path)
                break
            
            if curr not in visited:
                visited.add(curr)
                for neighbor, weight in graph.get(curr, []):
                    heapq.heappush(frontier, (weight, neighbor, path + [neighbor]))
        
        if not nearest_goal_path:
            break
            
        goal_found, segment = nearest_goal_path
        complete_path.extend(segment[1:])
        current_pos = goal_found
        remaining_goals.remove(goal_found)

    return complete_path

maze_graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [], 'J': [], 'K': [], 'L': [], 'M': []
}

final_maze_path = best_first_search(maze_graph, 'S', ['I', 'J'])
print(f"Path covering all goals: {final_maze_path}")
