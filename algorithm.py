class Solution:
    def reverseVowels(self, s: str) -> str:
        # 1. init
        vowel_list = []
        vowel_set = set(list("aeiouAEIOU"))
        s_list = list(s)

        # 2. make vowel_list
        for idx, val in enumerate(s):
            if val in vowel_set:
                vowel_list.append(idx)

        # 3. loop
        l, r = 0, len(vowel_list) - 1
        while l < r:
            l_idx, r_idx = vowel_list[l], vowel_list[r]
            s_list[l_idx], s_list[r_idx] = s_list[r_idx], s_list[l_idx]
            l += 1
            r -= 1

        return "".join(s_list)

sl = Solution()
s = "hello"
s = "leetcode"
s = "aA"
res = sl.reverseVowels(s)

print('res', res)