from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 1. init
        d = {}

        # 2. sort
        items1.sort()
        items2.sort()

        # 3. loop
        for key, value in items1:
            d[key] = value

        for key, value in items2:
            if key in d:
                d[key] += value
            else:
                d[key] = value

        return [[key, value] for key, value in sorted(d.items())]


items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]

items1 = [[1,1],[3,2],[2,3]]
items2 = [[2,1],[3,2],[1,3]]

items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]

sl = Solution()

res = sl.mergeSimilarItems(items1, items2)

print('res', res)