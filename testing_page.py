import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

feed = [[] for _ in range(7)]
shark = [2]
shark_size = shark[0]
result = 0
for i in range(n):
    for j in range(n):
        if data[i][j] != 0 and data[i][j] != 9:
            x = data[i][j]
            feed[x].append((i,j))
        elif data[i][j] == 9:
            shark.append([i,j])



def dfs(now):
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    x,y = now
    dist[x][y] = 0
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<= nx <n and 0<= ny < n:
                if dist[nx][ny] > (dist[x][y]+1) or dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append([nx,ny])

    return dist


def find_next(now):
    temp = 0
    target = []
    for i in feed[1:shark[0]]:
        temp += len(i)
        for j in i:
            target.append([0,j])
    if temp == 0:
        return False
        
    x,y = now
    for i in range(len(target)):
        nx,ny = target[i][1]
        ndist = dfs([x,y])[nx][ny]
        target[i][0] = ndist
    target.sort()

    return target 

# while True:
#     ans = [[1e9]*n for _ in range(n)] 
#     ans[shark[1][0]][shark[1][1]] = 0 
#     temp = find_next(shark[1])
#     if temp == False:
#         break
#     for i in range(7):
#         if temp[0][1] in feed[i]:
#             feed[i].remove(temp[0][1])
#             break
#     data[shark[1][0]][shark[1][1]] = 0
#     result += temp[0][0]
#     shark[1] = temp[0][1]
#     data[shark[1][0]][shark[1][1]] = 9
#     shark_size -=1
#     if shark_size == 0:
#         shark[0] +=1
#         shark_size = shark[0]

# print(result)

print(dfs([2,2]))

