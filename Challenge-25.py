# Challenge - 25
# http://www.pythonchallenge.com/pc/hex/lake.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image
import base64, wave

url = "http://www.pythonchallenge.com/pc/hex/lake.html"
un = "butter"
pw = "fly"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    # print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

'''
wavUrl = "http://www.pythonchallenge.com/pc/hex/lake{0}.wav"
header = {"Authorization": " Basic YnV0dGVyOmZseQ=="}
for i in range(1, 26):
    req = request.Request(wavUrl.format(i), headers=header)
    data = request.urlopen(req).read()
    with open('lake\\lake{0}.wav'.format(i), 'wb') as f:
        f.write(data)

'''

wav = "e:\WorkSpace\\PythonChallenge\\lake\\lake{0}.wav"
res = Image.new('RGB', (300, 300))
ws = [wave.open(wav.format(i)) for i in range(1, 26)]
for i in range(25):
    data = ws[i].readframes(ws[i].getnframes())
    # print(data)
    im = Image.frombytes('RGB', (60, 60), data)
    res.paste(im, (60*(i % 5), 60*(i//5)))
res.show()

# decent
