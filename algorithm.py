from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 1. init
        n = len(coordinates)

        # 2. ccw
        def ccw(r, p, q):
            first = (p[0] - r[0]) * (q[1] - r[1])
            second = (p[1] - r[1]) * (q[0] - r[0])
            result = first - second

            if result > 0:
                return 1
            elif result == 0:
                return 0
            else:
                return -1

        # 3. loop
        for i in range(n-2):
            if ccw(coordinates[i], coordinates[i+1], coordinates[i+2]) != 0:
                return False

        return True


sl = Solution()

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
res = sl.checkStraightLine(coordinates)

print('res', res)