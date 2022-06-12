from urllib import parse
import requests

def parse_cmd(cmd):
    return parse.quote(cmd, encoding="utf-8")

def request(cmd):
    base_url = "http://localhost:8080/run.php?cmd="
    r = requests.get(f"{base_url}{parse_cmd(cmd)}")
    print('r', r.text)

while True:
    print(request(input()))
    print()

