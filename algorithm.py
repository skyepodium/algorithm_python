from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 0. sort
        nums.sort()

        # 1. init
        n = len(nums)
        res = []
        st = set()

        for i in range(n - 3):
            for j in range(i+1, n-2):

                l = j + 1
                r = n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        cur = [nums[i], nums[j], nums[l], nums[r]]
                        key = "".join([str(x) for x in cur])
                        if key not in st:
                            res.append(cur)
                            st.add(key)
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1

                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return res

nums = [1,0,-1,0,-2,2]
target = 0

nums = [2,2,2,2,2]
target = 8

sl = Solution()
print(sl.fourSum(nums, target))