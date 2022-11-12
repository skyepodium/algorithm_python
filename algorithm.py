from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([str(key)*count for key, count in sorted([(key, count) for key, count in Counter(s).items()], key=lambda x: -x[1])])

sl = Solution()
print(sl.frequencySort("tree"))
