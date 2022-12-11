class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # 1. init
        prev = arr[0]
        is_up = False
        is_down = False

        # 2. loop
        for i, num in enumerate(arr):
            if num == prev and i != 0:
                return False

            if num > prev:
                if is_down:
                    return False
                is_up = True

            if num < prev:
                if not is_up:
                    return False
                is_down = True

            prev = num

        return is_up and is_down