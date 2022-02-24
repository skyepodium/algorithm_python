class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 1. init
        st = []

        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                l, r = st[-1] + 1, i
                s = s[:l] + s[l:r][::-1] + s[r:]
                st.pop()

        return s.replace("(", "").replace(")", "")

sl = Solution()
s = "(abcd)"
# s = "(u(love)i)"
s = "(ed(et(oc))el)"
res = sl.reverseParentheses(s)

print('res', res)
