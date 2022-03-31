class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set([int(x) for x in re.split("[a-z]", word) if x != '']))
