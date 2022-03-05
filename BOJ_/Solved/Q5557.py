from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q5557
#######  TODAY  #######
##### 2022. 03. 05 #####
GIVEN ) N 개의 숫자가 주어질 때, 마지막 두 숫자 사이에 = 를 놓고
        나머지 사이엔 -,+ 을 배치하여 등식이 성립하는 경우의 수를 구하라
        계산과정 중 음수 혹은 20을 초과하는 숫자가 나오는경우는 제외한다
INPUT ) 첫째 줄에 N 이 주어진다 { 3<= N <= 100 }
        둘째 줄에는 0이상 9 이하의 자연수 N 개가 공백으로 구분되어 주어진다
OUTPUT) 만들 수 있는 올바른 등식 경우의 수를 출력하라
Approach ) 이 또한 2차원 dp를 사용해서 풀 수 있다고 한다 
'''
# import sys
# input = sys.stdin.readline

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

# xprint(dp)