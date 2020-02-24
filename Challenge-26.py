# Challenge - 26
# http://www.pythonchallenge.com/pc/hex/decent.html

# -*- coding: utf-8 -*

from urllib import request, error
import hashlib as ha

url = "http://www.pythonchallenge.com/pc/hex/decent.html"
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
源码中有一提示：you've got his e-mail，指的是[Level 19]中的leopold.moz@pythonchallenge.com。

这个邮件存在，需要我们以sorry或apology（或其他？）为主题发个邮件过去。邮件回复：

Never mind that.
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?
'''

md5 = "bbb8b499a0eef99b52c7f13f4e78c24b"
data = open("mybroken.zip", "rb").read()

'''with open("tmp1.txt", "w") as f:'''
for i in range(len(data)):  # 2701
    # print(i)
    for j in range(256):
        newData = data[:i] + bytes([j]) + data[i+1:]

        # f.write("i=%d, j=%d, md5=%s, newData=%s" %(i, j, ha.md5(newData).hexdigest(), newData))
        # f.write("\n")
        '''
        if i == 1234 and j == 168:
            print(data)
            print(newData)
        '''
        if ha.md5(newData).hexdigest() == md5:
            open('repaired.zip', 'wb').write(newData)
            print(i, j)
            raise StopIteration

# speed boat