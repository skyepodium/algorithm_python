class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 1. init
        c = Counter(chars)
        res = 0

        # 2. loop
        for w in words:
            temp = (c | Counter(w)) - c
            if len(temp) == 0:
                res += len(w)

        return res