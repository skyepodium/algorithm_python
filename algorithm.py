from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                res += 1

        return res
