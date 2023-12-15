class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return first[:i]
        return first
