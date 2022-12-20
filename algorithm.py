from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 1. init
        n = len(rooms)
        v = [[] for _ in range(n+1)]
        check = [False] * (n+1)

        # 2. build graph
        for room, keys in enumerate(rooms):
            for key in keys:
                v[room].append(key)

        # 3. dfs
        def dfs(node):
            check[node] = True
            for n_node in v[node]:
                if not check[n_node]:
                    dfs(n_node)

        dfs(0)

        return sum(check) == n

rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
sl = Solution()
res = sl.canVisitAllRooms(rooms)

print('res', res)