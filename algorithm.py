from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        # 1. init
        check = [False] * (n + 1)
        st = []
        res = [0]

        # 2. valid
        def valid(i, j):
            for x, y in st:
                if abs(i - x) == abs(j - y):
                    return False
            return True

        # 3. DFS
        def dfs(i):
            if i >= n:
                res[0] += 1
                return

            for j in range(n):
                if not check[j] and valid(i, j):
                    st.append((i, j))
                    check[j] = True
                    dfs(i + 1)
                    st.pop()
                    check[j] = False

        dfs(0)

        return res[0]

sl = Solution()
n = 4
# n = 1
res = sl.solveNQueens(n)
print('res', res)