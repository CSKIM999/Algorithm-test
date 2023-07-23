n = int(input())
data = list(map(int,input().split()))

dp = [1 for _ in range(n)]
for i in range(n):
    now = data[i]
    for j in range(i+1,n):
        if data[j] < now:
            dp[j] = max(dp[i] + 1,dp[j])
print(max(dp))