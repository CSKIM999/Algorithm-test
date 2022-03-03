from lib import xprint
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
'''

import sys
import heapq
input = sys.stdin.readline


n,k = map(int,input().split())
J = []
JT = [False * n]
for i in range(n):
    a = list(map(int,input().split()))
    a.append(i)
    J.append(a)
c = []
for i in range(k):
    a = int(input())
    c.append((i,a))
heapq.heapify(J)
heapq.heapify(c)
print(heapq.heappop(J))
print(c)