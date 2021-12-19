from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda x, y: x ^ y, [x for x in range(start, start + n * 2, 2)])