class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # 1. init
        idx_list = [idx for idx, w in enumerate(s) if w == c]
        n = len(s)
        check = [-1 for _ in range(n)]

        # 2. bfs
        def bfs():
            q = deque(idx_list)
            for idx in idx_list:
                check[idx] = 0

            while q:
                node = q.popleft()

                n_node_list = [node - 1, node + 1]
                for n_node in n_node_list:
                    if n_node < 0 or n_node >= n: continue

                    if check[n_node] != -1: continue
                    check[n_node] = check[node] + 1
                    q.append(n_node)

        bfs()

        return check