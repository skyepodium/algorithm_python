from heapq import heappush, heappop

x = int(input())

q = [64]
res = 0

while q and sum(q) > x:
    half = int(heappop(q) / 2)

    if sum(q) + half > x:
        heappush(q, half)
    else:
        heappush(q, half)
        heappush(q, half)

print(len([x for x in q if x != 0]))

