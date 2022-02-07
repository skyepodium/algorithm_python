from collections import defaultdict

def solution(clothes):
    # 1. init
    d = defaultdict(int)
    res = 1

    # 2. make dict
    for c, t in clothes:
        d[t] += 1

    # 3. all combinations
    for x in d.values():
        res *= (x+1)

    return res - 1
