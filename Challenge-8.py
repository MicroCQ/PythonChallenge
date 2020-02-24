# Challenge - 8
# http://www.pythonchallenge.com/pc/def/integrity.html

# -*- coding: utf-8 -*

from urllib import request
import bz2

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
req = request.urlopen(url, timeout=60).read()
un = req.splitlines()[20][5:-1]
pw = req.splitlines()[21][5:-1]

print(un)
print(pw)

'''
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un).decode())
print(bz2.decompress(pw).decode())
'''

# un = huge
# pw = file
