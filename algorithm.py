def solution(numbers):
    # 1. init
    answer = 0
    size = len(numbers)

    # 2. check prime
    def is_prime(num):
        if num <= 1:
            return False

        end = int(num ** 0.5) + 1
        for i in range(2, end):
            if num % i == 0:
                return False
        return True

    # 3. dfs
    check = [False for _ in range(size)]
    ss = set()
    def dfs(idx, stack):
        if not (len(stack) >= 2 and stack[0] == "0") and stack:
            val = int("".join(stack))
            if val not in ss and is_prime(val):
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

    return len(ss)


s = "17"
res = solution(s)

print("res", res)