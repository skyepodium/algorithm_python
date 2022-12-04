from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 1. init
        s_q = deque(s)
        t_q = deque(t)

        # 2. loop
        while s_q and t_q:
            s_top = s_q[0]
            t_top = t_q[0]
            if s_top == t_top:
                s_q.popleft()
                t_q.popleft()
            else:
                t_q.popleft()

        return not s_q

sl = Solution()

s = "abc"
t = "ahbgdc"

s = "axc"
t = "ahbgdc"

s = ""
t = "ahbgdc"

s = "b"
b = "abc"

res = sl.isSubsequence(s, t)

print('res', res)