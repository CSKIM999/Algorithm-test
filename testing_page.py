import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))


# n = 20
# data = [
#     [4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1],
#     [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
#     ]

shark = [2]
result = 0
shark_size = 2
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark.append((i,j))
            data[i][j] = 0

            

def find(array,shark):
    x,y=0,0
    min_val = 500
    for i in range(n):
        for j in range(n):
            if array[i][j] != -1 and 1<=data[i][j]<shark[0]:
                if array[i][j] < min_val:
                    x,y = i,j
                    min_val = array[i][j]
    
    if min_val == 500:
        return False
    return [min_val,[x,y]]

def bfs(data,shark):
    n = len(data)
    dist = [[-1]*n for _ in range(n)]
    q = deque()
    q.append(shark[1])
    dist[shark[1][0]][shark[1][1]] = 0
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i] , y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n and data[nx][ny] <= shark[0]:
                if dist[nx][ny] > (dist[x][y]+1) or dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append([nx,ny])

    return dist

while True:
    ans = find(bfs(data,shark),shark) 
    # 움직일 때 바뀌어야 할 것
    # 1. 먹이리스트 갱신 2. 상어위치 갱신 3. 상어있던자리 비우기 4.현재시간 5.상어크기카운트
    if ans == False:
        break
    result += ans[0] # 4
    nx,ny = ans[1]
    data[nx][ny] = 0 # 2
    shark_size -=1
    shark[1] = (nx,ny)
    if shark_size == 0:
        shark[0] +=1
        shark_size = shark[0]

print(result)