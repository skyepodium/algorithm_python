class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # 1. init
        i, j = 0, len(s) - 1
        l = list(s)

        # 2. loop
        while i < j:
            if not l[i].isalpha():
                i += 1
            elif not l[j].isalpha():
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

        # 3. return
        return ''.join(l)


sl = Solution()
s = "ab-cd"
s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
print(sl.reverseOnlyLetters(s))
