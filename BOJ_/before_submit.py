import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
data = [[[] for _ in range(N)] for _ in range(N)]
light = [[False for _ in range(N)] for _ in range(N)]
light[0][0] = True
d = [[1,0],[-1,0],[0,1],[0,-1]]
Vnode = []
for i in range(M):
    x,y,a,b = map(int,input().split())
    data[x-1][y-1].append([a-1,b-1])
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

print(result)