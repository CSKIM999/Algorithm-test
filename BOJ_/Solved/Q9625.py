dp = [[0,1,1],[1,1,2]]
num = int(input())

if num < 3:
    print(dp[0][num-1],dp[1][num-1])
else:
    dp[0].extend([0]*47)
    dp[1].extend([0]*47)
    for i in range(3,num):
        dp[0][i] = dp[0][i-1]+dp[0][i-2]
        dp[1][i] = dp[1][i-1]+dp[1][i-2]
    print(dp[0][num-1],dp[1][num-1])
    temp = 0
    for i in dp[1]:
        temp += i
    print(temp
    )
'''
도와주려고 실5따리 풀었더니만 배은망덕한 쉑
'''