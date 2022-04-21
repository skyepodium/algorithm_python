class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # 1. init
        res = 0

        # 2. loop
        for o in operations:
            if o == '++X' or o == 'X++':
                res += 1
            else:
                res -= 1

        return res