import re


def main(amountText):
    if not re.fullmatch("\d{1,3}(,\d{3})+|[1-9]{1}\d*|0", amountText):
        return False

    return True

s_list = ["Hello", "-123", "10,000원", "0123", "0", "1", ",123", "1,123", "1234"]

for s in s_list:
    if main(s):
        print("correct", s)
    else:
        print("error", s)
