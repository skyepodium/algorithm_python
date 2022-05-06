class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # 1. init
        st = []

        # 2. loop
        for c in s:
            if st:
                t, cnt = st[-1]
                if t == c:
                    if cnt == k - 1:
                        while st and st[-1][0] == c:
                            st.pop()
                    else:
                        st.append((c, cnt + 1))
                else:
                    st.append((c, 1))
            else:
                st.append((c, 1))

        return "".join([t for t, _ in st])

s = "abcd"
k = 2

s = "deeedbbcccbdaa"
k = 3

s = "pbbcggttciiippooaais"
k = 2

sl = Solution()

res = sl.removeDuplicates(s, k)

print('res', res)

