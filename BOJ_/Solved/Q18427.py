from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q18427
#######  TODAY  #######
##### 2022. 06. 14 #####
GIVEN ) N명의 학생이 최대 M 개의 블럭을 갖고 H높이의 탑을 쌓고자 한다.
        높이가 정확히 H인 탑을 만들 수 있는 경우의 수를 계산하라
INPUT ) 첫째 줄에 N,M,H 가 공백을 기준으로 주어진다.
        ( 1<= N <= 50, 1<= M <= 10, 1<= H <= 1,000)
        둘째 줄부터 각 학생이 가진 블럭의 높이가 공백을 기준으로 주어진다.
OUTPUT) H 높이의 탑을 만드는 경우의 수를 10,007로 나눈 나머지를 출력하라
Approach )  냅색 알고리즘을 사용하되, 데이터 처리가 관건일듯
            풀어보니 변환냅색으로 풀이 가능할 듯함

            N1 = set(0,1,2) , N2= set(2,3) . . .

            +=======================+
            | X | 1 | 2 | 3 | 4 | 5 |
            +=======================+
            | N0| 0 | 0 | 0 | 0 | 0 |
            +=======================+
            | N1| 0 | 0 | 0 | 0 | 0 |
            +=======================+
            | N2| 0 | 0 | 0 | 0 | 0 |
            +=======================+
            | N3| 0 | 0 | 0 | 0 | 0 |
            +=======================+
'''
import sys
input = sys.stdin.readline


N, M, H = map(int, input().split())
data = []
for i in range(N):
    data.append(set(map(int, input().split())))

dp = [[0]*H for _ in range(N+1)]

#학생들 N 순환
for i in range(N):
    
    node = data[i]
    i += 1
    # dp 최대높이까지 순환 1~H
    for j in range(H):
        dp[i][j] += dp[i-1][j]

        #현재 높이의 노드를 만들수있는가?
        for k in node:
            # H 가 지금 가진 블럭보다 크거나 같다
            if j+1 > k:
                dp[i][j] += dp[i-1][j-k]
            elif j+1 == k:
                dp[i][j] += 1

print(dp[-1][-1]%10007)

'''
dp도 나름 좀 익숙해진듯?
'''