class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # 1. init
        s = sentence.split(" ")

        # 2. loop
        prev = s[-1]
        for c in s:
            if prev[-1] != c[0]:
                return False
            prev = c

        return True