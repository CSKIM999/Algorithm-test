from collections import deque

d = [[-1,0],[0,-1],[0,1],[1,0]]

r,c = list(map(int,input().split()))
table = []
water = []
cave = []
godo = []
for i in range(r):
    temp = list(input())
    ttmp = []
    for j in range(c):
        if temp[j] == '*':
            water.append((i,j))
            ttmp.append(1)
        elif temp[j] == 'D':
            cave = [i,j]
            ttmp.append(-1)
        elif temp[j] == 'S':
            godo = [i,j,1]
            ttmp.append(1e9)
        elif temp[j] == 'X':
            ttmp.append(-1)
        else:
            ttmp.append(1e9)
    table.append(ttmp)

for i,j in water:
    q = deque()
    q.append([i,j])

    hist = set()
    hist.add((i,j))
    while q:
        x,y = q.popleft()
        now = table[x][y]
        for k in range(4):
            nx,ny = x+d[k][0], y+d[k][1]
            if 0> nx or 0 > ny or nx >= r or ny >= c:
                continue
            if table[nx][ny] != -1 and table[nx][ny] > now+1 and (nx,ny) not in hist:
                table[nx][ny] = now+1
                q.append([nx,ny])
                hist.add((nx,ny))

q = deque()
q.append(godo)
x,y,n = godo
result = 1e9
hist = set()
hist.add((x,y))
while q:
    x,y,now = q.popleft()
    if result != 1e9 and now+1 > result:
        continue
    for i in range(4):
        nx,ny = x+d[i][0], y+d[i][1]
        if 0> nx or 0 > ny or nx >= r or ny >= c:
                continue
        if table[nx][ny] == -1:
            if [nx,ny] == cave and result > now+1:
                result = now+1
            continue
        if table[nx][ny] > now+1 and (nx,ny) not in hist:
            q.append([nx,ny,now+1])
            hist.add((nx,ny))

if result == 1e9:
    print("KAKTUS")
else:
    print(result-1)