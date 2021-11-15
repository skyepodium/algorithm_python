class Solution:
    def binaryGap(self, n: int) -> int:
        # 1. init
        max_dist = 0
        cnt = 0

        # 2. loop
        while n > 0:
            if n % 2 == 1:
                max_dist = max(max_dist, cnt)
                cnt = 1
            else:
                if cnt > 0: cnt += 1

            n //= 2

        return max_dist