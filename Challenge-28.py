# Challenge - 28
# http://www.pythonchallenge.com/pc/ring/bell.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image as Im
import bz2, keyword as kw

url = "http://www.pythonchallenge.com/pc/ring/bell.html"
un = "repeat"
pw = "switch"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    #print(req)
except error.HTTPError as e:
    print(e.code, e.reason)


filePath = "e:\WorkSpace\\PythonChallenge\\"
picName = "bell.png"  # mode RGB size (640, 480)
picFile = filePath + picName
pic = Im.open(picFile)
# pic.show()
(width, height) = pic.size

data = pic.getdata()
d = [i[1] for i in data]
s = []
for i in range(0, len(d), 2):
    if abs(d[i] - d[i+1]) != 42:
        s.append(abs(d[i] - d[i+1]))
print(bytes(s).decode())  # whodunnit().split()[0] ?

# whodunnit --> who has do it
# python 荷兰人guido van rossum



'''with open("tmp.txt", "w") as f:
    for y in range(height):
        for x in range(width):
            t = "-".join(str(p[(x, y)][1]))
            f.write(t)
        f.write("\n")

'''