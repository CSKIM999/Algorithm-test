'''
5
1 10
1 10
1 10
1 10
1 10
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
for i in range(n):
    req, value = arr[i]
    if req+i > n:
        continue
    dp[req+i] = dp[i]+value

print(max(dp))
