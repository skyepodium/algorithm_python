class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for num, idx in zip(nums, index):
            res.insert(idx, num)

        return res
