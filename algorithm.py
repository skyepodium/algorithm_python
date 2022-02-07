from collections import defaultdict

def solution(genres, plays):
    # 1. init
    res = []
    c = defaultdict(int)
    i = defaultdict(list)

    # 2. genre total
    for idx, (g, p) in enumerate(zip(genres, plays)):
        c[g] += p
        i[g].append((idx, p))

    # 3. count
    for g, _ in sorted(c.items(), key=lambda x: -x[1]):
        song_list = i[g]
        song_list.sort(key=lambda x: (-x[1], x[0]))
        res.append(song_list[0][0])
        if len(song_list) >= 2: res.append(song_list[1][0])

    return res



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

res = solution(genres, plays)

print('res', res)