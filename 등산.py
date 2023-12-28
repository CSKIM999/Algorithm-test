from collections import deque
from string import ascii_lowercase,ascii_uppercase
idx = 0
dic = {}
for i in ascii_uppercase:
    dic[i] = idx
    idx += 1
for i in ascii_lowercase:
    dic[i] = idx
    idx += 1

dx = [-1,0,0,1]
dy = [0,-1,1,0]
table = []
n,m,t,d = list(map(int,input().split()))
for _ in range(n):
    table.append(list(input()))
tableDic = {}
for i in range(n):
    for j in range(m):
        tableDic[(i,j)] = 1e7
def calMove(t,f):
    tx,ty = t
    fx,fy = f
    tv,fv = dic[table[tx][ty]],dic[table[fx][fy]]
    if tv <= fv:
        return 1
    else:
        return (fv-tv)**2

q = deque()
q.append([0,0])
mainTable = [[1e7 for _ in range(m)] for _ in range(n)]
mainTable[0][0] = 0
subTable = [[1e7 for _ in range(m)] for _ in range(n)]
subTable[0][0] = 0
while q:
    x,y = q.popleft()
    v = mainTable[x][y]
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if abs(dic[table[nx][ny]] - dic[table[x][y]]) > t:
                continue
            newV = v+calMove([nx,ny],[x,y])
            if mainTable[nx][ny] > newV:
                mainTable[nx][ny] = newV
                q.append([nx,ny])

def dfs(v,x,y,dTable):
    global subTable
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if subTable[nx][ny] != 1e7 and [nx,ny] != [0,0]:
                newV = v+subTable[nx][ny]+calMove([nx,ny],[x,y])
                dTable[0][0] = min(dTable[0][0],newV)
                return
            newV = v+calMove([nx,ny],[x,y])
            if abs(dic[table[nx][ny]] - dic[table[x][y]]) > t:
                continue
            if nx==0 and ny == 0:
                dTable[0][0] = min(dTable[0][0],newV)
                return
            if newV > dTable[0][0]:
                continue
            if dTable[nx][ny] > newV:
                dTable[nx][ny] = newV
                dfs(newV,nx,ny,dTable)
res = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == 'c':
            print('now')
        if i == 0 and j == 0:
            continue
        # if res != 0 and res > dic[table[i][j]]:
        #     continue
        temp = [[1e7 for _ in range(m)] for _ in range(n)]
        temp[i][j] = 0
        dfs(0,i,j,temp)
        dist = temp[0][0]
        subTable[i][j] = dist
        if mainTable[i][j] + dist <= d:
            res = max(res,dic[table[i][j]])
print(res)