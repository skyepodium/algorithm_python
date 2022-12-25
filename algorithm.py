from collections import Counter, defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 1. init
        c = Counter(s)
        n = len(s)

        if k == 0:
            return 0

        # 2. exception
        if len(c) < 3:
            return -1

        for cnt in c.values():
            if cnt < k:
                return -1

        # 3. two pointer
        l, r = n // 2 - 1, n // 2
        l_start_index = -1

        for r in range(n//2, n):
            left, right = s[l], s[r]

            if c[right] > k:
                c[right] -= 1
            else:
                l_start_index = l
                break

            if c[left] > k:
                c[left] -= 1
                l -= 1

        for l_idx in range(l_start_index, -1, -1):
            left = s[l_idx]
            if c[left] > k:
                c[left] -= 1
                l -= 1
            else:
                break

        res = l + 1 + n - r

        # 3. two pointer
        l, r = n // 2 - 1, n // 2
        l_start_index = -1
        for r in range(n//2, n):
            left, right = s[l], s[r]

            if c[right] > k:
                c[right] -= 1
            else:
                l_start_index = l
                break

            if c[left] > k:
                c[left] -= 1
                l -= 1

        for l_idx in range(l_start_index, -1, -1):
            left = s[l_idx]
            if c[left] > k:
                c[left] -= 1
                l -= 1
            else:
                break

        res = min(res, l + 1 + n - r)

        d = defaultdict(int)
        for i, c in enumerate(s):
            d[c] += 1
            if d['a'] >= k and d['b'] >= k and d['c'] >= k:
                res = min(res, i + 1)
                break

        d = defaultdict(int)
        for i, c in enumerate(reversed(s)):
            d[c] += 1
            if d['a'] >= k and d['b'] >= k and d['c'] >= k:
                res = min(res, i + 1)
                break

        return res

sl = Solution()

s = "aabaaaacaabc"
k = 2

# # s = "a"
# # k = 1
#
# s = "a"
# k = 0
#
s = "abca"
k = 1

s = "caaababcaa"
k = 2

res = sl.takeCharacters(s, k)

print('res', res)