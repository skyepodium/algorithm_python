from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image


image = [[1,1,0],[1,0,1],[0,0,0]]

res = Solution().flipAndInvertImage(image)
print('res', res)


