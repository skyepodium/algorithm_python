def solution(n):
    check = [False] * n
    res = [0]
    st = []

    def can_put(i, j):
        for x, y in st:
            if abs(i-x) == abs(j-y):
                return False
        return True

    def dfs(idx):
        if idx >= n:
            res[0] += 1
            return

        for i in range(n):
            if not check[i] and can_put(idx, i):
                check[i] = True
                st.append((idx, i))
                dfs(idx + 1)
                check[i] = False
                st.pop()

    dfs(0)
    return res[0]

n = 4
res = solution(n)
print('res', res)