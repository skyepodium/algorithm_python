class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word[0:1].upper() + word[1:].lower() == word