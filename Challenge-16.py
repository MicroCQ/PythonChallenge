# Challenge - 16
# http://www.pythonchallenge.com/pc/return/mozart.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
from PIL import Image as Im

url = "http://www.pythonchallenge.com/pc/return/mozart.html"
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
picName = "mozart.gif"
picFile = filePath + picName
pic = Im.open(picFile)
# pic.show()

(width, height) = pic.size
# data = list(pic.getdata())
newPic = Im.new(pic.mode, (width, height))

for y in range(height):
    pixels = [pic.getpixel((x, y)) for x in range(width)]
    #  print(pixels)
    x = pixels.index(195)

    newpixels = pixels[x:width] + pixels[:x]

    for x in range(width):
        newPic.putpixel((x, y), newpixels[x])

newPic.show()

# romance