from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # 1. init
        max_val = max(nums)
        res = -1

        # 2. cal cnt
        def cal_cnt(mid):
            return sum([1 for x in nums if x >= mid])

        # 3. sort
        nums.sort()

        # 4. binary search
        s, e = 0, max_val
        while s <= e:
            mid = s + (e - s) // 2
            cnt = cal_cnt(mid)
            if cnt > mid:
                s = mid + 1
            elif cnt == mid:
                return mid
            else:
                e = mid - 1

        return res

sl = Solution()

nums = [3,5]
# nums = [0,0]
# nums = [0,4,3,0,4]

res = sl.specialArray(nums)

print('res', res)
