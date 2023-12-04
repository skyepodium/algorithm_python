url = "shopping.naver.com/luxury/home"


def encode_url(url: str) -> str:
    res = ""

    for c in url:
        if c in ["/", ":"]:
            res += c
        else:
            res += f"%{hex(ord(c))[2:]}"

    return res


res = "https://" + encode_url(url)
print(res)
