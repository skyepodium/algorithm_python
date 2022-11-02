n, m = map(int, input().split())
j = int(input())

res = 0
l, r = 1, m

for _ in range(j):
    x = int(input())
    l_delta, r_delta = abs(x-l), abs(x-r)

    if x < l:
        l -= l_delta
        r -= l_delta
        res += l_delta
    elif x > r:
        l += r_delta
        r += r_delta
        res += r_delta

print(res)