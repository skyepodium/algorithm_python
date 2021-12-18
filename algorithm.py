class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # 1. init
        result = []

        # 2. check
        def check(num):
            str_num = str(num)

            if '0' in str_num:
                return False

            for a in str_num:
                if num % int(a) != 0:
                    return False

            return True

        # 3. loop
        for i in range(left, right + 1):
            if check(i):
                result.append(i)

        return result