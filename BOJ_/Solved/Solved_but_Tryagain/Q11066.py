from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
''' 
BOJ_ QuestionNumber __ Q11066
#######  TODAY  #######
##### 2022. 03. 07 #####
GIVEN ) 여러 챕터의 소설을 임의의 순서로 합쳐서 한 개의 책으로 엮으려 한다
        {{{{{ 단 ,, 양 옆으로 인접한 챕터만 합칠 수 있다. }}}}}
        각 챕터는 합칠 때 각각의 크기를 더한 만큼의 비용이 발생한다. 임의의 순서로 합칠 때 최소비용을 구하라
INPUT ) 첫째 줄에 테스트케이스의 수 T 가 주어진다
        각 테스트케이스의 첫째 줄에는 챕터의 수 K ( 3<= K <= 500 )
        둘째 줄에는 1장부터 K 장까지의 각각의 크기가 공백을 구분으로 주어진다
OUTPUT) 각 테스트케이스마다 합치는데 필요한 최소비용을 출력하라
Approach )  찾아봤다. 이것 역시 2차원 DP 를 사용하면 쉽게 풀 수 있었다.
            다만, 냅색 알고리즘과 다른 누적합을 사용하는 DP문제이다. 그룹화 하는 DP 문제에서 사용할 수 있을 듯 하다

'''
import sys
input = sys.stdin.readline



T = int(input())

for _ in range(T):
    l = int(input())
    nodes = list(map(int,input().split()))
    stack = [0 for i in range(len(nodes)+1)]
    for i in range(1,len(stack)):
        stack[i] = stack[i-1]+nodes[i-1]
    result = sum(stack)

    dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
    dp[0] = stack
    for i in range(2,1+l): # 덩어리크기
        for j in range(1,l-i+2): #시작 노드
            temp = []
            for k in range(i-1):
                temp.append(dp[j][j+k] + dp[j+k+1][j+i-1])
            dp[j][j+i-1] = min(temp) + (dp[0][j+i-1]-dp[0][j-1])#누적합 더하기
    result = dp[1][l]            
    print(f"{result}")
