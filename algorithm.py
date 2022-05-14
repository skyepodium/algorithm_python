class Solution:
    def makeFancyString(self, s: str) -> str:
        # 1. init
        st = []

        # 2. loop
        for c in s:
            a, b = st[-1] if st else ('', 0)

            if a == c and b == 2: continue

            cnt = b + 1 if a == c else 1

            st.append((c, cnt))

        return "".join([a for a, b in st])


sl = Solution()

s = "leeetcode"
s = "aaabaaaa"
s = "aab"
res = sl.makeFancyString(s)

print('res', res)