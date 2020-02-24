# Challenge - 11
# http://www.pythonchallenge.com/pc/return/5808.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
from PIL import Image as im
import re

url = "http://www.pythonchallenge.com/pc/return/5808.html"
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
picName = "cave.jpg"
picFile = filePath + picName
origin = im.open(picFile)

width, height = origin.size
print(width, height)
odd = im.new("RGB", (width//2, height//2))
even = im.new("RGB", (width//2, height//2))

for x in range(width):
    for y in range(height):
        # 根据 x + y 的奇偶性质分离到不同的图片
        if (x + y) % 2 == 0:
            odd.putpixel((x//2, y//2), origin.getpixel((x, y)))
        else:
            even.putpixel((x//2, y//2), origin.getpixel((x, y)))

odd.show()
even.show()