# Challenge - 13
# http://www.pythonchallenge.com/pc/return/disproportional.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
import re
import xmlrpc.client as xc

url = "http://www.pythonchallenge.com/pc/return/disproportional.html"
un = "huge"
pw = "file"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

# http://www.pythonchallenge.com/pc/phonebook.php
proxy = xc.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
try:
    print(proxy.phone("Bert"))  # Bert is evil! go back!
except error as e:
    print(e.code, e.reason)

# 555-ITALY