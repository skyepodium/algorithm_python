class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key=lambda x: x[-1])
        return ' '.join([i[:-1] for i in s])


sl = Solution()
s = "is2 sentence4 This1 a3"
print(sl.sortSentence(s))
