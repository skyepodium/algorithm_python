from collections import Counter

def solution(want, number, discount):
    # 1. init
    c = Counter()
    for w, n in zip(want, number):
        c[w] = n

    # 2. discount
    n = len(discount)
    res = 0
    for i in range(n):
        if discount[i] not in c:
            continue
        d = Counter(discount[i:i+10])
        if len(c - d) == 0:
            res += 1

    return res

want = ["b", "a", "r", "p1", "p2"]
number = [3, 2, 2, 2, 1]
discount = ["c", "a", "a", "b", "r", "a", "p1", "b", "p1", "r", "p2", "b", "a", "b"]

res = solution(want, number, discount)

print('res', res)

