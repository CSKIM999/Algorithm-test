import sys
from collections import deque
input = sys.stdin.readline

n,K = map(int,input().split())
data = [[] for _ in range(n)]
virus =[]
for i in range(n):
    data[i] = list(map(int,input().split()))
    for j in range(n):
        if data[i][j] !=0:
            virus.append([data[i][j],0,i,j])
s,X,Y = map(int,input().split())
virus.sort()
q = deque(virus)


while q:
    a,time,x,y = q.popleft()
    if time == s:
        break
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if -1<nx<len(data) and -1<ny<len(data):
            if data[nx][ny] == 0:
                data[nx][ny] = a
                q.append([a,time+1,nx,ny])


print(data[X-1][Y-1])