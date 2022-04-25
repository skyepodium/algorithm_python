from collections import defaultdict


def solution(fees, records):
    # 1. init
    base_minute, base_fee, per_minute, per_fee = fees
    p = defaultdict(list)
    remain = defaultdict(int)
    res = defaultdict(int)

    # 2. cal_diff
    def cal_diff(before, cur):
        before_hour, before_minute = before
        cur_hour, cur_minute = cur
        hour_diff = cur_hour - before_hour
        minute_diff = cur_minute - before_minute

        if minute_diff < 0:
            hour_diff -= 1
            minute_diff += 60

        return hour_diff * 60 + minute_diff

    # 3. cal_fee
    def cal_fee(diff):
        res = base_fee

        if diff > base_minute:
            m_diff = diff - base_minute
            a = m_diff // per_minute
            if m_diff % per_minute != 0: a += 1
            res += a * per_fee

        return res

    # 4. loop
    for r in records:
        t, num, cmd = r.split(" ")
        cur_time = [int(x) for x in t.split(":")]
        if cmd == "IN":
            p[num] = cur_time
        else:
            remain[num] += cal_diff(p[num], cur_time)
            p.pop(num, None)

    # 5. sum time
    for r in p.items():
        num, t = r
        remain[num] += cal_diff(t, [23, 59])

    # 6. total fee
    for num, val in remain.items():
        res[num] = cal_fee(val)

    return [fee for num, fee in sorted(res.items(), key=lambda x: (x[0], [1]))]


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# records = ["05:34 5961 IN", "07:59 5961 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

res = solution(fees, records)

print('res', res)