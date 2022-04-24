import re

def solution(m, musicinfos):
    # 1. init
    res = "(None)"
    t = -1
    tk_list = ['C', 'D', 'F', 'G', 'A']

    def rep(s):
        for tk in tk_list:
            s = re.sub(f"{tk}#", tk.lower(), s)
        return s

    m = rep(m)

    # 2. cal diff
    def cal_diff(s, e):
        s_h, s_m = [int(x) for x in s.split(":")]
        e_h, e_m = [int(x) for x in e.split(":")]

        h_diff = e_h - s_h
        if e_m < s_m:
            h_diff -= 1
            e_m += 60
        m_diff = e_m - s_m

        return h_diff * 60 + m_diff

    # 3. loop
    for ms in musicinfos:
        # 1) split
        s, e, name, ml = ms.split(",")
        ml = rep(ml)

        # 2) cal_diff
        diff = cal_diff(s, e)

        # 3) get total
        ml_len = len(ml)
        me = (diff // ml_len) * ml + ml[0:diff % ml_len]

        r = re.search(m, me)

        if r:
            if diff > t:
                t = diff
                res = name

    return res


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
#HELLO

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
#FOO
# # #
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
#WORLD
#
# m = "BF#"
# musicinfos = ["00:53,12:56,HELLO!!!,AEBBF#"]

res = solution(m, musicinfos)
print('res', res)
