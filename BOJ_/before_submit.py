import sys
input = sys.stdin.readline

N,K = map(int,input().split())
item = []
for i in range(N):
    item.append(list(map(int,input().split())))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
result = 0
for i in range(1,N+1):
    w,v = item[i-1]
    for j in range(1,K+1):
        if j>=w:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
        # dp[i][j]=max()
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j]>result:
            result = dp[i][j]
    pass

print(result)