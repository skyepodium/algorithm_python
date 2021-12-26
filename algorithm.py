class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 1. init
        result = 0

        # 2. getNum
        def getNum(c):
            return ord(c) - ord('A') + 1

        # 3. loop
        for c in columnTitle:
            result = result * 26 + getNum(c)

        return result