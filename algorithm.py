from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. init
        max_int = amount + 1
        d = [max_int for _ in range(max_int)]
        d[0] = 0

        # 2. bottom up
        for i in range(0, max_int):
            for c in coins:
                if i-c >= 0:
                    d[i] = min(d[i], d[i-c] + 1)

        return d[amount] if d[amount] <= amount else -1

sl = Solution()
coins = [1,2,5]
amount = 11

coins = [2]
amount = 3

coins = [1]
amount = 0

# coins = [186,419,83,408]
# amount = 6249
res = sl.coinChange(coins, amount)

print('res', res)


