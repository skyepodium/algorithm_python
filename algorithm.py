class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # 1. sort
        nums.sort()
        n = len(nums)

        # 2. lower_bound
        def lower_bound(t):
            s, e = 0, n
            while s < e:
                mid = s + (e - s) // 2
                if nums[mid] < t:
                    s = mid + 1
                else:
                    e = mid
            return e

        # 3. upper_bound
        def upper_bound(t):
            s, e = 0, n
            while s < e:
                mid = s + (e - s) // 2
                if nums[mid] <= t:
                    s = mid + 1
                else:
                    e = mid
            return e

        l, r = lower_bound(target), upper_bound(target) - 1

        return [l, r] if l != r else [l]