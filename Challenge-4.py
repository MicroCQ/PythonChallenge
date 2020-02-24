# Challenge - 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

# -*- coding: utf-8 -*

from urllib import request
import re

rep = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php", timeout=60)

# nothing = "12345"
nothing = "8022" # 16044 divide by 2
urlPath = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

while nothing:
    pattern = re.compile(r"\d+")
    rep1 = request.urlopen(urlPath + nothing, timeout=60)
    result = rep1.read().decode()
    print(result)
    nothing ="".join(pattern.findall(result))

print(nothing)

# peak.html
# http://www.pythonchallenge.com/pc/def/peak.html