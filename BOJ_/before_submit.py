import sys
sys.setrecursionlimit(25000)
input = sys.stdin.readline
dic = {}
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(a)
for i in range(n):
    dic[a[i]] = i
r,c = map(int,input().split())
dp = [[0 for _ in range(c)] for _ in range(r)]
data = []
for _ in range(r):
    data.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        data[i][j] = dic[data[i][j]]

hst = [0]*n
hst[data[0][0]] = 1
d = [[0,1],[0,-1],[1,0],[-1,0]]
C = 1
dp[0][0] = 1
def dfs(now,hist,count):
    global C,dp
    if count > C:
        C = count
    if C == 26:
        return
    x,y = now
    if dp[x][y]<C:
        dp[x][y] = C
    elif dp[x][y]>C:
        return
    for w in range(4):
        nx,ny = x+d[w][0],y+d[w][1]
        if 0<= nx < r and 0<=ny<c:
            nxtnum = data[nx][ny]
            if not hist[nxtnum]:
                hist[nxtnum] = 1
                dfs([nx,ny],hist,count+1)
    hist[data[x][y]] = 0
    return

dfs([0,0],hst,C)
print(C)