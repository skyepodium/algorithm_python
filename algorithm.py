class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # 1. init
        res = 0

        # 2. loop
        for w in text.split(" "):
            isOk = True
            for a in w:
                if a in brokenLetters:
                    isOk = False
                    break
            if isOk:
                res += 1

        return res