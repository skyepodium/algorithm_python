s = 0
a = []

for _ in range(9):
    n = int(input())
    s += n
    a.append(n)

def check():
    for i in range(9):
        for j in range(i + 1, 9):
            if s - a[i] - a[j] == 100:
                return i, j
    return -1, -1

i, j = check()

for k in range(9):
    if k != i and k != j:
        print(a[k])