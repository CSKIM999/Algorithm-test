from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2573
#######  TODAY  #######
##### 2022. 03. 21 #####
GIVEN ) n*m 크기의 테이블에 빙산의 크기와 위치가 주어진다. 주변에 0 의 갯수에 따라 녹는 속도가 달라진다고 했을 때,
        빙산의 덩어리가 2개 이상으로 갈라지는 시간을 출력하라
INPUT ) 첫째 줄에 N,M 이 주어진다 ( 3<= N,M <= 300 )
        그 다음 N 개의 줄에 걸쳐 테이블의 상태가 주어진다. 0 은 빈칸, 나머지는 10 이하의 정수로 주어진다.
OUTPUT) 빙산이 분리되는 최초의 시간을 출력하라. 만약 다 녹았음에도 분리되지 않으면 0을 출력하라

Approach )  제일 큰 빙산의 좌표를 저장하고 녹는bfs 돌린 이후 테이블 bfs 돌려서 카운트 2개이상 혹은 0 개 나오면 break 하게 하면 안되나?
'''
# import sys
# input = sys.stdin.readline

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