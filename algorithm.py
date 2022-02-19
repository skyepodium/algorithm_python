class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return sum([x * (x - 1) // 2 for x in Counter([tuple(sorted(do)) for do in dominoes]).values()])
