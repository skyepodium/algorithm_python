import re

class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        s = re.sub("[^0-9 ]", "", s).strip()
        s_list = [int(x) for x in re.split(" +", s)]

        prev = -1
        for c in s_list:
            if not prev < c: return False
            prev = c

        return True


sl = Solution()
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
s = "hello world 5 x 5"
res = sl.areNumbersAscending(s)

print('res', res)

