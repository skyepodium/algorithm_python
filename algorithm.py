from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1. init
        numList = []
        for idx, num in enumerate(nums):
            numList.append((idx, num))

        # 2. sort
        numList.sort(key=lambda x: (x[1], x[0]))

        # 3. loop
        for i in range(len(numList) - 1):
            f_idx, f_num = numList[i]
            s_idx, s_num = numList[i+1]
            if f_num == s_num and abs(f_idx - s_idx) <= k:
                return True

        return False

sl = Solution()
nums = [1,2,3,1,2,3]
k = 2
res = sl.containsNearbyDuplicate(nums, k)

print('res', res)
