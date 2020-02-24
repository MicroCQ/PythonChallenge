# Challenge - 5
# http://www.pythonchallenge.com/pc/def/peak.html

# -*- coding: utf-8 -*


from urllib import request
import pickle

'''
rep = request.urlopen("http://www.pythonchallenge.com/pc/def/peak.html", timeout=60)
print(rep.read())
'''

rep = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p", timeout=60)
ans = rep.read()
#print(ans)
resultes=pickle.loads(ans)

for i in resultes:
    for tmp in i:
        print(tmp[0] * tmp[1], end="")
    print("")

# channel
# http://www.pythonchallenge.com/pc/def/channel.html