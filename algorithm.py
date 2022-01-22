from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 1. init
        letter = []
        digit = []

        # 2. loop
        for log in logs:
            is_numberic = True
            for i in log.split(" ")[1:]:
                if not i.isnumeric():
                    is_numberic = False
            if is_numberic:
                digit.append(log)
            else:
                letter.append(log)

        # 3. sort
        letter.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))

        return letter + digit

sl = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
res = sl.reorderLogFiles(logs)

print('res', res)
