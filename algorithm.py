import re

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def refine(a):
            while True:
                cur = re.search("#", a)
                if not cur: break

                l, r = cur.start(), cur.end()

                if l == 0:
                    a = a[l+1:]
                else:
                    a = a[:l-1] + a[r:]

            return a

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