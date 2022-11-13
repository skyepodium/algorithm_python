from collections import deque

def solution(order):
    # 1. init
    res = 0
    n = len(order)
    s = []
    order = deque(order)

    for i in range(n):
        if i + 1 != order[0]:
            s.append(i + 1)
        else:
            order.popleft()
            res += 1

            while s and order and s[-1] == order[0]:
                s.pop()
                order.popleft()
                res += 1

    return res

order = [4, 3, 1, 2, 5]
order = [5, 4, 3, 2, 1]

print(solution(order))