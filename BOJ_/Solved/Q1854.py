import sys
from heapq import *
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1854
#######  TODAY  #######
##### 2023. 03. 03 #####
GIVEN ) A에서 B로 향할때, K 번째로 짧은 경로의 길이를 탐색하라.
        도시의 개수 n 과 간선의 개수 m 이 주어진다
INPUT ) 첫째 줄에 n,m,k 가 주어진다. ( 0<=n<=1,000 && 0<=m<=2,000,000 && 1<=k<=100 )
        이후 m 개의 줄에 걸쳐 a,b,c 가 주어진다 ( 1 <= a,b<= n && 0 <= c <= 1,000)
        도시의 번호는 n까지 연속되며, 1번도시는 항상 시작도시이다.
OUTPUT)  n 개의 줄을 출력하라. 각 줄의 의미는 1번 도시에서 i번 도시까지의 k번째 최단거리를 의미한다.
Approach ) 다익스트라 돌리면서 해당 노드 방문할때마다 해쉬리스트에 저장하기?  
'''
# import sys
# input = sys.stdin.readline
n, m, k = map(int, input().split())
dic = {i: [[1e9]*k, set()] for i in range(n+1)}
dic[1][0][0] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dic[a][1].add((b, c))

h = []
# for b, c in dic[1][1]:
#     dic[b][0][k-1] = c
#     dic[b][0].sort()
heappush(h, [0, 1])
while h:
    cost, to = heappop(h)
    for b, c in dic[to][1]:
        if dic[b][0][k-1] > cost+c:
            dic[b][0][k-1] = cost+c
            dic[b][0].sort()
            heappush(h, [cost+c, b])

for i in range(1, n+1):
    if dic[i][0][k-1] == 1e9:
        print(-1)
    else:
        print(dic[i][0][k-1])

'''
아이디어를 좀 참고하긴 했으나 다익스트라 감 다시잡기 좋았음.
'''
