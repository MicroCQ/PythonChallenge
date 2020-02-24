# Challenge - 17
# http://www.pythonchallenge.com/pc/return/romance.html

# -*- coding: utf-8 -*

from urllib import request, error, parse
from http import cookiejar
import re
import bz2
import xmlrpc.client as xc

# url = "http://www.pythonchallenge.com/pc/return/romance.html"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
un = "huge"
pw = "file"

try:
    cj = cookiejar.CookieJar()
    # pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    # pwMgr.add_password(None, url, un, pw)
    # handler = request.HTTPBasicAuthHandler(pwMgr)
    # opener = request.build_opener(request.HTTPCookieProcessor(cj), handler)
    opener = request.build_opener(request.HTTPCookieProcessor(cj), request.HTTPHandler)
    req = opener.open(url).read().decode()
    # print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

for cookie in cj:
    print(cookie)

pat = re.compile("and the next busynothing is (\d+)")
url_template = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={0}'
next_num = '12345'
cookies = []
while next_num:
    html = opener.open(url_template.format(next_num), timeout=10).read().decode()
    for cookie in cj:
        cookies.append(cookie)
    matchRes = pat.findall(html)
    if matchRes:
        next_num = matchRes[0]
        print(next_num)
    else:
        break

values = [x.value for x in cookies]
# msg = url.unquote_plus("".join(values))
msg = parse.unquote_to_bytes(("".join(values)).replace('+', '%20'))
print(msg)
print(bz2.decompress(msg).decode("utf-8"))

msg = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
info = parse.unquote_to_bytes(msg.replace('+', '%20'))
print(bz2.decompress(info).decode('utf-8'))#ascii

# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

proxy = xc.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
try:
    print(proxy.phone("Leopold"))  # 莫扎特的父亲Leopold Mozart
except error as e:
    print(e.code, e.reason)

# 555-VIOLIN
# http://www.pythonchallenge.com/pc/return/violin.html
# http://www.pythonchallenge.com/pc/stuff/violin.php

url1 = "http://www.pythonchallenge.com/pc/stuff/violin.php"
headers = {'Cookie': 'info=the flowers are on their way'}
# req1 = request.Request(url1, headers=headers)
# print(request.urlopen(req1).read().decode())
opener1 = request.build_opener()
opener1.addheaders.append(('Cookie', "info=the flowers are on their way"))
req1 = opener1.open(url1).read().decode()
print(req1)

# oh well, don't you dare to forget the balloons.
# http://www.pythonchallenge.com/pc/return/balloons.html