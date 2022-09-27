import sys
from collections import deque
input = sys.stdin.readline
n, m = list(map(int, input().split()))
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
d = [[-1, 0, 0, 1], [0, -1, 1, 0]]
result = 0


def bfs():
    global result
    rtable = [[6 for _ in range(n)] for _ in range(n)]
    if result == 668:
        result
    dic = {i: [0, 0, [0, 0], []] for i in range(m+1)}
    for ix in range(n):
        for iy in range(n):
            if rtable[ix][iy] != 6:
                continue
            if table[ix][iy] == -1 or table[ix][iy] == []:
                if table[ix][iy] == []:
                    continue
                rtable[ix][iy] = -1
                continue
            q = deque()
            node = table[ix][iy]
            rtable[ix][iy] = node
            q.append([ix, iy])
            hist = [[[ix, iy]], []]
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx, ny = x+d[0][i], y+d[1][i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if table[nx][ny] == node and [nx, ny] not in hist[0]:
                            rtable[nx][ny] = node
                            hist[0].append([nx, ny])
                            q.append([nx, ny])
                        elif node != 0 and table[nx][ny] == 0 and [nx, ny] not in hist[1]:
                            hist[1].append([nx, ny])
                            q.append([nx, ny])
            block, zblock = len(hist[0])+len(hist[1]), len(hist[1])
            hist = hist[0]+hist[1]
            d1, d2, d3, d4 = dic[node]
            if d1 < block:
                dic[node] = [block, zblock, [ix, iy], [i[:] for i in hist]]
            elif d1 == block:
                if d2 < zblock:
                    dic[node] = [block, zblock, [ix, iy], [i[:] for i in hist]]
                    continue
                elif d2 == zblock and d3[0] <= ix:
                    if d3[0] < ix:
                        dic[node] = [block, zblock, [ix, iy], [i[:]
                                                               for i in hist]]
                        continue
                    elif d3[0] == ix and d3[1] < iy:
                        dic[node] = [block, zblock, [ix, iy], [i[:]
                                                               for i in hist]]

    target = [0, 0, [0, 0]]

    def setTarget(lst):
        nonlocal target
        target = lst

    for i in range(1, m+1):
        a, b, c, _ = dic[i]
        if a >= target[0]:
            if a > target[0]:
                setTarget(dic[i])
                continue
            if b >= target[1]:
                if b > target[1]:
                    setTarget(dic[i])
                    continue
                if c[0] >= target[2][0]:
                    if c[0] > target[2][0]:
                        setTarget(dic[i])
                        continue
                    if c[1] > target[2][1]:
                        setTarget(dic[i])
    if target[0] == 0:
        return False
    elif target[0]+target[1] < 2:
        return False
    result += target[0] ** 2
    target = target[3]
    for x, y in target:
        table[x][y] = []


def gravity():
    for i in range(n-1, -1, -1):
        empty = []
        for j in range(n-1, -1, -1):
            if empty == []:
                if table[j][i] == []:
                    empty = [j, i]
            else:
                if table[j][i] == []:
                    continue
                if table[j][i] >= 0:
                    x, y = empty
                    table[x][y] = table[j][i]
                    table[j][i] = []
                    empty = [x-1, y]
                else:
                    empty = []
                    continue


def rotate():
    global table
    newTable = [[table[j][i] for j in range(n)] for i in range(n-1, -1, -1)]
    table = [i[:] for i in newTable]


while True:
    if bfs() == False:
        break
    gravity()
    rotate()
    gravity()

print(result)
