from urllib import parse
import requests

def parse_cmd(cmd):
    return parse.quote(cmd, encoding='utf-8')

def request(cmd):
    return requests.get(f"http://localhost:8080/run.php?cmd={parse.quote(cmd, encoding='utf-8')}")

if __name__ == '__main__':
    while True:
        r = request(input())
        print('r', r.text, '\n')
