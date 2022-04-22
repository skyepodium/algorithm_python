class Solution:
    def digitSum(self, s: str, k: int) -> str:

        def sum_str(st):
            res = 0
            for c in st:
                res += int(c)
            return str(res)

        while len(s) > k:
            base = ""
            for i in range(0, len(s), k):
                c = s[i:i+k]
                base += sum_str(c)
            s = base

        return s

sl = Solution()
s = "11111222223"
k = 3
s = "00000000"
k = 3
res = sl.digitSum(s, k)

print('res', res)