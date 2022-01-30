class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # 1. init
        numList = list(set(arr))

        def lower_bound(arr, target):
            l, r = 0, len(arr)

            while l < r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid

            return r + 1

        def upper_bound(arr, target):
            l, r = 0, len(arr)

            while l < r:
                mid = (l + r) // 2
                if arr[mid] <= target:
                    l = mid + 1
                else:
                    r = mid

            return r + 1

        for num in numList:
            diff = upper_bound(arr, num) - lower_bound(arr, num)
            if diff > (len(arr) / 4):
                return num

        return -1