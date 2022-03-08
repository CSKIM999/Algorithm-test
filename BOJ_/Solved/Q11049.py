from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q11049
#######  TODAY  #######
##### 2022. 03. 07 #####
GIVEN ) 순서가 정해진 행렬이 주어진다.
        행렬을 곱연산 할 때 일정 비용이 발생한다. 예를들어 2*3 행렬과 3*9 행렬을 곱할경우의 비용의 계산은 다음과 같다.
        ex ) 2*3*9 = 72
        하지만 이는 곱셈을 하는 순서에따라 최종비용이 변하게 된다.
        예를 들어, A의 크기가 5*3이고, B의 크기가 3*2, C의 크기가 2*6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.
            AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5*3*2 + 5*2*6 = 30 + 60 = 90번이다.
            BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3*2*6 + 5*3*6 = 36 + 90 = 126번이다.
        따라서 행렬의 순서는 바꾸지 않고, 곱셈의 순서를 정하는 방법으로 곱셈 비용의 최솟값을 반환하라
INPUT ) 첫째 줄에 행렬의 수 N 이 주어진다.
        둘째 줄부터 N 번째 줄까지 행렬의 크기가 주어진다.
        항상 순서대로 곱셈이 가능한 값만 주어진다
OUTPUT) 곱연산 비용의 최솟값을 반환하라

Approach )  Q11066 과 거의 같은 문제인듯하다
            행렬을 곱하면 앞의 행과 뒤의 열 이 남아서 순서대로만 진행한다면 그룹화문제와 같다.
            실습하는 차원에서 2차원 리스트를 작성해서 완성해보자



'''
# import sys
# input = sys.stdin.readline


# N = int(input())
# mat = []
# for i in range(N):
#     mat.append(list(map(int,input().split())))
# dp = [[[0,[0,0]] for _ in range(N+1)] for _ in range(N+1)] # 최소비용과 결과 행렬곱

# for i in range(1,N+1):#묶는 덩어리크기 1~5
#     for j in range(1,N+2-i): #시작노드 1~ 2+(5-i)
#         if i == 1:
#             dp[j][j] = [0,[mat[j-1][0],mat[j-1][1]]]
#             continue
#         temp = []
#         for k in range(i-1):
#             left,down = dp[j][j+k],dp[j+k+1][j+i-1]
#             temp.append([left[0] + down[0] + (left[1][0]*down[1][0]*down[1][1]) , [left[1][0],down[1][1]]])
#         dp[j][j+i-1] = min(temp)
# result = dp[1][N]
# print(result[0])
'''
1회차 코드 .... 시간초과 판정을 받았다. 크누스최적화로는 불가능하다고 한다. 씨부럴
                
'''
N = int(input())
mat = []
for i in range(N):
    mat.append(list(map(int,input().split())))

maxcal = 2**32
dp = [[0 for _ in range(N)] for _ in range(N)] # 최소비용과 결과 행렬곱
for i in range(1,N):#묶는 덩어리크기 2~3
    for j in range(N-i): #시작노드 1~ 2+(5-i
        dp[j][j+i] = maxcal
        for k in range(j,j+i): #i = 1, j = 0,1 now 1 , k = 1
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][i+j]+mat[j][0]*mat[k][1]*mat[i+j][1])
print(dp[0][-1])


'''
2회차 > 3번째 for 문 k 를 동적할당할 수 있게 range를 j와 j+i 로 설정하면 가능하다 행렬의 특징을 활용하여 값을 더하였음
'''