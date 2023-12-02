from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # 1. init
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

        # 2. sort
        sorted_score = sorted(score, reverse=True)

        # 3. rank
        rank = {}
        for i, s in enumerate(sorted_score):
            if i < 3:
                rank[s] = medals[i]
            else:
                rank[s] = str(i + 1)

        # 4. return
        return [rank[s] for s in score]


sl = Solution()

score = [5, 4, 3, 2, 1]
score = [10, 3, 8, 9, 4]

res = sl.findRelativeRanks(score)

print('res', res)
