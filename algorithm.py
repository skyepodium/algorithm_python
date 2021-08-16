def solution(numbers):
    # 1. init
    size = len(numbers)
    max_int = int("".join(sorted(numbers, reverse=True))) + 1
    d = [True for _ in range(max_int)]

    # 2. eratos
    def eratos(n):
        m = int(n ** 0.5) + 1
        for i in range(2, m):
            for j in range(i+i, max_int, i):
                if d[j]:
                    d[j] = False
    eratos(max_int)

    # 3. dfs
    check = [False for _ in range(size)]
    ss = set()
    def dfs(idx, stack):
        if not (len(stack) >= 2 and stack[0] == "0") and stack:
            val = int("".join(stack))
            if val not in ss and val >= 2 and d[val]:
                ss.add(val)

        if idx == size:
            return

        for i in range(size):
            if not check[i]:
                check[i] = True
                stack.append(numbers[i])
                dfs(idx + 1, stack)
                check[i] = False
                stack.pop()

    dfs(0, [])

    return len(ss)


s = "011"
res = solution(s)

print(res)


