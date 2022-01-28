'''
직사각형 모양의 방을 로봇청소기로 청소하고자 한다. 일부 칸에는 가구가 놓여있고 로봇은 가구 위를 이동할 수 없다.
로봇은 오직 인접한 한 칸으로만 이동할 수 있을 때 모든 더러운칸을 청소하는데 필요한 최소 이동횟수를 반환하라

입력은 여러개의 테스트케이스로 주어진다
각 테스트케이스의 첫째 줄에는 가로크기 w, 세로크기 h 가 주어진다.(1<=w,h<=20) 둘째 줄 부터 h개의 줄에 방의 정보가 주어진다.
. : 깨끗한 칸 ,, * : 더러운 칸 ,, x : 가구 ,, o : 로봇청소기의 시작위치
더러운 칸의 개수는 10개 이하이며, 로봇청소기는 오직 하나만 존재한다.
입력의 마지막 줄에는 0 이 2개 주어진다.

각 테스트케이스마다, 더러운 칸을 모두 깨끗한 칸으로 바꾸는 최소 이동횟수를 한줄에 하나씩 출력하라.
만약 방문할 수 없는 더러운 칸이 존재하는 경우 -1을 출력하라
'''
from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline
d = [[0,-1],[1,0],[0,1],[-1,0]]
def bfs(now,Tdata):
    x,y = now
    W,H = len(Tdata[0]), len(Tdata)
    Vtable = [[i*0 for i in j] for j in Tdata]
    Vtable[x][y] = 1
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        c = Vtable[x][y]
        for a,b in d:
            nx,ny = x+a,y+b
            if 0<=nx<H and 0<=ny<W: #우선 테이블 안에 위치하는가?
                if Tdata[nx][ny] != 2 and not Vtable[nx][ny]: #벽에 가로막히진 않았는가?
                    Vtable[nx][ny] = c+1
                    q.append((nx,ny))
    return Vtable


while True:
    result = 1e9
    w,h = map(int,input().split())
    if w == 0:
        break
    case = []
    for i in range(h):
        case.append(list(input().strip()))
    dic = {'.':0,'*':-1,'x':2,'o':1}
    dxdy = [[0,-1],[1,0],[0,1],[-1,0]]
    table = []
    robot = []
    trashes = []

    for i in range(h): #table 의 str 을 int 로 변환
        temp = []
        for j in range(len(case[i])):
            now = dic[case[i][j]]
            temp.append(now)
            if now==1 or now == -1:
                if now == 1:
                    robot.append(i)
                    robot.append(j)
                else:
                    trashes.append([i,j])

        table.append(temp)

    N = len(trashes)
    bfsTable = [[0]*N for _ in range(N+1)]
    bfsRobot = bfs(robot,table)
    flag = 0
    for i in range(N):
        x,y = trashes[i]
        if not bfsRobot[x][y]:
            flag = 1
            break
        bfsTable[-1][i] = bfsRobot[x][y]

    if flag:
        print(-1)
        continue

    for i in range(N):
        Vnow = bfs(trashes[i],table)
        for j in range(N):
            x,y = trashes[j]
            bfsTable[i][j] = Vnow[x][y]

    perm = list(permutations([i for i in range(N)],N))
    result = 1e9
    for nodes in perm:
        temp = 0
        temp += bfsTable[-1][nodes[0]]-1
        F = nodes[0]
        for node in nodes[1:]:
            T = node
            temp += bfsTable[F][T]-1
            F = node
        result = min(result,temp)

    print(result)