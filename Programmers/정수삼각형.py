tri = [[7]]
dp = [tri[0][0]]


for i in tri[1:]:
    temp = dp + [0]
    for j in range(len(dp)):
        temp[j] = max(temp[j],i[j]+dp[j])
        temp[j+1] = max(temp[j+1],i[j+1]+dp[j])
    dp = temp[:]

print(max(dp))

'''
1회차 > 구상이 귀찮지 구현은 매우쉽다 스무스하게 패스
'''