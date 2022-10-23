class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([c[::-1] for c in s.split()])


s = "Let's take LeetCode contest"
s = "God Ding"
sl = Solution()
res = sl.reverseWords(s)

print('res', res)