from heapq import heappop, heappush

n = int(input())
m = int(input())
v = [[] for _ in range(n+1)]
MAX_INT = int(1e12)
d = [MAX_INT] * (n+1)
path = [0] * (n+1)

for _ in range(m):
    s, e, c = map(int, input().split())
    v[s].append((e, c))

start_node, end_node = map(int, input().split())

def dijkstra(start_node):
    pq = []
    d[start_node] = 0
    pq.append((d[start_node], start_node))

    while pq:
        cost, node = heappop(pq)
        if cost > d[node]:
            continue

        for next_node, next_cost in v[node]:
            if d[next_node] > d[node] + next_cost:
                d[next_node] = d[node] + next_cost
                path[next_node] = node
                heappush(pq, (d[next_node], next_node))


path[start_node] = start_node
dijkstra(start_node)

print(d[end_node])

st = []
while path[end_node] != end_node:
    st.append(end_node)
    end_node = path[end_node]
st.append(start_node)
print(len(st))
print(*st[::-1])