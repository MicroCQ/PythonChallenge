# Challenge - 32
# http://www.pythonchallenge.com/pc/rock/arecibo.html
# 参考 https://www.jianshu.com/p/378482e69f51

# -*- coding: utf-8 -*

from urllib import request, error
from PIL import Image

'''
url = "http://www.pythonchallenge.com/pc/rock/arecibo.html"
un = "kohsamui"
pw = "thailand"

try:
    pwMgr = request.HTTPPasswordMgrWithDefaultRealm()
    pwMgr.add_password(None, url, un, pw)
    handler = request.HTTPBasicAuthHandler(pwMgr)
    opener = request.build_opener(handler)
    req = opener.open(url).read().decode()
    # print(req)
except error.HTTPError as e:
    print(e.code, e.reason)
'''
# Fill in the blanks <!-- for warmup.txt -->

import itertools
import time

def loadfile(file):
    """
    读取文件
    :param file: 文件名
    :return: vertical 高度, horizontal 宽度, v 纵坐标块数, h 横坐标块数
    """
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if (not line.startswith("#")) and (line.strip() != "")]
        raw = [list(map(int, line.split())) for line in lines]
        # print(raw)
        vertical, horizontal = raw[0][0], raw[0][1]
        v, h = raw[1:vertical + 1], raw[vertical + 1:]
        return vertical, horizontal, v, h


def getZero(num, length, pas, start):
    numList = [i for i in range(1, length + 1)]
    # print(numList)
    zeroSet = []
    for i in range(length - num - start - 1, pas - 2, -1):
        tmp = numList[:i]
        zeroSet.append(list(itertools.permutations(tmp, pas - 1)))

    for i in range(length - num - start, pas - 1, -1):
        tmp = numList[:i]
        zeroSet.append(list(itertools.permutations(tmp, pas)))
    return zeroSet


def getData(length, data):
    d = []  # 初始化的数据
    for i in data:
        d += [1, ]*i + [0]
    d = d[:-1]
    x = length - len(d)  # x为剩余可插入的点数
    pos = {0}  # pos为插入位置
    i = 0
    try:
        while True:
            t = d.index(0, i)
            pos.add(t)
            i = t + 1
    except:
        if len(d) > 1:
            pos.add(len(d) - 1)  # [0, 2, 4, 7] 零所在位置（2，4）和头尾（0，7）都可用于插入。
    pos = list(pos)
    pos.sort()
    return d, x, pos

def getAlt(data, x, pos, alt):
    if len(pos) == 1:
        data = data + [0, ] * x
        alt.append(data)
        return
    for m in range(x, -1, -1):
        if m > 0:
            new_d = data[:pos[0]] + [0, ] * m + data[pos[0]:]
            new_pos = [p + m for p in pos]
            if x - m > 0:  # 剩余可分配0的个数为 x-m 个
                getAlt(new_d, x - m, new_pos[1:], alt)
            elif x - m == 0:  # 剩余可分配0的个数为0，完成需要
                alt.append(new_d)
        elif m == 0:
            getAlt(data, x, pos[1:], alt)


def initBoard(length, lists, alt, d):
    for i, list in enumerate(lists):
        d, x, pos = getData(length, list)
        getAlt(d, x, pos, alt[i])  # 获取可能性
        #print(i, list, len(alt[i]), alt[i])



def getLine(i, board, d): #  获取第 i 行/列。
  if d == 0:
    return board[i]
  else:
    return [board[j][i] for j in range(len(board))]


def getTimes(source, l):# 获取所有方案中元素在其各个位置出现次数，如source = [[1, 1, 0, 0], [0, 1, 1, 0]]
  res = [0,] * l# 出现次数。
  for s in source:
    for i in range(l):
      res[i] = res[i] + s[i]
  return res


def getIndex(line, pss, ass):
    for i in range(len(line)):
        if line[i] == 1:
            pss.append(i)
        elif line[i] == 0:
            ass.append(i)
    return

def del_Alt(pss, ass, lists):
    res = []
    for l in lists:
        flag = True
        for p in pss:
            if l[p] != 1:
                flag = False
                break
        for a in ass:
            if l[a] != 0:
                flag = False
                break
        if flag:
            res.append(l)
    return res


def rever_map(altLists, length, board, d):
    for i in range(length):
        pss, ass = [], []
        line = getLine(i, board, d)
        getIndex(line, pss, ass)
        altLists[i] = del_Alt(pss, ass, altLists[i])
        times = getTimes(altLists[i], length)
        if len(altLists[i]) > 0:
            setMap(i, altLists[i], times, board, d)  # 将确定的选项写入
    return

def setMap(i, list, times, board, d):
    l = len(list)
    for j, t in enumerate(times):
        if d == 0:
            if t == l:
                board[i][j] = 1
            elif t == 0:
                board[i][j] = 0
        elif d == 1:
            if t == l:
                board[j][i] = 1
            elif t == 0:
                board[j][i] = 0


def playgame(width, height, xlist, ylist):
    alt_X = [[] for i in range(height)]  # 所有X坐标可能的情况
    alt_Y = [[] for i in range(width)]  # 所有X坐标可能的情况
    dires = [0, 1] # 0 水平 1 垂直

    initBoard(width, xlist, alt_X, dires[0])
    initBoard(height, ylist, alt_Y, dires[1])

    board = [[-1 for i in range(width)] for i in range(height)]  # 初始化棋盘
    temp_board = []
    count = 0

    flag = False
    count = 0
    print(time.process_time())
    while not flag:
        rever_map(alt_X, width, board, dires[0])
        rever_map(alt_Y, height, board, dires[1])
        count = count + 1
        flag = check_board(board)

    return board


def print_board(board):
    for b in board:
        print(b)



def check_board(board):
    for b in board:
        for i in range(len(b)):
            if b[i] == -1:
                return False
    return True


def drawPic(board, width, height):
    pic = Image.new("L", (width, height))
    data = []
    for b in board:
        for p in b:
            data.append((1-p)*255)
    #print(data)
    pic.putdata(data)
    return pic

filePath = "e:\WorkSpace\\PythonChallenge\\ans32\\"
#fileName = "warmup.txt"
fileName = "up.txt"
txtFile = filePath + fileName

vl, hl, ver, hor = loadfile(txtFile)
print(vl, hl, ver, hor)
board = playgame(vl, hl, ver, hor)
print_board(board)
print(time.process_time())
img = drawPic(board, vl, hl)
img.resize((100, 100)).show()

# http://www.pythonchallenge.com/pc/rock/python.html
# 自由的（free as in speech），而不是免费的（free as in beer）
# beer
