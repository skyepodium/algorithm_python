class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 1. init
        res = 0
        in_list = [0 for _ in range(n + 1)]
        out_list = [0 for _ in range(n + 1)]

        # 2. loop
        for a, b in trust:
            in_list[b] += 1
            out_list[a] += 1

        # 3. check
        for i in range(1, n + 1):
            if in_list[i] == n - 1 and out_list[i] == 0:
                return i

        return -1