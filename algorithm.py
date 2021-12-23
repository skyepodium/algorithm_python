class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        return "".join([x[0] for x in sorted([x for x in zip(s, indices)], key=lambda x: x[1])])
