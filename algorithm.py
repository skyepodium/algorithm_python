n = int(input())
a, b = 1, 1

for _ in range(n):
    if a > b:
        a, b = b, a

    a += 1

print(a * b)