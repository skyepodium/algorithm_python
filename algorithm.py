from heapq import heappush, heappop, heapify


def solution(scoville, K):
    # 1. init
    heapify(scoville)
    res = 0

    # 2. loop
    while len(scoville) >= 2 and scoville[0] < K:
        res += 1
        f = heappop(scoville)
        s = heappop(scoville)
        heappush(scoville, f + s)

    return res if scoville[0] >= K else -1