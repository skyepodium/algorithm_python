class Solution:
    def binaryGap(self, n: int) -> int:
        # 1. num_to_binary
        def num_to_binary(n):
            s = ""
            while n > 0:
                s += str(n % 2)
                n //= 2

            return s

        s = num_to_binary(n)

        # 2. loop
        max_dist = 0
        cnt = 0
        for i in range(0, len(s)):
            if s[i] == "1":
                max_dist = max(max_dist, cnt)
                cnt = 1
            else:
                if cnt > 0:
                    cnt += 1

        return max_dist