t = int(input())

for _ in range(t):
    q = input()

    a = int(q[0]) + int(q[1]) + int(q[2])
    b = int(q[3]) + int(q[4]) + int(q[5])

    res = "YES" if a == b else "NO"

    print(res)