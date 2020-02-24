# Challenge - 12
# http://www.pythonchallenge.com/pc/return/evil.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
from PIL import Image as im
from io import BytesIO

url = "http://www.pythonchallenge.com/pc/return/evil.html"
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


filePath = "e:\WorkSpace\\PythonChallenge\\evil\\"
picName_1 = "evil1.jpg"
picName_2 = "evil2.jpg"
picName_3 = "evil3.jpg"
picFile = filePath + picName_2
origin = im.open(picFile)
# origin.show()

gfxName = "evil2.gfx"
gfxFile = filePath + gfxName
originFile = open(gfxFile, "rb").read()

pathName = [0]*5
for i in range(5):
    piece = originFile[i::5]
    print(piece)
    pic = im.open(BytesIO(piece))
    # print(pic.format.lower())
    pathName[i] = filePath + str(i) + "." + str(pic.format.lower())
    f = open(pathName[i], "wb")
    f.write(piece)
    f.close()

'''
0.jpeg dis
1.png  pro
2.gif  port
3.png  ional
disproportinnal

view-source:http://www.pythonchallenge.com/pc/return/evil4.jpg
Bert is evil! go back!
'''

