from collections import Counter

def solution(k, tangerine):
    # 1. init
    cnt_sum = 0
    res = 0

    # 2. init
    for num, cnt in sorted(Counter(tangerine).items(), key=lambda x: -x[1]):
        cnt_sum += cnt
        res += 1
        if cnt_sum >= k:
            return res

    return res


k = 6
t = [1, 3, 2, 5, 4, 5, 2, 3]

k = 4
t = [1, 3, 2, 5, 4, 5, 2, 3]

k = 2
[1, 1, 1, 1, 2, 2, 2, 3]

print(solution(k, t))