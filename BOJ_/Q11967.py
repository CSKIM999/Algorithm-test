from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q11967
#######  TODAY  #######
##### 2022. 06. 10 #####
GIVEN ) N*N 크기의 헛간 안에 (1<= N <= 100) 불이 꺼진 방들이 존재한다.
        나는 최대한 많은 방의 불을 키고싶어하며 방 안의 스위치로 지정된 방의 불을 킬 수 있다.
        나는 오로지 불이 켜진, 상하좌우에 인접한 방에만 들어갈 수 있을 때 최대한 킬수 있는 방의 수를 구하라
INPUT ) 첫째 줄에 N 과 M 이 정수로 주어진다 ( 1 <= M <= 20,000 ) 
        다음 M 개의 줄에 x,y,a,b 가 주어지며 (x,y) 방에서 (a,b) 방의 불을 키는 스위치가 존재한다는 뜻
OUTPUT) 최대 개수를 구하라 
Approach ) 불키기와 탐색을 나눠서 해야할듯
            불키기는 딕셔너리로 만들고
            탐색은 visited 리스트 bfs 로 관리하자 해봐야 만개
'''
import sys
from collections import deque
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

N,M = map(int,input().split())
data = [[[] for _ in range(N)] for _ in range(N)]
light = [[False for _ in range(N)] for _ in range(N)]
light[0][0] = True
d = [[1,0],[-1,0],[0,1],[0,-1]]
Vnode = []
for i in range(M):
    x,y,a,b = map(int,input().split())
    data[x-1][y-1].append([a-1,b-1])

def bfs4route(node,hist):
    sx,sy = node
    ret = []

    sq = deque()
    sq.append([sx,sy])
    shist = []
    while sq:
        sx,sy = sq.popleft()
        for i in range(4):
            nsx,nsy = sx+d[i][0], sy+d[i][1]
            if 0<=nsx<N and 0<=nsy<N and light[nsx][nsy]:
                if [nsx,nsy] not in shist and [nsx,nsy] not in hist:
                    ret.append([nsx,nsy])
                    sq.append([nsx,nsy])
                    shist.append([nsx,nsy])
    
    return ret
result = 1
hist = []
q =deque([[0,0]])

while q:
    x,y = q.popleft()
    if [x,y] not in hist:
        hist.append([x,y])
    data[x][y].sort()
    for node in data[x][y]: #현재 방문한 노드에서 불을 킨 노드
        lx,ly = node
        if not light[lx][ly]: #아직 불이 켜지지않은 노드라면
            light[lx][ly] = True
            result += 1
            flag = False
            for i in range(4): #이번에 불을 킨 노드가 방문이 가능한 노드라면 q에 삽입
                if not flag:
                    nx,ny = lx+d[i][0], ly+d[i][1]
                    if [nx,ny] in hist and not flag:
                        flag = True
                        q.append([lx,ly])
                        hist.append([lx,ly])
                        bfs = bfs4route([lx,ly],hist)
                        for sn in bfs:
                            q.append(sn)

# route = deque()
# route.append([0,0])
# res = 0
# Rhist = set()
# while route:
#     x,y = route.popleft()
#     res += 1
#     for i in range(4):
#         nx,ny = x+d[i][0], y+d[i][1]
#         if 0<=nx<N and 0<=ny<N and light[nx][ny]:
#             route.append([nx,ny])
#             Rhist.add([nx,ny])
xprint(light)
print(result)




###################################################
###################################################
###################################################


# def lightOn(get):
#     global result
#     LQ = deque(get)
#     while LQ:
#         lx,ly = LQ.popleft()
#         if not light[lx][ly]:
#             light[lx][ly] = True
#             result += 1
#             # if data[lx][ly]:
#             #     for x in data[lx][ly]:
#             #         LQ.append(x)
                    

# def bfs(): #항상 0,0 에서 시작해서 퍼져나가자.
#     global light
#     q = deque()
#     res = []
#     q.append([0,0])
#     if [0,0] not in Vnode and data[0][0]:
#         for lx,ly in data[0][0]:
#             res.append([lx,ly])
#         Vnode.append([0,0])
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx,ny = x+d[i][0],y+d[i][1]
#             if 0<= nx< N and 0<= ny < N and [nx,ny] not in Vnode:

#                 if light[nx][ny]:
#                     q.append([nx,ny])
#                     Vnode.append([nx,ny])

#                     if [nx,ny] not in Vnode and data[nx][ny]:
#                         for lx,ly in data[nx][ny]:
#                             res.append([lx,ly])
#                         Vnode.append([nx,ny])

#     return res

# while True:
#     nodes = bfs()
#     if not nodes:
#         break
#     lightOn(nodes)

# print(result)