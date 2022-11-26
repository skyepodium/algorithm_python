def solution(ability):
    # 1. init
    n = len(ability)
    m = len(ability[0])
    check = [False] * (n)
    res = [0]

    # 2. dfs
    def dfs(idx, power):
        if idx >= m:
            res[0] = max(res[0], power)
            return

        for i in range(n):
            if not check[i]:
                check[i] = True
                dfs(idx + 1, power + ability[i][idx])
                check[i] = False

    dfs(0, 0)

    # 3. return
    return res[0]

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
# ability = [[20, 30], [30, 20], [20, 30]]
print(solution(ability))