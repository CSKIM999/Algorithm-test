'''
ACAYKP
CAPCAK
'''
a = list(input())
b = list(input())
al = len(a)
bl = len(b)
dp = [[0 for _ in range(al+1)] for _ in range(bl+1)]

for i in range(1,bl+1):
    x = b[i-1]
    for j in range(1,al+1):
        y = a[j-1]
        if y == x:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])