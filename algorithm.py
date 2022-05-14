from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)

        return min(c['b'], c['a'], c['l']//2, c['o']//2, c['n'])


sl = Solution()
text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"
res = sl.maxNumberOfBalloons(text)

print('res', res)
