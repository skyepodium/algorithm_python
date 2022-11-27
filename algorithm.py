from collections import deque

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        q = deque(list(s))

        for _ in range(n):
            if "".join(q) == goal:
                return True
            q.append(q.popleft())

        return False

sl = Solution()
s = "abcde"
goal = "cdeab"

s = "abcde"
goal = "abced"
res = sl.rotateString(s, goal)

print('res', res)