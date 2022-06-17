from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1976
#######  TODAY  #######
##### 2022. 06. 17 #####
GIVEN ) 임의의 도시로 여행을 떠나고자 한다.
        각각의 도시에는 간선이 있을수도, 없을수도 있다. 여행일정이 주어질 때
        여행의 가능여부를 판별하는 프로그램을 작성하라
        같은 도시를 여러번 방문해도 문제없다.
INPUT ) 첫째 줄에 도시의 수 N 이 주어진다. ( 1<= N <= 200 )
        둘째 줄에 여행계획에 속한 도시의 수 M 이 주어진다. ( 1<= M <= 1,000 )
        다음 N 개의 줄에 N 개의 정수가 주어진다.
        마지막 줄에는 여행 계획이 주어진다.
OUTPUT) 가능하다면 YES 불가능하다면 NO 를 출력하라
Approach ) N 이 200 이어서 플로이드워셜을 사용할까 싶었지만, 결국 최단거리가 아니라 여행가능여부이므로
           시작노드에서 모든 노드로 도착할 수만 있다면 그만인듯하다.
           따라서 다익스트라 알고리즘을 사용해볼것
'''



import sys
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
inf = 1e9

N = int(input())
M = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))
path = list(map(int,input().split()))
start = path[0]-1
dist = [inf]*N
dist[start] = 0
q = []
hpush(q,(0,start))

while q:
    c,node = hpop(q)
    if c>dist[node]:
        continue
    for i in range(N):
        if c+1<dist[i] and data[node][i]:
            hpush(q,(c+1,i))
            dist[i] = c+1

flag = 0
for i in path:
    i -=1
    if dist[i] == inf:
        flag = 1
        print('NO')
        break
if not flag:
    print('YES')

'''
다 잘해놓고 line 59  break 을 안걸어줘서 출력오류를 고려 못함
아무튼 다익스트라 좋고 어쨋든 가면되는 판단도 좋았던것같음.

'''