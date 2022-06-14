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
# input = sys.stdin.readline

N,M = map(int,input().split())
data = [[[] for _ in range(N)] for _ in range(N)]
light = [[0 for _ in range(N)] for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
light[0][0] = visit[0][0] = 1
d = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(M):
    x,y,a,b = map(int,input().split())
    data[y-1][x-1].append([b-1,a-1])

q =deque([[0,0]])

while q:
    x,y = q.popleft() #방문 노드

    for node in data[x][y]: #현재 방문한 방에서 킬 수 있는 스위치들
        lx,ly = node #스위치 방들의 좌표
        light[lx][ly] = 1 #방 안의 모든스위치 키기

        if not visit[lx][ly]: #불을 킨 방을 방문하지 않았는가?
            flag = 0

            for i in range(4): #이번에 불을 킨 노드가 방문이 가능한 노드라면 q에 삽입
                nx,ny = lx+d[i][0], ly+d[i][1] 

                if 0<=nx<N and 0<=ny<N and visit[nx][ny]: #만약 주변에 접근 가능한 방이 있다면
                    flag = 1
                    break
            if flag:
                visit[lx][ly] = 1
                q.append([lx,ly]) #방문 가능한 방이므로 q에 추가해주기

    for i in range(4):
            nx,ny = x+d[i][0], y+d[i][1] 
            if 0<=nx<N and 0<=ny<N and light[nx][ny] and not visit[nx][ny]: 
                q.append([nx,ny])
                visit[nx][ny] = 1

result = 0 
for i in range(N):
    for j in range(N):
        result += light[i][j]

print(result)


'''
문제 자체는 어렵지 않은 반면에, 테스트케이스가 존내 까다로웠음.

이상하게 안맞아서 보니까 line 55 의 nxny 를 xy 가 아닌 lxly 로 돌리고있었음 븅신같이
'''