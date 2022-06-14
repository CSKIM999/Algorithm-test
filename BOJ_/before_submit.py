import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
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