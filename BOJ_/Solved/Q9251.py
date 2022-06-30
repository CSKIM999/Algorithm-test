from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q9251
#######  TODAY  #######
##### 2022. 06. 25 #####
GIVEN ) LCS ( Longest Common Subsequence ) // L--- Substring 과는 다름.
        ACAYKP 와 CAPCAK 의 LCS 는 ACAK 가 된다.
INPUT ) 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로 이루어져있으며, 최대 1000글자이다.
OUTPUT) 두 문자열의 LCS 길이를 출력하라
Approach )  LCS 알고리즘 연습해보기
길이가 긴 문자열을 비교대상문자열 A, 짧은 문자열을 비교문자열 B로 사용하자
for i in B
    for j in A
        if i == 0 or j == 0
            dp[i][j] = 0
            
        elif i == j:
            now = dp[i-1][j-1] + 1
        
        else:
            now = max(dp[i-1][j],dp[i][j-1])
        

'''


import sys
input = sys.stdin.readline
sys.setrecursionlimit(25000)
X = list(input().strip())
Y = list(input().strip())
x,y = len(X),len(Y)

if x==y:
    A,B = X,Y
elif x<y:
    A,B = Y,X
else:
    A,B = X,Y
dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for i in range(len(B)):
    b = B[i]
    for j in range(len(A)):
        a = A[j]
        if a==b:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

print(dp[-1][-1])