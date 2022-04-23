class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # 1. init
        vowel = ['a', 'e', 'i', 'o', 'u']
        v = set(vowel)
        s = sentence.split(" ")
        n = len(s)

        # 2. loop
        for i in range(n):
            cur = s[i]
            if cur[0].lower() in v:
                s[i] += "ma"
            else:
                s[i] = s[i][1:] + s[i][0] + "ma"
            s[i] += "a" * (i+1)

        return " ".join(s)


sl = Solution()
sentence = "I speak Goat Latin"
# sentence = "The quick brown fox jumped over the lazy dog"
res = sl.toGoatLatin(sentence)

print('res', res)