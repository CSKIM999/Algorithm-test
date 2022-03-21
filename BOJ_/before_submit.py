import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
table = []
d = [[-1,0],[0,1],[1,0],[0,-1]]
for i in range(n):
    table.append(list(map(int,input().split())))

bigM = [0,0,0]
def check_bfs():
    global bigM
    visit = []
    q = deque()
    flag = False
    for i in range(n):
        for j in range(m):
            if table[i][j] and not flag:
                q.append([i,j])
                visit.append([i,j])
                flag = True
                while q:
                    x,y = q.popleft()
                    if bigM[0]<table[x][y]:
                        bigM = [table[x][y],x,y]
                    for k in range(4):
                        nx,ny = x+d[k][0],y+d[k][1]
                        if table[nx][ny] and [nx,ny] not in visit:
                            visit.append([nx,ny])
                            q.append([nx,ny])
            if table[i][j] and [i,j] not in visit:
                return False
    if not flag:
        return 2
    return True

def melt_bfs(M):
    meltQ = deque()
    visit = []
    q = deque()
    a,x,y = M
    q.append([x,y])
    visit.append([x,y])
    while q:
        x,y = q.popleft()
        count = 0
        for i in range(4):
            nx,ny = x+d[i][0],y+d[i][1]
            if table[nx][ny] and [nx,ny] not in visit:
                visit.append([nx,ny])
                q.append([nx,ny])
            if not table[nx][ny]:
                count+=1
        meltQ.append([x,y,count])
    B = [0,0,0]
    while meltQ:
        x,y,c = meltQ.popleft()
        table[x][y] -= c
        if table[x][y] < 0:
            table[x][y] = 0
        elif table[x][y]>B[0]:
            B = [table[x][y],x,y]
    return B

if check_bfs() == 2:
    print(0)
else:
    time = 0
    while True:
        foo = check_bfs()
        if not foo:
            print(time)
            break
        elif foo ==2:
            print(0)
            break
        else:
            bigM = melt_bfs(bigM)
        time += 1

'''
1회차 시간초과??
'''