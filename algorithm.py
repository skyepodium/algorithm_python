def solution(people, limit):
    # 1. init
    l = 0
    r = len(people) - 1
    cnt = 0

    # 2. sort
    people.sort()

    # 3. two pointer
    while l <= r:
        cnt += 1
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1

    return cnt