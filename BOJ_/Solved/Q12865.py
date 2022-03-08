from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q12865
#######  TODAY  #######
##### 2022. 03. 08 #####
GIVEN ) 준서는 여행에 N 개의 물건을 가져가고자 한다.
        각 물건은 무게 W 와 가치 V 를 가지며 물건을 배낭에 넣어가면 준서가 V 만큼 즐길 수 있다
        준서는 최대 K 만큼의 무게를 들 수 있을 때 가져갈 수 있는 최대의 V 를 구하라
INPUT ) 첫째 줄에 물품의 수 N ( 1<= N <= 100)과, 버틸 수 있는 무게 K ( 1<= K <= 100,000 ) 가 주어진다
        둘째 줄부터 N 개의 줄에 걸쳐 물건의 무게 W ( 1<= W <= 100,000 )와 해당 물건의 가치 V ( 0 <= V <= 1,000 ) 이 주어진다
OUTPUT) 가치합의 최댓값을 출력하라 
Approach ) 많이 봤던 냅색문제다 혼자 한번 풀어보자  
'''
# import sys
# input = sys.stdin.readline

N,K = map(int,input().split())
item = []
for i in range(N):
    item.append(list(map(int,input().split())))
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
result = 0
for i in range(1,N+1):
    w,v = item[i-1]
    for j in range(1,K+1):
        if j>=w:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
        # dp[i][j]=max()
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j]>result:
            result = dp[i][j]
    pass

print(result)

'''
****** b4 code ******

N,K = 4,7
get = [
    [4, 7],
    [6 ,13],
    [4, 8],
    [3, 6],
    [5 ,12]
]
W = [0 for x in range (N+1)]
V = [0 for x in range (N+1)]
DP = [[0 for x in range(K+1)] for x in range (N+1)]
for x in range (1,N+1) :
    W[x],V[x] = get[x]

print(W,V)
for i in range (1,N+1) : #만족도인덱스
    for j in range (1,K+1) : #크기인덱스
        if j >= W[i] :
            print(f'i : {i} && j : {j}')
            print(f'V[i] : {V[i]} ***&*** DP[i][j-W[i]] : {DP[i][j-W[i]]} ***&*** DP[i-1][j] : {DP[i-1][j]}')
            DP[i][j] = max(V[i]+DP[i][j-W[i]],DP[i-1][j])
            print(f'{W} :: W')
            print(f'{V} :: V')
            xprint(DP)
            print()
        else :
            DP[i][j] = DP[i-1][j]
            

print(f'{W} :: W')
print(f'{V} :: V')
xprint(DP)
'''