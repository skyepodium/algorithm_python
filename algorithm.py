from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 1. init
        check = [False] * (n + 1)
        st = []
        res = []

        # 2. valid
        def valid(i, j):
            for x, y in st:
                if abs(i - x) == abs(j - y):
                    return False
            return True

        # 3. DFS
        def dfs(i):
            if i >= n:
                temp = []
                for x, y in st:
                    cur = ['.'] * n
                    cur[y] = 'Q'
                    temp.append("".join(cur))
                res.append(temp)
                return

            for j in range(n):
                if not check[j] and valid(i, j):
                    st.append((i, j))
                    check[j] = True
                    dfs(i + 1)
                    st.pop()
                    check[j] = False

        dfs(0)

        return res

sl = Solution()
n = 4
# n = 1
res = sl.solveNQueens(n)
print('res', res)