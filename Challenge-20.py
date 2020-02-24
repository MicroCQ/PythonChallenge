# Challenge - 20
# http://www.pythonchallenge.com/pc/hex/idiot2.html

# -*- coding: utf-8 -*

from urllib import request, error
import re, zipfile

# url = "http://www.pythonchallenge.com/pc/hex/idiot2.html"
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
un = "butter"
pw = "fly"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url)
    # print(req.read())
    # print(req.info())
    # print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

# private property beyond this fence
# but inspecting it carefully is allowed

# Content-Range: bytes 0-30202/2123456789

'''
totalSize = 2123456789
start = 30203  # 0
pa = re.compile(r"-(\d+)")
while True:
    opener.addheaders = [("Range", "bytes={0}-".format(start))]
    req = opener.open(url)
    print(req.read())
    start = int(pa.search(req.info()["Content-Range"]).group(1))+1
    if start > totalSize:
        break
    else:
        print(start)
'''
'''
header = {"Authorization": "Basic YnV0dGVyOmZseQ=="}
header["Range"] = "bytes={0}-".format(start)
req = request.Request(url, headers=header)
ans = request.urlopen(req)
print(ans.read())
'''
# invader

'''
start =1176543212 # 2123456789
pa = re.compile(r"(\d+)")
while True:
    opener.addheaders = [("Range", "bytes={0}-".format(start))]
    req = opener.open(url)
    print(req.read())
    start = int(pa.search(req.info()["Content-Range"]).group(1))-1
    if start < 30347:
        break
    else:
        print(start)

'''
# b'esrever ni emankcin wen ruoy si drowssap eht\n'
# 2123456743
# b'and it is hiding at 1152983631.\n'
# 2123456711


# strTmp = "esrever ni emankcin wen ruoy si drowssap eht" #  the password is your new nickname in reverse
# strTmp = "1152983631" #  1363892511
# strTmp = "2123456711" #  1176543212
# print(strTmp[::-1])

start = 1152983631  # 0
pa = re.compile(r"-(\d+)")
opener.addheaders = [("Range", "bytes={0}-".format(start))]
req = opener.open(url).read()
with open("ans-20.zip", "wb") as f:
    f.write(req)
# ans-20.zip, pwd="redavni" # invader

'''
Readme.txt 

Yes! This is really level 21 in here. 
And yes, After you solve it, you'll be in level 22!

Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.
'''