import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q5582
#######  TODAY  #######
##### 2023. 03. 02 #####
GIVEN ) 공통부분문자열
INPUT ) 첫째 둘째줄에 두개의 4000자 이하의 문자열이 주어진다 
OUTPUT) 최대공통부분문자열의 길이를 출력하라 
Approach )  dp
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

a = list(input())
b = list(input())
na, nb = len(a), len(b)
dp = [[0]*(nb+1) for _ in range(na+1)]
res = 0
for i in range(1, na+1):
    for j in range(1, nb+1):
        if b[j-1] == a[i-1]:
            now = dp[i-1][j-1]+1
            dp[i][j] = now
            res = max(now, res)
print(res)
