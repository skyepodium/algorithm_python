class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        return re.fullmatch(re.sub("\\.", "[a-z]", p), s) is not None
