from collections import deque

def solution(queue1, queue2):
    # 1. init
    queue1, queue2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    total = s1 + s2
    res = 0
    s = set()

    if total != (total // 2) * 2:
        return -1

    # 2. loop
    while queue1 and queue2 and s1 != s2:
        res += 1
        key = f"s1{s1}{queue1[0]}s2{s2}{queue2[0]}"
        if key in s:
            return -1
        s.add(key)

        if s1 > s2:
            front = queue1.popleft()
            s1 -= front
            queue2.append(front)
            s2 += front
        else:
            front = queue2.popleft()
            s2 -= front
            queue1.append(front)
            s1 += front

    if not queue1 or not queue2:
        return -1

    return res


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

queue1 = [1, 1]
queue2 = [1, 5]

res = solution(queue1, queue2)
print('res', res)
