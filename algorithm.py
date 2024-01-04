class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        cur = board[x][y]
                        if cur == '.': continue
                        if cur in s:
                            return False
                        else:
                            s.add(cur)

        for b in board:
            t = [num for num in b if num != '.']
            s = set()
            for num in t:
                if num in s:
                    return False
                else:
                    s.add(num)

        for j in range(0, 9):
            s = set()
            for i in range(0, 9):
                num = board[i][j]
                if num == '.': continue
                if num in s:
                    return False
                else:
                    s.add(num)

        return True
