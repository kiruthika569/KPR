def bfs(graph,start_node):
    visited=set()
    queue=deque()
    queue.append(start_node)
    visited.add(start_node)
    print("BFS Traversal Order:")
    while queue:
        current_node=queue.popleft()
        print(current_node,end=' ')
        