from collections import Counter
import re

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 1. init
        t = re.sub("[^balon]", "", text)
        c = Counter(t)
        res = int(1e4)

        # 2. exception
        if len(c) != 5: return 0

        if c['o'] < 2 or c['l'] < 2: return 0

        # 3. loop
        for key, val in c.items():
            n = val // 2 if key == 'o' or key == 'l' else val
            res = min(res, n)

        return res


sl = Solution()
text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"
res = sl.maxNumberOfBalloons(text)

print('res', res)
