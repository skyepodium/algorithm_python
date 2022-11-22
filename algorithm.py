t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    s = sorted(list(s))
    print(ord(s[-1]) - ord('a') + 1)