# Challenge - 23
# http://www.pythonchallenge.com/pc/hex/bonus.html

# -*- coding: utf-8 -*

from urllib import request, error
import this

url = "http://www.pythonchallenge.com/pc/hex/bonus.html"
un = "butter"
pw = "fly"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    # print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

'''
'va gur snpr bs jung?'
'''
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "nopqrstuvwxyzabcdefghijklm"

transTab = str.maketrans(str1, str2)
inStr = "va gur snpr bs jung?"
print(inStr.translate(transTab))
# in the face of what?

# In the face of ambiguity