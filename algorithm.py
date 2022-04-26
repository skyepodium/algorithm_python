from heapq import heappush, heappop


def solution(n, works):
    # 1. pq
    pq = []
    for w in works:
        heappush(pq, -w)

    # 2. loop
    while n > 0 and pq:
        top = heappop(pq)
        if -top >= 2:
            heappush(pq, -(-top-1))
        n -= 1

    # 3. sum
    return sum([x*x for x in pq])

works = [4, 3, 3]
n = 4

res = solution(n, works)
print('res', res)
