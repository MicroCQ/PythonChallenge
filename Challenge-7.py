# Challenge - 7
# http://www.pythonchallenge.com/pc/def/oxygen.html

# -*- coding: utf-8 -*

'''
from urllib import request

rep = request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.html", timeout=60)
print(rep.read())
'''

from PIL import Image as im
import re

filePath = "e:\WorkSpace\\PythonChallenge\\"
picName = "oxygen.png"
picFile = filePath + picName
pic = im.open(picFile)

for x in range(0, pic.size[0]):
    for y in range(0, pic.size[1]):
        r, g, b, a = pic.getpixel((x, y))
        rgba = (r, g, b, a)
        '''
        if (r == g) & (g == b):
            print(rgba, x, y)
        '''

tmpPic = pic.crop((0, 43, 607, 51))
tmpPic = tmpPic.convert("L")
#tmpPic.show()
ans = ""
for x in range(0, tmpPic.size[0]):
    r = tmpPic.getpixel((x, tmpPic.size[1]-1))
    if x % (tmpPic.size[1]-1) == 0:
        ans += chr(r)

print(ans)
results = re.findall(r"[0-9]{3}", ans)
for i in range(0, len(results)):
    print(chr(int(results[i])), end="")

# integrity