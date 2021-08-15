import collections


def solution(n, lost, reserve):
    answer = 0

    remain_diff = collections.Counter(reserve) - collections.Counter(lost)
    remains = list(remain_diff.keys())

    lost_diff = collections.Counter(lost) - collections.Counter(reserve)
    losts = list(lost_diff.keys())

    cnt = 0
    for val in losts:
        if val + 1 in remains:
            cnt += 1
            remains.remove(val + 1)
        elif val - 1 in remains:
            cnt += 1
            remains.remove(val - 1)

    return n - len(losts) + cnt