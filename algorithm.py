class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 1. init
        idx = word.find(ch)

        return word[:idx+1][::-1] + word[idx+1:] if idx > -1 else word
