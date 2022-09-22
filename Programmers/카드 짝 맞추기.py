from itertools import permutations
from collections import deque

board = [[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]]
start = [0, 0]
# board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
# start = [0, 1]

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
                    if table[nx][ny] != 0:
                        break
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


def dfs(seq, frm, table, count, depth):
    global result
    if seq == (1, 2, 5, 4, 3, 6):
        pass
    if len(seq) == depth:
        if count == 30:
            pass
        result = min(result, count)
        return
    if result < count+1 or result < count+(4*(len(seq)-depth)):

        return
    now = dic[seq[depth]]

    for i in range(2):
        newcount = count
        nx0, ny0 = now[i]
        nx1, ny1 = now[i-1]
        card = int(table[nx0][ny0])
        temp = bfs(frm, table)
        newcount += temp[nx0][ny0] + 1
        temp = bfs([nx0, ny0], table)
        newcount += temp[nx1][ny1] + 1
        table[nx0][ny0] = 0
        table[nx1][ny1] = 0
        dfs(seq, [nx1, ny1], [x[:] for x in table], newcount, depth+1)
        table[nx0][ny0] = card
        table[nx1][ny1] = card


result = 1e9
for s in permut:
    lst = s
    pn = [[] for _ in range(len(lst))]
    for pi in range(len(lst)):
        count = 0
        now = lst[pi]
        pn[pi].extend(dic[now])
    dfs(s, start, [t[:] for t in board], 0, 0)

print(result)
