from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        return "".join([x[0] for x in sorted([x for x in zip(s, indices)], key=lambda x: x[1])])


sl = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
res = sl.restoreString(s, indices)

print('res', res)