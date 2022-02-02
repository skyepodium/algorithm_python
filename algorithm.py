class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. init
        diff = 2147483647
        n = len(arr)
        res = []

        # 2. sort
        arr.sort()

        # 3. loop
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                diff = min(diff, arr[i + 1] - arr[i])

        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                if diff == arr[i + 1] - arr[i]:
                    res.append((arr[i], arr[i + 1]))

        return res
