from collections import Counter


def solution(gems):
    # 1. init
    n = len(gems)
    total_cnt = len(set(gems))
    c = Counter()
    res = [0, n-1]

    # 2. two pointer
    s = 0
    for e, cur in enumerate(gems):
        # 1) cnt update
        c[cur] += 1

        # 2) minify
        while len(c) >= total_cnt:
            if e - s < res[1] - res[0]:
                res[0], res[1] = s, e

            s_val = gems[s]
            c[s_val] -= 1
            if c[s_val] == 0:
                c.pop(s_val)
            s += 1

    return [x+1 for x in res]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

gems = ["AA", "AB", "AC", "AA", "AC"]

gems = ["XYZ", "XYZ", "XYZ"]

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]



res = solution(gems)

print('res', res)