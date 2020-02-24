# Challenge - 27
# http://www.pythonchallenge.com/pc/hex/speedboat.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image as Im
import bz2, keyword as kw

url = "http://www.pythonchallenge.com/pc/hex/speedboat.html"
un = "butter"
pw = "fly"

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
http://www.pythonchallenge.com/pc/ring/bell.html  Page Source <img src="zigzag.jpg"> <!-- did you say gif? -->
http://www.pythonchallenge.com/pc/hex/zigzag.gif
'''

filePath = "e:\WorkSpace\\PythonChallenge\\"
picName = "zigzag.gif"  # mode P size (320, 270)
picFile = filePath + picName
pic = Im.open(picFile)
# pic.show()
(width, height) = pic.size
data = pic.tobytes()
p = pic.getpalette()[::3]
# print(len(data), data)
# print(len(p), p)

table = bytes.maketrans(bytes([i for i in range(256)]), bytes(p))
trans = data.translate(table)

zipped = list(zip(data[1:], trans[:-1]))
indices = [i for i, p in enumerate(zipped) if p[0] != p[1]]
new = Im.new(pic.mode, pic.size)
color = [255, ]*len(data)
for i in indices:
  color[i] = 0
new.putdata(color)
# new.show() # not key word

dif = [p[0] for i, p in enumerate(zipped) if p[0] != p[1]]
#print(bytes(dif))
text = bz2.decompress(bytes(dif)).decode()
print(set([i for i in text.split() if not kw.iskeyword(i)])) # {'../ring/bell.html', 'switch', 'print', 'repeat', 'exec'}

'''
url = "http://www.pythonchallenge.com/pc/ring/bell.html"
un = "repeat"
pw = "switch"
'''