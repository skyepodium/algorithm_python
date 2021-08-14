def solution(s):
    res = ""
    s = s.lower()
    is_new = True
    for c in s:
        val = c
        if c == " ":
            is_new = True
        else:
            if is_new:
                val = c.upper()
            is_new = False
        res += val
    return res

s = "3people unFollowed me"

res = solution(s)

print(res)