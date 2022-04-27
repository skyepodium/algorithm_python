def solution(n, times):
    # 1. init
    max_val = max(times)
    res = max_val * n
    s, e = 0, max_val * n

    # 2. cal cnt
    def cal_cnt(a):
        r = 0
        for t in times:
            r += a // t
        return r

    # 3. binary search
    while s < e:
        mid = s + (e - s) // 2

        cnt = cal_cnt(mid)

        if cnt < n:
            s = mid + 1
        else:
            res = min(res, mid)
            e = mid

    return res
