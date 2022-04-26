from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 1. init
        n = len(points)
        e = []
        d = [i for i in range(n)]
        res = 0

        # 2. cal_dist
        def cal_dist(first, second):
            x, y = first
            a, b = second
            return abs(x-a) + abs(y-b)

        # 3. make graph
        for i in range(n):
            for j in range(i+1, n):
                e.append((i, j, cal_dist(points[i], points[j])))

        # 4. sort
        e.sort(key=lambda x: x[2])

        # 5. find
        def find(node):
            if node == d[node]:
                return node
            else:
                d[node] = find(d[node])
                return d[node]

        # 6. cal cost
        for a, b, cost in e:
            a, b = find(a), find(b)
            if a != b:
                d[a] = b
                res += cost

        return res

sl = Solution()

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points = [[3,12],[-2,5],[-4,1]]
res = sl.minCostConnectPoints(points)

print('res', res)