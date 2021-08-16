import re


def main(amountText):
    # 1. 숫자 콤마만 있는지 확인
    # match를 쓰면 안된다. match는 문자열의 시작부터 패턴이 일치하는지 찾는다.
    # 25,000,123원은 앞에서 숫자를 이미 만족했기 때문에 '원'은 매칭되지 않는다고 나온다.
    if re.search("[^0-9,]", amountText):
        print("error: contain non digit or non comma", s)
        return False

    # 2. 0으로 시작 검사
    # .은 글자 1개를 대체합니다.
    if re.fullmatch("0.+", amountText):
        print("error: start with 0", s)
        return False

    # 3, 3자리씩 콤마가 있거나 없는지 확인합니다.
    if not re.fullmatch("\d{1,3}(,?\d{3})+", amountText):
        print("error: wrong comma", s)
        return False

    return True

s_list = ["Hello", "-123", "10,000원", "0123", "0", "1", ",123", "1,123", "1234"]

for s in s_list:
    if main(s):
        print("correct", s)
