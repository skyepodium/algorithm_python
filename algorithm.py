n = int(input())

MAX_VAL = -1
res = -1
s = []
a = []

def dfs(idx, i):
    if idx >= 5:
        if len(s) == 3:
            val = sum(s) % 10
            global MAX_VAL, res
            if val >= MAX_VAL:
                MAX_VAL = val
                res = i
        return

    s.append(a[idx])
    dfs(idx + 1, i)
    s.pop()

    dfs(idx + 1, i)

for i in range(1, n+1):
    a = list(map(int, input().split()))
    dfs(0, i)

print(res)