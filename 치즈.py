from collections import deque
n,m = list(map(int,input().split()))
table = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs():
    q = deque()
    q.append([0,0])
    hist = set()
    melt = set()
    res = set()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if table[nx][ny] == 0 and (nx,ny) not in hist:
                    hist.add((nx,ny))
                    q.append((nx,ny))
                elif table[nx][ny] == 1:
                    if (nx,ny) in melt:
                        res.add((nx,ny))
                    else:
                        melt.add((nx,ny))
    return res
time = 0
while True:
    melted = bfs()
    if len(melted) == 0:
        print(time)
        break
    for x,y in melted:
        table[x][y] = 0
    time += 1