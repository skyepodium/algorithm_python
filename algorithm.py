from heapq import heappush, heappop


def solution(k, score):
    res = []
    pq = []

    for s in score:
        if len(res) < k:
            heappush(pq, s)
        else:
            if pq[0] < s:
                heappop(pq)
                heappush(pq, s)
        res.append(pq[0])

    return res