n = 5
money = [1, 2, 5]
# answer ---- 4
l = len(money)

dp = [[0]*(n+1) for _ in range(l+1)]

for i in range(l):
    token = money[i]
    i += 1
    for j in range(n+1):
        dp[i][j] += dp[i-1][j]
        if token == j:
            dp[i][j] += 1
        elif j > token:
            dp[i][j] += dp[i][j-token]

[print(i) for i in dp]
'''
개같은 냅색 ship것
'''
