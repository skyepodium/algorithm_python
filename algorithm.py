n, m = map(int, input().split())

parent = [x for x in range(n)]
power = []

for i in range(n):
    power.append(int(input()))

def find(node):
    if node == parent[node]:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]

for _ in range(m):
    o, p, q = map(int, input().split())
    p -= 1
    q -= 1

    p, q = find(p), find(q)
    if o == 1:
        parent[p] = q
        power[q] += power[p]
        power[p] = 0
    else:
        if power[p] == power[q]:
            power[p], power[q] = 0, 0
        elif power[p] > power[q]:
            parent[q] = p
            power[p] -= power[q]
            power[q] = 0
        else:
            parent[p] = q
            power[q] -= power[p]
            power[p] = 0

remain = sorted([x for x in power if x > 0])
print(len(remain))
print(*remain)