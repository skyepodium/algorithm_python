class Solution:
    def makeGood(self, s: str) -> str:
        res = []

        for c in s:
            top = res[-1] if len(res) > 0 else ""

            if top.lower() == c.lower() and ord(top) != ord(c):
                res.pop()
            else:
                res.append(c)

        return "".join(res)