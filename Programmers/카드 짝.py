'''
자료구조
카드목록 => [false * n]
    집으면 true
    짝 맞춰지면 지금까지 온 모든 루트에서 

만들 함수 목록

1. 한칸 이동
2. 점프
3. 카드집기


'''

from itertools import permutations
from collections import deque

board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
start = [0, 1]
dic = {}
node = set()
for i in range(4):
    for j in range(4):
        now = board[i][j]
        if now != 0:
            node.add(now)
            try:
                dic[now].append([i, j])
            except KeyError:
                dic[now] = [[i, j]]

M = max(dic)

permut = permutations(range(1, M+1), M)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def walk(now):
    x, y = now
    temp = []
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            temp.append([nx, ny])
    return temp


def jump(now, table):
    x, y = now
    temp = []
    for i in range(4):
        nnx, nny = dx[i], dy[i]
        for j in range(1, 5):
            nx, ny = x+nnx*j, y+nny*j
            if 0 <= nx < 4 and 0 <= ny < 4:
                if table[nx][ny] == 0:
                    continue
                if j == 1:
                    continue
                temp.append([nx, ny])
                break
            else:
                if j > 2:
                    nx, ny = nx-nnx, ny-nny
                    temp.append([nx, ny])
                break

    return temp


def bfs(start, table):
    temp = [[10 for _ in range(4)] for _ in range(4)]
    q = deque()
    x, y = start
    temp[x][y] = 0
    q.append([start, 0])
    while q:
        now, count = q.popleft()
        x, y = now
        t = []
        t.extend(walk([x, y]))
        t.extend(jump([x, y], table))
        for i in t:
            ix, iy = i
            if temp[ix][iy] > count + 1:
                temp[ix][iy] = count+1
                q.append([[ix, iy], count+1])
    return temp


result = 1e9
for s in permut:
    a, b, c = s
    a, b, c = dic[a], dic[b], dic[c]
    for i in range(2):
        count = 0
        ax0, ay0 = a[i]
        ax1, ay1 = a[i-1]
        temp = bfs(start, board)
        count += temp[ax0][ay0] + 1
        temp = bfs([ax0, ay0], board)
        count += temp[ax1][ay1] + 1
        tBoard = [i[:] for i in board]
        tBoard[ax0][ay0] = 0
        tBoard[ax1][ay1] = 0
        for j in range(2):
            bx0, by0 = b[j]
            bx1, by1 = b[j-1]
            temp = bfs([ax1, ay1], tBoard)
            count += temp[bx0][by0] + 1
            temp = bfs([bx0, by0], tBoard)
            count += temp[bx1][by1] + 1
            tBoard[bx0][by0] = 0
            tBoard[bx1][by1] = 0
            for k in range(2):
                cx0, cy0 = c[j]
                cx1, cy1 = c[j-1]
                temp = bfs([bx1, by1], tBoard)
                count += temp[cx0][cy0] + 1
                temp = bfs([cx0, cy0], tBoard)
                count += temp[cx1][cy1] + 1
                result = min(result, count)
print(result)
