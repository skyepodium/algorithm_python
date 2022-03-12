class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # 1. init
        origin = arr[::]
        n = len(arr)
        arr_idx = 0

        # 2. loop
        for cur in origin:
            if arr_idx >= n: break

            arr[arr_idx] = cur
            arr_idx += 1

            if cur == 0 and arr_idx < n:
                arr[arr_idx] = cur
                arr_idx += 1