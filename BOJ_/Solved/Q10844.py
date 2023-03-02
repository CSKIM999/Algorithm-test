import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q10844
#######  TODAY  #######
##### 2023. 03. 02 #####
GIVEN ) 쉬운계단수.
        12345 // 12323 과 같이 각 자리의 차이가 1인 수를 계단수라 한다.
        자리수 N 이 주어질 때 만들 수 있는 경우의 수를 구하라
INPUT ) 100 이하의 자연수 N 이 주어진다. 
OUTPUT) 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다. 
Approach )  dp 테스트

'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [1 if i > 0 else 0 for i in range(10)]
f = 0
for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j+1]+dp[i-1][j-1]

print(sum(dp[-1]) % 1000000000)
