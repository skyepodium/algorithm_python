from collections import Counter

def solution(input_string):
    res = ""
    base = Counter(input_string)

    for char, cnt in base.items():
        if cnt == 1:
            continue

        first_idx, last_idx = len(input_string) - 1, 0
        for idx, val in enumerate(input_string):
            if val == char:
                first_idx = min(first_idx, idx)
                last_idx = max(last_idx, idx)
        if cnt < last_idx - first_idx + 1:
            res += char

    return "".join(sorted(res)) if len(res) > 0 else "N"

s = "edeaaabbccd"
s = "eeddee"
s = "string"
s = "zbzbz"
res = solution(s)
print('res', res)