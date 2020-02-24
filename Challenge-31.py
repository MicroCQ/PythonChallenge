# Challenge - 31
# http://www.pythonchallenge.com/pc/ring/grandpa.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image

'''
url = "http://www.pythonchallenge.com/pc/ring/grandpa.html"
un = "repeat"
pw = "switch"

# 识图搜索
#  Koh samui Thailand

'''

'''
url = "http://www.pythonchallenge.com/pc/rock/grandpa.html"
un = "kohsamui"
pw = "thailand"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    #print(req)
except error.HTTPError as e:
    print(e.code, e.reason)
'''

filePath = "e:\WorkSpace\\PythonChallenge\\"
picName = "mandelbrot.gif"  # mode P size (640, 480)
picFile = filePath + picName
pic = Image.open(picFile)
# pic.show()
(w, h) = pic.size
#print(pic.mode, pic.size, pic.info)
# left = "0.34" top = "0.57" width = "0.036" height = "0.027"
left, top, width, height = 0.34, 0.57, 0.036, 0.027

iters = 128
result = []
for y in range(h - 1, -1, -1):
  for x in range(0, w):
    z = 0 + 0j
    c = complex(left + x * width / w, top + y * height / h)
    for i in range(iters):
        z = z * z + c
        if abs(z) > 2:
            break
    result.append(i)

img = Image.new(pic.mode, pic.size)
img.putdata(result)
# img.show()

'''
data = pic.getdata()
dif = [result[i]-data[i] for i in range(len(data))]
'''
dif = [(a-b) for a, b in zip(list(pic.getdata()), result) if a != b] # len 1679

img2 = Image.new("L", (23, 73))
img2.putdata([i > 0 and 255 or 0 for i in dif])
img2.save("ans-31.jpg")
img2.show()
# 识图搜索 Arecibo message
# arecibo