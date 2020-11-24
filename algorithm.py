from collections import deque


def bfs(start_node):
    q = deque()
    check[start_node] = 0
    q.append(start_node)

    while q:
        node = q.popleft()

        for n_node in v[node]:
            if check[n_node] == -1:
                check[n_node] = check[node] + 1
                q.append(n_node)


n, m, k, x = map(int, input().split())
v = [[] for _ in range(n+1)]
check = [-1 for _ in range(n+1)]
cnt = 0

for _ in range(m):
    start_point, end_point = map(int, input().split())
    v[start_point].append(end_point)

bfs(x)

for i in range(0, n+1):
    if k == check[i]:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)


