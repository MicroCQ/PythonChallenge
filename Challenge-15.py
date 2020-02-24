# Challenge - 15
# http://www.pythonchallenge.com/pc/return/uzi.html

# -*- coding: utf-8 -*

from urllib import request
from urllib import error
import datetime

url = "http://www.pythonchallenge.com/pc/return/uzi.html"
un = "huge"
pw = "file"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    print(req)
except error.HTTPError as e:
    print(e.code, e.reason)

for i in range(1006, 1997, 10):
    if i % 4 == 0:
        date = datetime.date(i, 1, 26)
        if date.weekday() == 0:
            print(i)

'''
1176
1356
1576
1756  second youngest
1976

1756-1-27 西元1756年1月27日，史上最偉大的古典音樂家莫札特(Wolfgang Amadeus Mozart)在現在的奧地利薩爾斯堡出生，
mozart
'''
