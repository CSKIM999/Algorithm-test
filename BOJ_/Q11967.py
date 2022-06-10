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
def lightOn(get):
    LQ = deque(get)
    while LQ:
        lx,ly = LQ.popleft()
        light[lx][ly] = True

def bfs(): #항상 0,0 에서 시작해서 퍼져나가자.
    global light,Vnode
    Vlst = []
    q = deque()
    res = []
    q.append([0,0])
    Vlst.append([0,0])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+d[i][0],y+d[i][1]
            if 0<= nx< N and 0<= ny < N and [nx,ny] not in Vlst:

                if light[nx][ny]:
                    q.append([nx,ny])
                    Vlst.append([nx,ny])

                    if [nx,ny] not in Vnode and data[nx][ny]:
                        for lx,ly in data[nx][ny]:
                            res.append([lx,ly])
                        Vnode.append([nx,ny])
    return res
lightOn(data[0][0])
xprint(light)
print(bfs())

