import re


def main(money):
    return re.fullmatch("\d{1,3}(,\d{3})+|\d|[1-9]{1}\d*", money)

s_list = ["Hello", "-123", "10,000원", "0123", "0", "1", ",123", "1,123", "1234"]

for s in s_list:
    res = "correct" if main(s) else "error"
    print(res, s)