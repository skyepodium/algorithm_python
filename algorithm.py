t = int(input())

for _ in range(t):
    # 0. input
    a, b = map(int, input().split())
    base = a % 10
    last_num = a % 10
    res = 0

    # 1. exception
    if last_num == 1:
        print(1)
        continue

    # 2. init
    s = set()
    cycle = []
    while last_num not in s:
        s.add(last_num)
        cycle.append(last_num)
        last_num = (last_num * base) % 10

    # 3. find
    cycle_len = len(cycle)
    last_idx = b % cycle_len
    res = cycle[last_idx - 1]

    print(res if res != 0 else 10)
