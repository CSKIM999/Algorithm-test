from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q11726
#######  TODAY  #######
##### 2022. 03. 09 #####
GIVEN ) 2*n 크기의 타일을 1*2 혹은 2*1 크기 타일로 채우는 경우의 수를 구하라
INPUT ) 첫째 줄에 N 이 주어진다
OUTPUT) 경우의수를 10,007 로 나눈 나머지를 출력하라
Approach )  dp 쓰자
'''
# import sys
# input = sys.stdin.readline

n = int(input())
dp = [i if i<3 else 0 for i in range(n+1)]
for i in range(3,n+1): dp[i]=sum(dp[i-2:i])
print(dp[-1])
