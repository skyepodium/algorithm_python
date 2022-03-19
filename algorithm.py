from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. init
        d = defaultdict(list)

        # 2. loop
        for idx, s in enumerate(strs):
            d["".join(sorted(s))].append(s)

        return d.values()

sl = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res = sl.groupAnagrams(strs)

print('res', res)