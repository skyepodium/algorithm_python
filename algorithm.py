class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        base = strs[0]
        res = ""
        size = 0

        for i in range(0, len(base) + 1):
            cur = base[:i]
            notSame = False
            for word in strs:
                if word[:i] != cur:
                    notSame = True
                    break
            if notSame:
                continue

            if len(cur) > size:
                size = len(cur)
                res = cur

        return res

sl = Solution()

strs = ["flower","flow","flight"]
strs = ["a"]
res = sl.longestCommonPrefix(strs)

print(res)