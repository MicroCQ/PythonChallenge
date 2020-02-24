# Challenge - 10
# http://www.pythonchallenge.com/pc/return/bull.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
import re

url = "http://www.pythonchallenge.com/pc/return/bull.html"
un = "huge"
pw = "file"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    print("req = ", req)
except error.HTTPError as e:
    print(e.code, e.reason)

url2 = "http://www.pythonchallenge.com/pc/return/sequence.txt"
try:
    pwMgr2 = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr2.add_password(None, url2, un, pw)
    handler2 = request.HTTPBasicAuthHandler(pwMgr2)
    opener2 = request.build_opener(handler2)
    req2 = opener2.open(url2).read().decode()
    print("req2 = ", req2)
except error.HTTPError as e:
    print(e.code, e.reason)

a = re.findall(r"\d+", req2)
print(a)

for i in range(5, 31):
    nextStr = ''
    count = 1
    j = 1
    #print(len(a[i-1]))
    while j <= len(a[i-1]):
        tmpStr = a[i-1]
        if j == len(a[i-1]):
            nextStr = nextStr + str(count) + tmpStr[j-count]
        elif tmpStr[j] == tmpStr[j-1]:
            count += 1
        else:
            nextStr = nextStr + str(count) + tmpStr[j-count]
            count = 1
        j += 1
    a.append(nextStr)
    print("a[%d] = %s" % (i, a[i]), len(a[i]))

print("len(a[%d]) = %d" % (i, len(a[i])))

'''    
len(a[30]) = ?
a = [1, 11, 21, 1211, 111221, 
'''
