class Solution:
    def countElements(self, nums: List[int]) -> int:
        # 1. init
        c = Counter(nums)
        s = set(nums)
        l = sorted(list(s))[1:len(s) - 1]
        res = 0

        # 2. loop
        for a in l:
            res += c[a]

        return res