import requests
import hashlib
from bs4 import BeautifulSoup


url = "http://167.99.88.216:30669/"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    hash: ''
}

r = requests.session()
out = r.get(url)
parsed_html = BeautifulSoup(out.text, "lxml")
given_text = parsed_html.body.find('h3', attrs={'align': 'center'}).text.encode()
print('given_text', given_text)

enc = hashlib.md5()
enc.update(given_text)
result = enc.hexdigest()
print("result", result)
data["hash"] = result
res = r.post(url, headers=headers, data=data)
print(res.text)
