n = int(input())
a = list(map(int, input().split()))
b = [(idx + 1, val) for idx, val in enumerate(a)]
b.sort(reverse=True, key=lambda x: x[1])
print(b[1][0])