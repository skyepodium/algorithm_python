class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1. init
        n = len(s)
        self.res = 0

        # 2. is_palindrome
        def is_palindrome(l, r):
            while 0 <= l <= r < n and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1

        # 3. loop
        for i in range(n):
            is_palindrome(i, i)
            is_palindrome(i, i+1)

        return self.res

sl = Solution()
s = "abc"
s = "aaa"
s = "qwer"
res = sl.countSubstrings(s)

print('res', res)