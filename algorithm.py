class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 1. init
        r_cnt, l_cnt = 0, 0
        res = 0

        # 2. loop
        for c in s:
            if r_cnt >= 0 and l_cnt >= 0 and r_cnt == l_cnt:
                res += 1
                r_cnt, l_cnt = 0, 0

            if c == "R":
                r_cnt += 1
            else:
                l_cnt += 1

        return res