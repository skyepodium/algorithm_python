from collections import deque

n = int(input())
check = [-1] * (n+1)
path = [0] * (n+1)

def bfs(start_node):
    q = deque()
    q.append(start_node)
    path[start_node] = start_node
    check[start_node] = 0

    while q:
        node = q.popleft()

        next_nodes = []
        if node % 3 == 0:
            next_nodes.append(node // 3)
        if node % 2 == 0:
            next_nodes.append(node // 2)
        if node > 2:
            next_nodes.append(node - 1)

        for next_node in next_nodes:
            if check[next_node] == -1:
                check[next_node] = check[node] + 1
                path[next_node] = node
                q.append(next_node)

bfs(n)

res = []
end_node = 1
print(check[end_node])
while path[end_node] != end_node:
    res.append(end_node)
    end_node = path[end_node]

res.append(n)
print(*res[::-1])