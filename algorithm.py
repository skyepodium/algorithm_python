# 1. init
n = int(input())
MAX_VAl = 1000001 * 16
MAX_INT = 1 << n
v = []
d = [[MAX_VAl for _ in range(MAX_INT)] for _ in range(n)]
size = 1 << n

# 2. make graph
for _ in range(n):
    v.append(list(map(int, input().split())))

# 3. travel
# cur 도시를 방문하고, 나머지 모든 도시를 방문했을때 최소 비용
def go(cur, status):
    # 1) 이미 방문한 경우 - memoization
    if d[cur][status] != MAX_VAl:
        return d[cur][status]

    if status == size - 1 and v[cur][0] != 0: return v[cur][0]

    # 2) 탐색
    for next in range(n):
        # 길이 없거나, 이미 방문한 도시이면 건너뜀
        if v[cur][next] == 0 or status & 1 << next: continue

        d[cur][status] = min(d[cur][status], go(next, status | (1 << next)) + v[cur][next])

    return d[cur][status]

res = go(0, 1)

print(res)

