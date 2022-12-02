class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # 1. init
        str_num = str(num)
        n = len(str_num)
        res = 0

        # 2. loop
        for i in range(n-k+1):
            s = str_num[i:i+k]
            s_num = int(s)
            if s_num == 0:
                continue
            if num % s_num == 0:
                res += 1

        return res

sl = Solution()

num = 240
k = 2

num = 430043
k = 2

res = sl.divisorSubstrings(num, k)

print('res', res)