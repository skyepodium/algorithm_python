a, b, c = map(int, input().split())
res = 0

res = max(max(res, a * b / c), a / b * c)
print(int(res))