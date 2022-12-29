class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1. init
        c = Counter(nums)

        # 2. loop
        for num, cnt in c.items():
            if cnt == 1:
                return num

        return -1