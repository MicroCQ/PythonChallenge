# Challenge - 29
# http://www.pythonchallenge.com/pc/ring/guido.html

# -*- coding: utf-8 -*

from urllib import request, error
import bz2

url = "http://www.pythonchallenge.com/pc/ring/guido.html"
un = "repeat"
pw = "switch"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    #print(req)
    blank = req.splitlines()[12:]
    data = bytes([len(b) for b in blank])
    print(bz2.decompress(data).decode())
    # Isn't it clear? I am yankeedoodle!
except error.HTTPError as e:
    print(e.code, e.reason)

