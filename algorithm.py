class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

s = "the sky is blue"
s = "  hello world  "
s = "a good   example"

print(Solution().reverseWords(s))