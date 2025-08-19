import heapq

def a_star_tree_search(graph, start, goal, heuristic, cost):
    # Priority queue with (f(n), node, g(n))
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, 0))
    
    parent = {start: None}

    while priority_queue:
        f, current, g = heapq.heappop(priority_queue)

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # reverse path

        for neighbor in graph[current]:
            new_g = g + cost[(current, neighbor)]
            f_val = new_g + heuristic[neighbor]

            if neighbor not in parent:  # since it's tree search (no re-expansion check)
                parent[neighbor] = current
                heapq.heappush(priority_queue, (f_val, neighbor, new_g))

    return None  # No path found


# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Example costs (edge weights)
cost = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('B', 'D'): 2,
    ('B', 'E'): 5,
    ('C', 'F'): 1,
    ('E', 'G'): 1
}

# Example heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

# Run A* Tree Search
path = a_star_tree_search(graph, 'A', 'G', heuristic, cost)
print("Path found:", path)