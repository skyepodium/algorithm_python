from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            return True
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False