class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        answer = -1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, nums[mid], target)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                answer = mid
                r = mid - 1

        return answer if answer != -1 else len(nums)
