from collections import deque

start_node = input()
end_node = input()

visited = set()
n = len(end_node)

def bfs(start):
    q = deque()
    q.append(start)
    visited.add(start)

    while q:
        node = q.popleft()

        next_nodes = []
        if node[-1] == "A":
            next_nodes.append(node[:len(node)-1])
        if node[0] == "B":
            next_nodes.append(node[1:][::-1])

        for next_node in next_nodes:
            if len(next_node) <= 0: continue
            if not next_node in visited:
                visited.add(next_node)
                q.append(next_node)

bfs(end_node)

print(1 if start_node in visited else 0)