import re


def solution(s):
    s_list = s.split("},{")

    tuple_list = []
    for cur in s_list:
        cur = re.sub("{{|}}", "", cur)

        cur_list = cur.split(",")
        tuple_list.append(cur_list)

    tuple_list.sort(key=lambda x: len(x))

    s = set()
    res = []
    for t in tuple_list:
        for val in t:
            if val not in s:
                res.append(int(val))
                s.add(val)
                break

    return res