from collections import Counter

def solution(X, Y):
    a = sorted((Counter(X) & Counter(Y)).items(), key=lambda x: (-int(x[0]), -int(x[1])))
    res = ""
    for num, count in a:
        res += num * int(count)

    if res == "":
        return "-1"

    if len(res) == res.count("0"):
        return "0"

    return res

x = "100"
y = "2345"

x = "100"
y = "203045"

# x = "5525"
# y = "1255"

res = solution(x, y)

print('res', res)