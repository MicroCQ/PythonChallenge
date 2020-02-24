# Challenge - 21
# -*- coding: utf-8 -*

import zipfile, zlib, bz2, gzip

filePath = "e:\WorkSpace\\PythonChallenge\\"
fileName = "ans-20.zip"
pw = b"redavni"

files = zipfile.ZipFile(filePath+fileName, "r")

'''
可以看到，对于不同输入，各个压缩库输出的字节串都各自带有各自的标识头：
zlib：x\x9c
bz2：BZh
gzip：\x1f
'''
file = files.infolist()[1].filename
with files.open(file, "r", pwd=pw) as f:
    content = f.read()
    while True:
        if content.startswith(b'BZh'):
            content = bz2.decompress(content)
            print("B", end="")
        elif content.startswith(b'x\x9c'):
            content = zlib.decompress(content)
            print(" ", end="")
        elif content.startswith(b'\x1f'):
            content = gzip.decompress(content)
            print("G", end="")
        elif content.endswith(b'\x9cx'):
            content = content[::-1]
            print()
        else:
            break
    print()

print(content[::-1])  #  'look at your logs'

# copper
