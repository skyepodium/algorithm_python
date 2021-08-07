class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        strs.sort(key=lambda x: len(x))

        base = strs[0]
        res = ""
        size = 0

        for i in range(0, len(base)):
            cur = base[i]
            for word in strs:
                if word[i] != cur:
                    return res

            if len(word[:i + 1]) > size:
                size = i + 1
                res = word[:i + 1]

        return res

sl = Solution()
input = ["flower","flow","flight"]
res = sl.longestCommonPrefix(input)
print('res', res)