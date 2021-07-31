class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip().split(" ")

        size = len(res)

        if size - 1 < 0: return 0

        return len(res[size - 1])
