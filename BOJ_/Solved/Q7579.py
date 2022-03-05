from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q7579
#######  TODAY  #######
##### 2022. 03. 05 #####
GIVEN ) N 개의 앱이 활성화 되어있고, M 만큼의 데이터를 확보하고자 한다.
        각 앱이 차지하는 메모리는 mi 와 같고, 비활성화 시 낭비되는 비용은 ci 이다
        M 만큼 확보를 위해 소모되는 최소비용을 계산하여 출력하라
INPUT ) 첫째 줄은 N,M 이 공백을 구분으로 주어진다 
        { 1 <= N <= 100 and 1 <= M <= 10,000,000 }

        둘째 줄에는 현재 활성화 되어있는 앱이 차지하는 메모리 mi 가 공백을 구분으로 주어진다.
        { 1 <= mi <= 10,000,000 }

        셋째 줄에는 각 앱의 비활성화 시 비용 ci 가 주어진다.
        { 1<= ci <= 100 }

        단, M <= Sigma(mi) 를 항상 만족한다
OUTPUT) M 바이트 확보를 위한 최소비용을 출력하라
Approach ) 2차원 dp 를 사용해야한다고 함

'''
# import sys
# input = sys.stdin.readline

n,m = map(int, input().split())
mv = list(map(int,input().split()))
ml = list(map(int,input().split()))
q = sum(ml)
dp = [[0 for _ in range(q)] for _ in range(n+1)]
result = q
for i in range(1,n+1):
    value,loss = mv[i-1],ml[i-1]
    for j in range(q):
        if j<loss:
            dp[i][j] = dp[i-1][j]
        elif j >= loss:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-loss]+value)
        
        if dp[i][j]>=m:
            result = min(result,j)
print(result)