# Challenge - 24 - new
# http://www.pythonchallenge.com/pc/hex/ambiguity.html

# -*- coding: utf-8 -*

from PIL import Image
import numpy as np
from queue import Queue

file = "e:\WorkSpace\\PythonChallenge\\maze.png"
pic = Image.open(file)
(width, height) = pic.size
dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
entrance, exit = (639, 0), (1, 640)
# entrance, exit = (0, 639), (640, 1)
white = (255, 255, 255, 255)
queue = [exit]
next_p = {}
pixels = pic.load()

nw = []
for x in range(width):
    for y in range(height):
        if pixels[x, y] != white:
            nw.append((x, y))
# open("tmp.txt", "w").write(str(nw))
# print("found %d non-white pixels" % len(nw))  # 206326

# BFS
while queue:
    pos = queue.pop(0)
    if pos == entrance:
        break
    for d in dire:
        temp = (pos[0]+d[0], pos[1]+d[1])
        #print(temp[0], temp[1])
        if (temp not in next_p) and (0 <= temp[0] < width) and (0 <= temp[1] < height) and (pic.getpixel(temp) != white):
            #print(pixels[temp[0], temp[1]])
            next_p[temp] = pos
            queue.append(temp)

path = []
imdata = pixels
while pos != exit:
    path.append(pic.getpixel(pos)[0])
    imdata[pos[0], pos[1]] = (0, 255, 0, 255)
    pos = next_p[pos]
    pic.putdata(imdata[pos[0], pos[1]])
open('maze.zip', 'wb').write(bytes(path[1::2]))
#print(len(path)) # 56827 44622
# print(bytes(path[1::2])) # len 22311
# print(path[1::2])
#pic.putdata(t for t in imdata)
#pic.show()
