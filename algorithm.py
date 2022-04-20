import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        # 1. init
        res = 0

        # 2. loop
        for r in re.split(" +", sentence):
            if re.fullmatch("[a-z]+", r) and r.lower() == r:
                res += 1
            elif re.fullmatch("[a-z]+-[a-z]+[\\.!, ]*", r):
                res += 1
            elif re.fullmatch("[a-z]*[\\.!, ]", r):
                res += 1

        return res

sl = Solution()
sentence = "cat and  dog"
# sentence = "!this  1-s b8d!"
# sentence = "alice and  bob are playing stone-game10"
# sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
res = sl.countValidWords(sentence)

print('res', res)