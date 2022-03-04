from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2225
#######  TODAY  #######
##### 2022. 03. 04 #####
GIVEN ) n 가지 종류의 동전이 있고, 각각의 동전의 가치는 다르다. 적절히 사용하여 가치의 합이 k 원이 되도록 하라.
        순서만 다른것은 같은 경우의 수로 취급한다
INPUT ) 첫째 줄에 n,k ( 1<= n <=100, 1<= k <= 10,000 ) 가 주어지고 그 위 n 개줄에 걸쳐 동전의 가치가 주어진다. ( 100,000 이하의 자연수 )
OUTPUT) 경우의 수를 출력하라. 이는 2^31 보다 작다
Approach )  DP 를 통해 다음 플로우차트를 따라보자
            1. 동전을 순회한다 < 중복을 피하기 위함
                1.1 현재 동전만으로 가능한 포인트들을 모두 +1 해준다
                1.2 현재 동전크기+1 부터 k 까지 순회하며 dp를 채운다


            
'''
# import sys
# input = sys.stdin.readline


n,k = map(int,input().split())
C = []
for i in range(n):
    x = int(input())
    if x > k:
        continue
    C.append(x)

if C:
    dp = [0 for _ in range(k)]

    for CVal in C:
        dp[CVal-1] += 1
        for Node in range(CVal,k):
            dp[Node] += dp[Node-CVal]
    print(dp[k-1])
else:
    print(0)
