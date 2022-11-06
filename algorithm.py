from collections import Counter

n = int(input())

for _ in range(n):
    s = input()
    c = Counter(s.lower())

    res = "GOOD" if c['g'] > c['b'] else "A BADDY"
    if c['g'] == c['b']:
        res = "NEUTRAL"

    print(f"{s} is {res}")
