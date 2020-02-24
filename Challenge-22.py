# Challenge - 22
# http://www.pythonchallenge.com/pc/hex/copper.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image as Im, ImageDraw
import turtle


# url = "http://www.pythonchallenge.com/pc/hex/copper.html"
url = "http://www.pythonchallenge.com/pc/hex/white.gif"
un = "butter"
pw = "fly"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read()
    # print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

filePath = "e:\WorkSpace\\PythonChallenge\\"
fileName = "white.gif"
pic = Im.open(filePath + fileName)
(width, height) = pic.size

newPic = Im.new("RGB", pic.size)
draw = ImageDraw.Draw(newPic)
cx, cy = 0, 100
for frame in range(pic.n_frames): # 133
    pic.seek(frame)
    left, upper, right, lower = pic.getbbox()
    # print(left, upper, right, lower)
    dx, dy = (left - 100) / 2, (upper - 100) / 2
    if dx == dy == 0:
        cx, cy = cx + 25, 100
    cx, cy = cx + dx, cy + dy
    draw.point([cx, cy])

    turtle.goto(cx, cy)

newPic.show()
# bonus