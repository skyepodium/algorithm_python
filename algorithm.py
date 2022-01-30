class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 1. init
        d = {}
        a = []
        b = []

        # 2. loop
        for idx, num in enumerate(arr2):
            d[num] = idx

        # 3. search
        for num in arr1:
            if num in d:
                a.append(num)
            else:
                b.append(num)

        return sorted(a, key=lambda x: d[x]) + sorted(b)