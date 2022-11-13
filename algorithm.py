def solution(elements):
    # 1. init
    s = set()
    n = len(elements)

    # 2. loop
    for num in range(1, n+1):
        for l in range(n):
            r = l + num
            if r > n:
                cur = sum(elements[l:r] + elements[:r - n])
            else:
                cur = sum(elements[l:r])

            if not cur in s:
                s.add(cur)
        print()

    return len(s)

elements = [7,9,1,1,4]
print(solution(elements))