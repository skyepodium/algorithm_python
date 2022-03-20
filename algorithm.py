from collections import defaultdict


def solution(id_list, report, k):
    # 1. init
    email = defaultdict(set)
    idx = defaultdict(int)

    # 2. id count
    for id in id_list:
        idx[id] = 0

    # 3. loop
    for r in report:
        start, end = r.split(" ")
        if start not in email[end]:
            email[end].add(start)

    # 4. check
    for reported, s in email.items():
        sender = list(s)
        if (len(sender)) >= k:
            for se in sender:
                idx[se] += 1

    return list(idx.values())
