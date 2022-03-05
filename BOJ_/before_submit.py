import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
dp = [[0 for i in range(21)] for _ in range(N-1)]
dp[0][nums[0]] = 1
for i in range(1,N-1):
    now = nums[i]
    for j in range(21):
        if dp[i-1][j]:
            if 0<=j+now<=20:
                dp[i][j+now] += dp[i-1][j]
            if 0<=j-now<=20:
                dp[i][j-now] += dp[i-1][j]
print(dp[-1][nums[-1]])