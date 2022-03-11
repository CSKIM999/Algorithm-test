from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q19238
#######  TODAY  #######
##### 2022. 03. 09 #####
GIVEN ) N*N 크기 안의 격자에 승객과 목적지, 택시가 존재한다. 승객과 목적지는 짝지어져있고, 택시는 승객을 운송해야한다
        택시가 비어있을 땐 항상 자기와 가장 가까운 승객을 향해 움직이며, 2명 이상이라면 행의 번호가 작은 승객을,
        또 같은 행에 2 명 이상이라면 열의 번호가 작은 승객을 우선적으로 탑승시킨다.
        또한, 택시에는 연료가 존재해서 한 칸 이동할 때 마다 연료를 1 소모한다. 만약 목적지에 도착하기 전 연료가 0이 된다면 그날의 업무는 끝난다.
        하지만 한 명의 승객을 목적지에 데려다 줄 때 마다 소모한 연료의 2배를 충전한다. 목적지에 도착하는것과 동시에 0이 되는것은 실패로 간주하지 않는다.
        승객과 택시는 같은칸에 존재할 수 있다.

INPUT ) 첫째 줄에 지도의 크기 N ( 2<= N <= 20 ), 승객의 수 M ( 1 <= M <= N**2 ) 그리고 초기연료의 양 F( 1 <= F <= 500,000 ) 가 주어진다.
        연료통의 크기는 무한하여 초기연료 이상으로 연료가 충전될 수 있다.
        둘째 줄부터 N 개의 줄에 걸쳐 지도가 주어진다. 0 은 빈칸, 1 은 벽이다
        그 다음 줄에 택시의 시작위치가 주어진다
        그리고 M 개의 줄에 걸쳐 각 승객의 출발지와 목적지가 주어진다
OUTPUT) 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력하라. 만약 업무가 종료되거나 모든 손님을 이동시킬 수 없을 땐 -1 을 출력하라
Approach )  먼저 손님을 순회하며 목적지까지의 연료소모량을 저장하자
            그리고 택시에서 손님의 순서를 파악해서 연료를 소모 충전하자

            3min
'''
# import sys
# input = sys.stdin.readline
from collections import deque
d = [[-1,0],[1,0],[0,-1],[0,1]]
N,M,F = list(map(int,input().split()))
table = []
for i in range(N):
    table.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            table[i][j] = -1
V = [False for _ in range(M)]
taxi = list(map(int,input().split()))
cost = {}
dic = []
for _ in range(M):
    x,y,nx,ny = list(map(int,input().split()))
    dic.append([[x-1,y-1],[nx-1,ny-1]])

def bfs(start):
    q = deque([[start[0],start[1]]])
    Rtable = [i[:] for i in table]
    Rtable[start[0]][start[1]] = 1
    while q:
        x,y = q.popleft()
        point = Rtable[x][y]
        for i in range(4):
            nx,ny = x+d[i][0],y+d[i][1]
            if 0<= nx < N and 0<= ny < N and Rtable[nx][ny] == 0:
                Rtable[nx][ny] = point+1
                q.append([nx,ny])
    return Rtable


for i in range(M):
    x,y = dic[i][0]
    nx,ny = dic[i][1]
    NF = bfs([x,y])[nx][ny] -1
    cost[i] = NF
# cost = {0: 7, 1: 6, 2: 4}

for _ in range(M):
    temp = bfs([taxi[0]-1,taxi[1]-1])
    ND = []
    for i in range(M):
        x,y = dic[i][0]
        nx,ny = dic[i][1]
        if not V[i]:
            ND.append([temp[x][y]-1,[x,y],i])
    ND.sort()
    if ND[0][0] == -1:
        F = -1
        break
    if cost[ND[0][2]] == -1:
        F = -1
        break
    F -= ND[0][0]
    if F < 0:
        F = -1
        break
    F -= cost[ND[0][2]]
    if F < 0:
        F = -1
        break
    F += 2*cost[ND[0][2]]
    V[ND[0][2]] = True
    taxi = [dic[ND[0][2]][1][0]+1,dic[ND[0][2]][1][1]+1]


print(F)