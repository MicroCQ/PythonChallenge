# Challenge - 30
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image

url = "http://www.pythonchallenge.com/pc/ring/yankeedoodle.html"
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
fileName = "yankeedoodle.csv"
csvFile = filePath + fileName

data = []
with open(csvFile, "r") as f:
    for l in f.read().split(","):
        data.append(l.strip())
# print(len(data)) # 7367
img = Image.new("F", (53, 139))
img.putdata([float(d) for d in data], 256)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.ROTATE_90)
#img.show()
# n = str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]

by = bytes([int(x[0][5]+x[1][5]+x[2][6]) for x in zip(data[::3], data[1::3], data[2::3])])
print(by.decode())

'''
So, you found the hidden message.
There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.
grandpa 
'''