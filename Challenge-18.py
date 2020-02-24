# Challenge - 18
# http://www.pythonchallenge.com/pc/return/balloons.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image as Im, ImageChops as Imc
import gzip  # 解压gz包
import binascii
import difflib

# url = "http://www.pythonchallenge.com/pc/return/balloons.html"
url = "http://www.pythonchallenge.com/pc/return/brightness.html"
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

filePath = "e:\WorkSpace\\PythonChallenge\\"
# fileName = "deltas.gz"
fileName = "delta.txt"
str1, str2 = [], []
with open(filePath + fileName) as deltas:
    for line in deltas:
        str1.append(line[:53] + "\n")
        str2.append(line[56:])
dif = difflib.Differ().compare(str1, str2)

with open(filePath + "tmp\\f.png", "wb") as f, open(filePath + "tmp\\f1.png", "wb") as f1, open(filePath + "tmp\\f2.png", "wb") as f2:
    for line in dif:
        bs = bytes([int(i, 16) for i in line[2:].strip().split(" ") if i])
        # print(bs)
        if line[0] == "+":
            f1.write(bs)
        elif line[0] == "-":
            f2.write(bs)
        else:
            f.write(bs)

'''
f:  ../hex/bin.html
f1: butter
f2: fly

http://www.pythonchallenge.com/pc/hex/bin.html
'''