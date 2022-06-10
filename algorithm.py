class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. inti
        res = 0
        st = set()

        # 2. two pointer
        l = 0
        for r, c in enumerate(s):
            while c in st:
                st.remove(s[l])
                l += 1
            st.add(c)
            res = max(res, r - l + 1)

        return res


sl = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
res = sl.lengthOfLongestSubstring(s)

print('res', res)