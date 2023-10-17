ipt = []
n = int(input())
for _ in range(n):
    ipt.append(int(input()))
M = max(ipt)
dp = [0]*(M+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

if M >=4:
    for i in range(4,M+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009
for i in ipt:
    print(dp[i])