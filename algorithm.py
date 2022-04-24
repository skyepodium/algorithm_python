def solution(citations):
    # 1. init
    res = 0
    max_val = max(citations)
    min_val = min(citations)
    n = len(citations)

    # 2. sort
    citations.sort()

    # 3. lower_bound
    def lower_bound(s, e, target):
        while s < e:
            mid = s + (e - s) // 2
            if citations[mid] < target:
                s = mid + 1
            else:
                e = mid
        return e

    # 4. loop
    for i in range(max_val+1):
        idx = lower_bound(0, n, i)
        upper = n - idx
        if upper >= i:
            res = max(res, i)

    return res


citations = [3, 0, 6, 1, 5]

citations = [1, 1, 1, 1, 1]

res = solution(citations)

print('res', res)