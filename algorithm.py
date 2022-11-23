from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(start_idx, size):
            for i in range(start_idx + 1, start_idx + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            if first >> 3 == 0b11110 and check(start, 3):
                start += 4
            elif first >> 4 == 0b1110 and check(start, 2):
                start += 3
            elif first >> 5 == 0b110 and check(start, 1):
                start += 2
            elif first >> 7 == 0:
                start += 1
            else:
                return False
        return True
