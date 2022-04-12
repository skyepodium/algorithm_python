class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 1. init
        res = letters[0]
        t = ord(target)
        val = 1000

        # 2. loop
        for l in letters:
            c = ord(l)
            if c > t and c < val:
                res = l
                val = c

        return res