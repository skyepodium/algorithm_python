class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 1. init
        st = []

        # 2. loop
        for c in s:
            if st and st[-1] == c:
                while st and st[-1] == c:
                    st.pop()
            else:
                st.append(c)

        return "".join(st)


