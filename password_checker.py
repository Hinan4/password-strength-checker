import hashlib
import requests
from zxcvbn import zxcvbn

def check_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    return score, feedback

def check_breach(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"API error: {res.status_code}")

    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0
