class Solution:
    def sortSentence(self, s: str) -> str:

        return " ".join([x[:len(x)-1] for x in sorted(s.split(" "), key=lambda x: int(x[-1]))])