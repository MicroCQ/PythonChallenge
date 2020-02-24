# Challenge-1
# http://www.pythonchallenge.com/pc/def/map.html

# -*- coding: utf-8 -*

baseStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "cdefghijklmnopqrstuvwxyzab"
outStr = ""

for i in baseStr:
    if i in str1:
        tmp = str1.index(i)
        outStr += str2[tmp]
    else:
        outStr += i

print(outStr)

# i hope you didnt translate it by hand. thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended. now apply on the url.

# another solver
transTab = str.maketrans(str1, str2)
oldUrl = "map"
print(oldUrl.translate(transTab))

# http://www.pythonchallenge.com/pc/def/ocr.html