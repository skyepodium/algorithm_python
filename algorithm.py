from heapq import heappop, heappush

def solution(n, k, cmd):
    # 1. init
    left, right, removed = [], [], []

    # 2. make heap
    for i in range(k):
        heappush(left, -i)
    for i in range(k, n):
        heappush(right, i)

    # 3. cmd
    for c in cmd:
        if c[0] == 'U':
            cnt = int(c.split(" ")[1])
            while left and cnt > 0:
                heappush(right, -heappop(left))
                cnt -= 1
        elif c[0] == 'D':
            cnt = int(c.split(" ")[1])
            while right and cnt > 0:
                heappush(left, -heappop(right))
                cnt -= 1
        elif c[0] == 'C':
            removed.append(heappop(right))

            if not right:
                heappush(right, -heappop(left))
        elif c[0] == 'Z':
            top = removed.pop()
            if top < right[0]:
                heappush(left, -top)
            else:
                heappush(right, top)

    res_left = [-x for x in left]
    total_set = set(res_left + right)

    result = ""
    for i in range(n):
        val = "X"
        if i in total_set:
            val = "O"
        result += val

    return result