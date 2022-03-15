class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 1. init
        res = ""
        cnt = 0

        # 2. loop
        for c in s:
            if c == '(':
                cnt += 1
                res += c
            elif c == ')':
                if cnt > 0:
                    cnt -= 1
                    res += c
            else:
                res += c

        # 3. exception
        origin = res
        res = ""
        for c in reversed(origin):
            if c == '(' and cnt > 0:
                cnt -= 1
            else:
                res += c

        return res[::-1]
