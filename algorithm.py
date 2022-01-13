class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 1. init
        even_list = [x for x in nums if x % 2 == 0]
        odd_list = [x for x in nums if x % 2 == 1]
        res = []

        # 2. loop
        for a, b in zip(even_list, odd_list):
            res.append(a)
            res.append(b)

        return res


