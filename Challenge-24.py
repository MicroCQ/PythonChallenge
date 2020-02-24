# Challenge - 24
# http://www.pythonchallenge.com/pc/hex/ambiguity.html

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image
import numpy as np
from queue import Queue

url = "http://www.pythonchallenge.com/pc/hex/ambiguity.html"
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

def BFS(startPos, endPos, imDatas):
    '''
    广度优先搜索迷宫路径
    :param startPos:  起始坐标, [x, y]
    :param endPos:  终止坐标, [x, y]
    :param imDatas:  迷宫图片像素值, (height, width, channel)
    :return: 返回记录父坐标的矩阵，上右下左分别用0, 1, 2, 3表示。
    根据这个矩阵，可回溯得到最短路径。
    '''

    visited = np.zeros(imDatas.shape[0:2], dtype=np.False_)
    #visited[639, 0] = True
    # visited[640, 1] = True

    father = -np.ones(imDatas.shape[0: 2], dtype=np.int8)
    dx = [-1, 0, 1, 0]  # 上右下左
    dy = [0, 1, 0, -1]

    bfs_queue = []
    bfs_queue.append(startPos)

    while bfs_queue:
        cur_pos = bfs_queue.pop(0)
        if cur_pos == endPos:
            break
        for i in range(4):
            x = cur_pos[0] + dx[i]
            y = cur_pos[1] + dy[i]
            if (0 <= x < width) and (0 <= y < height) and (imDatas[x, y, 1] == imDatas[x, y, 2] == 0) and (not visited[x, y]):
                father[x, y] = i
                bfs_queue.append([x, y])
        visited[cur_pos[0], cur_pos[1]] = True
    return father

def mapXY(pre, pos):
    ''' 根据父坐标类型和当前坐标，得到父坐标
    :param pre: 0,1,2,3分别表示当前坐标位于父坐标的上右下左
    :param pos: 当前坐标[x, y]
    :return: 父坐标[x, y]
    '''
    if pre == 0:
        pos[0] += 1
    elif pre == 1:
        pos[1] -= 1
    elif pre == 2:
        pos[0] -= 1
    elif pre == 3:
        pos[1] += 1
    else:
        raise Exception("Invalid Father Pos!")
    return pos

def getData(imDatas, father, startPos, endPos):
    '''
    回溯得到最短路径以及路径上每个像素点r通道的像素值
    :param imDatas: 迷宫图片像素值
    :param father: 每个点的父坐标
    :param startPos: 开始坐标 [x, y]
    :param endPos: 结束坐标 [x, y]
    :return: Red通道像素值, 用绿色像素标记的迷宫路径
    '''
    data = []
    curPos = endPos[:]

    while curPos != startPos:
        # 取Red通道像素值
        # data.append(bytes(imDatas[curPos[0], curPos[1], 0]))
        #data.append(chr(imDatas[curPos[0], curPos[1], 0]))
        data.append(imDatas[curPos[0], curPos[1], 0])
        # print(data)
        # 路径用绿色像素标记
        imDatas[curPos[0], curPos[1]] = [0, 255, 0, 255]
        curPos = mapXY(father[curPos[0], curPos[1]], curPos)
    data.append(chr(imDatas[startPos[0], startPos[1], 0]))
    return data, imDatas

filePath = "e:\WorkSpace\\PythonChallenge\\"
fileName = "maze.png"
pic = Image.open(filePath + fileName)
(width, height) = pic.size
imData = list(pic.getdata())
imData = np.array(imData)
#imData = imData.reshape((height, width, -1))
imData = imData.reshape((width, height, -1))

# print("BFS")
start, end = [639, 0], [1, 639]
path = BFS(start, end, imData)
# print("Get Path and data")
data, nimData = getData(imData, path, start, end)
open('maze.zip', 'wb').write(bytes(data[::2]))
#open('maze1.txt', 'wb').write(bytes(data[::2]))

nimData = nimData.reshape((-1, 4)).tolist()
nimData = [tuple(x) for x in nimData]
pic.putdata(nimData)
# pic.show()

# lake