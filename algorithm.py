from collections import defaultdict, deque

def solution(begin, target, words):
    # 1. init
    d = defaultdict(list)
    check = defaultdict(int)
    words.append(begin)

    # 2. get_diff
    def get_diff(a, b):
        res = 0
        for q, w in zip(a, b):
            if q != w: res += 1
        return res

    # 3. loop
    for i, a in enumerate(words):
        for j, b in enumerate(words):
            if i == j: continue
            if get_diff(a, b) == 1:
                d[a].append(b)
                d[b].append(a)

    # 4. bfs
    def bfs(start):
        q = deque()
        q.append(start)
        check[start] = 0

        while q:
            node = q.popleft()
            for n_node in d[node]:
                if n_node not in check:
                    check[n_node] = check[node] + 1
                    q.append(n_node)

    bfs(begin)

    return check[target]

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]

res = solution(begin, target, words)

print('res', res)