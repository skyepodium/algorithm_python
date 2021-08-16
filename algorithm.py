import re

def main(s):
    return re.fullmatch("01\d-\d{3,4}-\d{4}|01\d\d{3,4}\d{4}", s)

s_list = [
    "010-1234-5678",
    "01012345678",
    "017-1234-5678",
    "01712345678",
    "010-123-5678",
    "0101235678",
    "안녕하세요",
    "123",
    "abcde",
    "010-1235678",
    "0101234-5678",
    "011322345"
]

for s in s_list:
    res = "correct" if main(s) else "error"
    print(res, s)