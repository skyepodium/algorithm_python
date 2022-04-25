from itertools import permutations

def solution(k, dungeons):
    # 1. init
    res = 0
    n = len(dungeons)
    idx_list = [_ for _ in range(n)]

    # 2. loop
    for idx in permutations(idx_list):
        l = k
        t = 0
        for i in idx:
            a, b = dungeons[i]
            if l < a or l < b: break
            t += 1
            l -= b

        res = max(res, t)

    return res


k = 80
dungeons = [[80,20],[50,40],[30,10]]

res = solution(k, dungeons)

print('res', res)