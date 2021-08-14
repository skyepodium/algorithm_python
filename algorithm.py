import collections


def solution(places):
    max_int = 5
    answer = [1 for _ in range(max_int)]
    check = []
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    for idx in range(max_int):
        place = places[idx]

        start_node = []
        for i in range(max_int):
            for j in range(max_int):
                if place[i][j] == "P":
                    start_node.append((i, j))

        def bfs(x, y):
            check[x][y] = 0
            q = collections.deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()

                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= max_int or ny < 0 or ny >= max_int:
                        continue

                    if check[nx][ny] != -1 or place[nx][ny] == "X":
                        continue

                    if place[nx][ny] == 'O':
                        check[nx][ny] = check[x][y] + 1
                        q.append((nx, ny))
                    elif place[nx][ny] == 'P' and check[x][y] + 1 <= 2:
                        return 0

            return 1

        for x, y in start_node:
            check = [[-1 for _ in range(max_int)] for _ in range(max_int)]
            if bfs(x, y) == 0:
                answer[idx] = 0
                break

    return answer


p = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

res = solution(p)

print(res)