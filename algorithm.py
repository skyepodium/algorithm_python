from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 1. init
        visited = set(deadends)
        check = set()

        # 2. move_bit
        def move_bit(node, idx, direction):
            if direction == 1:
                next_bit = (int(node[idx]) + 1) % 10
            else:
                next_bit = (int(node[idx]) - 1) % 10
            if next_bit >= 10:
                next_bit = 0
            elif next_bit < 0:
                next_bit = 9
            return node[:idx] + str(next_bit) + node[idx+1:]


        # 3. bfs
        def bfs(start_node, target_node):
            q1 = set([start_node])
            q2 = set([target_node])
            step = 0

            while q1 and q2:
                if len(q1) > len(q2):
                    q1, q2 = q2, q1

                temp = set()

                for node in q1:
                    if node in deadends:
                        continue

                    if node in q2:
                        return step

                    visited.add(node)

                    for i in range(4):
                        for j in [-1, 1]:
                            next_node = move_bit(node, i, j)
                            if next_node in visited:
                                continue
                            temp.add(next_node)

                q1 = q2
                q2 = temp
                step += 1

            return -1

        return bfs("0000", target)

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

deadends = ["8888"]
target = "0009"

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"

sl = Solution()
print(sl.openLock(deadends, target))