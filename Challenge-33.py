# Challenge - 33
# http://www.pythonchallenge.com/pc/rock/beer.html

# -*- coding: utf-8 -*
'''
from urllib import request, error

url = "http://www.pythonchallenge.com/pc/rock/beer.html"
un = "kohsamui"
pw = "thailand"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

http://www.pythonchallenge.com/pc/rock/beer1.jpg
http://www.pythonchallenge.com/pc/rock/beer2.jpg -- no, png
http://www.pythonchallenge.com/pc/rock/beer2.png

If you are blinded by the light, remove its power, with its might.
Then from the ashes, fair and square, another truth at you will glare.
'''

from PIL import Image
import numpy as np

filePath = "e:\WorkSpace\\PythonChallenge\\"
picName = "beer2.png" # mode L 138*138
picFile = filePath + picName
pic = Image.open(picFile)
#print(pic.info, pic.mode, pic.size)

imdata = np.array(list(pic.getdata()))
lt = []
ld = []
for i in imdata:
    if not (i in lt):
        lt.append(i)
        ld.append([i, 1])
    else:
        ld[lt.index(i)][1] += 1

imarray = np.array(sorted(ld, key=lambda ld: ld[0]))
#print([np.sqrt(i) for i in np.cumsum(imarray[:, 1])])

for i in range(imarray.shape[0] - 2, 0, -2):
    newdata = imdata[np.where(imdata < imarray[i, 0])]
    size = int(np.sqrt(len(newdata)))
    newIm = Image.new('L', (size, size))
    newIm.putdata(newdata)
    newIm.save('ans33/level33_%i.png' % i)

# gremlins

'''
# 另一种解法
from PIL import Image
import math

with Image.open('beer2.png') as img:
  data = list(img.getdata())
for i in range(254, -1, -1):
  imgData = [d for d in data if d < i]
  x = math.sqrt(len(imgData))
  if x == int(x) and x > 0:
    newImg = Image.new('L', (int(x), int(x)))
    newImg.putdata(imgData)
    newImg.save('ans33/'+str(x)+'.png')
    #newImg.show()
'''




