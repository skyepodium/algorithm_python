class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. init
        n = len(cost)
        cost += [0]
        d = [int(1e7)] * (n+1)

        # 2. bottom up
        d[0], d[1] = cost[0], cost[1]
        for i in range(0, n):
            if i + 1 <= n:
                d[i+1] = min(d[i+1], d[i] + cost[i+1])
            if i + 2 <= n:
                d[i+2] = min(d[i+2], d[i] + cost[i+2])
                
        return d[n]
