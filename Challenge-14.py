# Challenge - 14
# http://www.pythonchallenge.com/pc/return/italy.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
from PIL import Image as Im

url = "http://www.pythonchallenge.com/pc/return/italy.html"
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
picName = "wire.png"
picFile = filePath + picName
origin = Im.open(picFile)
# origin.show()

width, height = origin.size
newPic = Im.new(origin.mode, (100, 100))
y, i, count = 0, 0, 0
while i < width:
    for x in range(0+count, 100-count):
        newPic.putpixel((x, y), origin.getpixel((i, 0)))
        i += 1
    for y in range(0+count, 99-count):
        newPic.putpixel((x, y), origin.getpixel((i, 0)))
        i += 1
    for x in range(99-count, 0+count, -1):
        newPic.putpixel((x, y), origin.getpixel((i, 0)))
        i += 1
    for y in range(98-count, 0+count, -1):
        newPic.putpixel((x, y), origin.getpixel((i, 0)))
        i += 1
    count += 1
newPic.show()

# http://www.pythonchallenge.com/pc/return/cat.html
# http://www.pythonchallenge.com/pc/return/uzi.html