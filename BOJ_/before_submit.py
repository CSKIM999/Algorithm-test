import sys
input = sys.stdin.readline
sys.setrecursionlimit(25000)
n,m = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
dd = [[1,0],[0,1],[-1,0],[0,-1]]
def dfs(now):
    global dp
    x,y = now
    if now == [n-1,m-1]:
        return True

    nowValue = data[x][y]
    for i in range(4):
        nx,ny = x+dd[i][0],y+dd[i][1]
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny] < nowValue:
                dp[nx][ny] += 1
                dfs([nx,ny])
    if (now != [n-1,m-1]) and (now != [0,0]):z
        count = 0
        for j in range(4):
            nx,ny = x+dd[j][0],y+dd[j][1]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny] < nowValue and dp[nx][ny] >= 0:
                    count += 1
        if not count:
            dp[x][y] = -1

dfs([0,0])
print(dp[-1][-1])