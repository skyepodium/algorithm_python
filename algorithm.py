class Solution:
    def sumZero(self, n: int) -> List[int]:
        # 1. inti
        res = []
        cnt = n // 2

        # 2. loop
        for i in range(1, cnt + 1):
            res.append(i)
            res.append(-i)

        if n % 2 != 0:
            res.append(0)

        return res