from collections import defaultdict
import re
import itertools

def solution(info, query):
    # 1. init
    info_dict = defaultdict()
    res = []

    # 2. set info
    def set_info(info):
        for x in info:
            l, p, c, f, s = x.split(" ")

            l_list = [l, '-']
            p_list = [p, '-']
            c_list = [c, '-']
            f_list = [f, '-']
            s_list = [int(s)]
            lpcf = list(itertools.product(l_list,p_list,c_list,f_list,s_list))

            for q, w, e, r, t in lpcf:
                key = f"{q}{w}{e}{r}"
                if key in info_dict:
                    info_dict[key].append(t)
                else:
                    info_dict[key] = [t]

    set_info(info)

    # 3. sort
    for val in info_dict.values():
        val.sort()

    # 4. lower bound
    def lower_bound(key, score):
        s_list = info_dict[key]
        l = 0
        r = len(s_list)

        while l < r:
            mid = l + (r - l) // 2

            if s_list[mid] < score:
                l = mid + 1
            else:
                r = mid

        return r

    # 5 query
    for q in query:
        l, p, c, f, s = re.compile(" and | ").split(q)
        key = f"{l}{p}{c}{f}"
        score = int(s)

        cnt = 0
        if key in info_dict:
            idx = lower_bound(key, score)
            cnt = len(info_dict[key]) - idx
        res.append(cnt)

    return res