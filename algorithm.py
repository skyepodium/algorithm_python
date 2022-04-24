def solution(relation):
    # 1. init
    res = 0
    n = len(relation)
    m = len(relation[0])
    idx_set = set()
    l_list = []

    # 2. go
    def go(idx, l):
        if idx >= m:
            if len(l) > 0:
                l_list.append(l[::])
            return

        l.append(idx)
        go(idx + 1, l)
        l.pop()

        go(idx + 1, l)

    go(0, [])

    # 3. sort
    l_list.sort(key=len)

    # 4. loop
    for l in l_list:
        c_list = [str(x) for x in l]
        c_set = set(c_list)

        is_possible = True
        for idx in idx_set:
            cnt = 0
            for x in list(idx):
                if x in c_set: cnt += 1

            if cnt == len(idx):
                is_possible = False
                break

        if not is_possible: continue

        # 1) make key
        key_list = []
        for c in relation:
            key = "_".join([str(c[a]) for a in l])
            key_list.append(key)

        # 2) uniqueness
        s = set(key_list)
        if len(s) < n: continue

        # 3) minimality
        idx_key = "".join([str(x) for x in l])

        idx_set.add(idx_key)
        res += 1

    return res


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

res = solution(relation)

print('res', res)