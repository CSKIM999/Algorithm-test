import sys
input = sys.stdin.readline
n,K = map(int,input().split())
virus = [[] for _ in range(K)]
data = [[] for _ in range(n)]
for i in range(n):
    data[i] = list(map(int,input().split()))
s,X,Y = map(int,input().split())

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            x = data[i][j]
            virus[x-1] = [[i,j]]

def expand(n,K,data,k):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(K):
        num = len(k[i])
        for l in range(num):
            x,y = k[i][l]
            for j in range(4):
                nx = x+dx[j]
                ny = y+dy[j]
                if -1<nx<n and -1<ny<n:
                    if data[nx][ny] ==0 and [nx,ny] not in k[i]:
                        data[nx][ny] = i+1
                        k[i].append([nx,ny])
    
    return data,k

for _ in range(s):
    data, k =expand(n,K,data,virus)
    
print(data[X-1][Y-1])