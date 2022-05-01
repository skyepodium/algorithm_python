import re

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def refine(a):
            st = []
            for c in a:
                if c != '#':
                    st.append(c)
                else:
                    if st: st.pop()
            return st

        return refine(s) == refine(t)


sl = Solution()

s = "ab#c"
t = "ad#c"

s = "ab##"
t = "c#d#"

s = "a#c"
t = "b"

s = "a##c"
t = "#a#c"

s = "ab##"
t = "c#d#"


s = "j##xfix"
t = "j###xfix"

res = sl.backspaceCompare(s, t)

print('res', res)