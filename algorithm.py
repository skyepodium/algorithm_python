class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # 1. init
        a = Counter(words1)
        b = Counter(words2)
        s = set()
        res = 0

        # 2. loop
        for key, val in a.items():
            if val == 1:
                s.add(key)

        for key, val in b.items():
            if val == 1 and key in s:
                res += 1

        return res
