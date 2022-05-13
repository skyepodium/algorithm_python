t = int(input())

for _ in range(t):
    cnt = int(input())
    a = list(map(int, input().split()))
    sum_val = sum(a)
    min_val = min(a)
    res = sum_val - min_val * cnt
    print(res)