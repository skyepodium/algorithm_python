from heapq import heappush, heappop, heapify


def solution(scoville, K):
    # 1. init
    answer = 0

    # 2. list to heap
    heapify(scoville)

    # 3. loop
    while len(scoville) >= 2 and scoville[0] < K:
        a = heappop(scoville)
        b = heappop(scoville)

        heappush(scoville, a + b * 2)
        answer += 1

    return answer if scoville[0] >= K else -1