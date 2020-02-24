# Challenge - 6
# http://www.pythonchallenge.com/pc/def/channel.html

# -*- coding: utf-8 -*

from urllib import request
import zipfile
import re
'''
rep = request.urlopen("http://www.pythonchallenge.com/pc/def/channel.html", timeout=60)
print(rep.read())

rep = request.urlopen("http://www.pythonchallenge.com/pc/def/channel.zip", timeout=60)
print(rep.read())
'''
filePath = "e:\WorkSpace\\PythonChallenge\\"
zipName = "channel.zip"
tmpPath = filePath + "tmp\\"
zp = zipfile.ZipFile(zipName, "r")

print(zp.open("readme.txt", "r"))
zp.extract("readme.txt", tmpPath)
tmp = open(tmpPath + "readme.txt", "rb").read().decode()

pattern = re.compile(r"\d+")

# transNum = "".join(re.findall(pattern, tmp))
transNum = "90052"
comments = ""
while transNum:
    transFile = transNum + ".txt"
    zp.extract(transFile, tmpPath)
    tmp = open(tmpPath + transFile, "rb").read().decode()
    transNum = "".join(re.findall(pattern, tmp))
    zpInfo = zp.getinfo(transFile)
    comments = "".join(zpInfo.comment.decode())
    print(comments, end="")

# HOCKEY
# oxygen








