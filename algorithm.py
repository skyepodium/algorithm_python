class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1. init
        seen = set()
        n = len(s)
        cnt = 2 ** k

        # 2. loop
        for i in range(n - k + 1):
            cur = s[i:i+k]
            if cur not in seen:
                cnt -= 1
                seen.add(cur)
            if cnt == 0: return True

        return False

sl = Solution()

s = "00110110"
k = 2

s = "0110"
k = 1

s = "0110"
k = 2

res = sl.hasAllCodes(s, k)

print('res', res)
