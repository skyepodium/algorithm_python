class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 0. init
        size = len(numbers)

        # 1. binary_search
        def binary_search(l, r, remain):
            while l <= r:
                mid = l + (r - l) // 2

                if numbers[mid] > remain:
                    r = mid - 1
                elif numbers[mid] < remain:
                    l = mid + 1
                else:
                    return mid
            return -1

        # 2. loop
        for i in range(size - 1):
            l = i + 1
            r = size - 1

            res = binary_search(l, r, target - numbers[i])
            if res != -1:
                return [i + 1, res + 1]
