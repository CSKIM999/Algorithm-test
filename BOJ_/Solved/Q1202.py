from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ 1202
#######  TODAY  #######
##### 2022. 03. 01 #####
GIVEN ) 보석점에는 보석이 N 개 존재하며 보석은 각각 무게 M, 가치 V 를 가진다
        가방에는 오직 한개의 보석만 C 이하의 무게일 때 넣을 수 있으며, K 개 가지고있다

INPUT ) 첫째 줄에 N,K 가 주어진다 ( 1 <= N, K <= 300,000 )
        다음 N 개의 줄에 각 보석의 정보 M,V 가 주어진다. ( 0 <= M,V <= 1,000,000 )
        다음 K 개의 줄에 가방에 담을 수 있는 최대무게 C 가 주어진다. ( 1 <= C <= 100,000,000)

OUTPUT) 훔칠 수 있는 보석 가격 합의 최대를 출력하라

Approach ) 난이도가 없었으면 단순히 가장 비싼 물품부터 넣고자 시도했을 것 그 방법으로 해보자
            2중 for 문은 시간초과가 남. 두번째 for 문을 이분탐색으로 해볼까 함
            이분탐색도 시간초과가 난다고 함. 내 생각에 해봐야 300,000*log2(300,000) 해봐야 580만 케이스 아닌가 싶은데
            
'''
import heapq

# import sys
# input = sys.stdin.readline


n,k = map(int,input().split())
J = []
bP = []
for i in range(n):
    heapq.heappush(J,list(map(int,input().split())))
    
for i in range(k):
    a = int(input())
    heapq.heappush(bP,a)

bP.sort()
print(J)
result = 0
temp = []
for i in bP:
    while J and i >= J[0][0]:
        heapq.heappush(temp, -heapq.heappop(J)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not J:
        break
print(result)