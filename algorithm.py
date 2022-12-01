class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def count_vowel(s: str) -> int:
            vowel_set = set(list('aeiou'))
            cnt = 0

            for c in s.lower():
                if c in vowel_set:
                    cnt += 1

            return cnt

        return count_vowel(s[:len(s) // 2]) == count_vowel(s[len(s) // 2:])