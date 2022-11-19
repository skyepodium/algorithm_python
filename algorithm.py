from typing import List
from collections import deque, defaultdict

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 1. init
        deadends = set(deadends)
        check = defaultdict(int)

        # 2. bfs
        def bfs(start_node):
            q = deque()
            q.append(start_node)

            while q:
                node = q.popleft()

                if node in deadends:
                    continue

                for idx, bit in enumerate(node):
                    upbit = str((int(bit) + 1) % 10)
                    if upbit == "10":
                        upbit = "0"
                    downbit = str((int(bit) - 1) % 10)
                    if downbit == "0":
                        downbit = "9"
                    up_node = node[:idx] + upbit + node[idx + 1:]
                    down_node = node[:idx] + downbit + node[idx + 1:]

                    next_nodes = [up_node, down_node]
                    for next_node in next_nodes:
                        if next_node in deadends:
                            continue
                        if next_node in check:
                            continue

                        check[next_node] = check[node] + 1
                        q.append(next_node)

        bfs("0000")

        return check[target] if target in check else -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

deadends = ["8888"]
target = "0009"

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"

s = Solution()
res = s.openLock(deadends, target)
print('res', res)