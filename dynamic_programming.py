from collections import deque
from functools import partial, partialmethod
import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

############################################ 일개미의 식량훔치기 ############################################
'''
어려운데 어쨌든간에 다이나믹 프로그래밍을 통해 수식화했다
과연 해당 문제가 나왔을 때 다음과 같은 알고리즘을 생각해 낼 수 있을지는 의문이다.

그러므로 일단 다음 알고리즘에 대한 자세한 설명을 적어놓고자 함

>>>> 가장 많이 훔치기 위한 알고리즘으로 해당 문제에선 가장 왼쪽에서부터 최선의 선택을 한다는 방법을 적용
** d[i] 에서 훔치기 위해선 d[i-1] 에선 훔치지 못함. 따라서 d[i] 에서의 최선의 선택을 위해선 오직 << d[i-1]와 d[i-2] >> 가 필요
** 다이나믹 프로그래밍의 조건에서는 [ 1) 큰 문제를 작은문제로 나눌 수 있다. 2) 작은 문제의 해답은 큰 문제에서도 공유된다] 였다.
** 따라서 다음 문제는 다이나믹 프로그래밍을 적용시킬 수 있는 문제로 판단된다.

>> 1 . 빈 리스트 d를 생성한다. 그리고 기본적으로 d[0] 와 d[1] 을 해당 조건에 맞춰 선언한다.
>> 2 . for 문을 통해 d[2] 부터 구하고자하는 d[n] 까지 array[i] + d[i-1] 와 d[i-2] 중 큰 값을 d[i] 에 삽입한다
'''

# n=13

# array = [1,3,1,5,300,5,1,8,51,31,25,46,5]
# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0],array[1])
# for i in range(2,n):
#     d[i] = max(d[i-1],d[i-2]+array[i])

# print(d[n-1])


############################################ 효율적인 화폐의 구성 ############################################
'''
이번 문제는 1번 문제였던 그리디알고리즘만으로는 풀어낼 수 없는 문제이다. 만약 동전이 2,3,5 로 주어지고 11을 만들어야한다고 가정하자.
그리디 알고리즘에 따르면 5를 2번 뺀 1이 남아서 만들 수 없다는 대답이 나오겠지만 최선의 해답은 5 한번 3 두번 빼서 만드는 총 3번에 걸친 계산값이다.

따라서 이번 문제 또한 다이나믹 프로그래밍을 사용해서 해석해보자.
앞선 문제와 같이 1부터 시작해서 M 값까지 만드는 비어있는 리스트를 생성한다. 하지만 여기서 불가능하다면 -1 을 출력해야하므로, 각 리스트의 값을 M+1 로 넣어주어
마지막에 만약 해당 인덱스 리스트가 M보다 크다면, 그것은 불가능이라고 출력하는 것을 전제로 시작한다.

이 알고리즘의 구성은 다음과 같다. ( i : 인덱스 // a : 최소한의 화폐 개수 // k : 화폐의 단위 )
1. a_(i-k) 를 만들 방법이 존재할 경우, a_i = min(a_i,a_(i-k)+1)
2. a_(i-k) 를 만들 수 없다면, a_i = 10001 입력
'''

# target = 15
# m=100
# array = [10001] * (m+1)
# array[0] = 0

# k = 2,3

# for i in k:
#     for j in range(i,m+1):
#         if array[j-i] != 10001:
#             array[j] = min(array[j],array[j-i]+1)

# if array[target] == 10001:
#     print(-1)
# else:
#     print(array[target])




############################################  미래도시  ############################################
'''
 0<=N<=100 (노드의 개수)
 노드개수 n 개이며 sub node 를 거쳐 main node 로 향하는 최단거리를 구한다
 문제 이름답게 미래도시에선 간선이 있는곳은 모두 1의 시간만을 소요한다
'''
# main = 4
# sub = 5
# n = 5

# data = [[0,1,1,1,inf],[1,0,inf,1,inf],[1,inf,0,1,1],[1,1,1,0,1],[inf,inf,1,1,0]]

# dist = [[inf]*n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             dist[i][j] = 0

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if j == k:
#                 continue
#             dist[j][k] = min(data[j][k],dist[j][k],dist[j][i]+dist[i][k])

# print(dist[1][sub-1]+dist[sub-1][main-1])
'''
해설에서는 해당 문제가 전형적인 플로이드 워셜 문제라고 소개하고있다.
노드의 개수가 100개에 불과하기때문에 "모든 점에서 모든 점까지의 거리" 를 구하는 플로이드 워셜알고리즘이
매우 쓸모가 있는것이다.
'''

############################################  전보  ############################################

'''
N 개의 도시 사이에 간선이 놓여있다.
A) start 도시에서 전보를 보냈을 때 메세지를 받을 수 있는 도시는 몇개이며
B) 모든 도시가 메세지를 받는데 걸리는 시간은?
1<= N <=30000

노드의 개수는 최대 30000이다. 만약 플로이드워셜 알고리즘을 사용 할 경우, 시간복잡도는 O(N^3) 이므로 N^3 는 3조에 달한다
따라서 위 문제는 다익스트라 알고리즘을 사용하는것이 적절하다.
A 를 풀기위해서 dist 내의 inf 값이 아닌 값을 count 하면 될 듯 하다.
B 를 위해서는 dist 값 내에서 inf를 제외한 최대값을 output 하면 될 듯 하다.
'''

# n = 3
# data = [[],[(2,4),(3,2)],[],[]]
# dist = [inf] * (n+1)

# # q=[]
# # node = 1
# # heapq.heappush(q,(0,node))
# # dist[node] = 0
# # distance, now = heapq.heappop(q)
# # print(distance,now)

# def dijkstra(node):
#     q =[]
#     heapq.heappush(q,(0,node))
#     dist[node] = 0
#     while q:
#         distance, now = heapq.heappop(q)
#         if dist[now] < distance:
#             continue
#         for i in data[now]:
#             cost = distance + i[1]
#             if cost < dist[i[0]]:
#                 dist[i[0]] = cost
#                 heapq.heappush(q,(cost,i[0]))

# dijkstra(1)
# count = 0
# max_value = 0
# for i in dist:
#     if i > 0 and i != inf:
#         count +=1
# for i in dist:
#     if i > max_value and i != inf:
#         max_value = i
# print(dist)
# print(max_value , count)

'''
21/06/03 직접 작성해보려고 한 결과 단 2일 지났다고 굉장히 버벅였다. 다익스트라 외에도 많은 알고리즘을 배웠지만,
알고있는것도 중요하나 응용할 수 있어야 비로소 사용 할 수 있는것이다. 앞으로 예제를 더 접하면서 응용할 수 있도록 많이 사용하자.
'''


############################################  팀 결성  ############################################
'''
Given ) 팀 합치기 연산과 같은 팀 여부 연산을 사용하라.
        합 연산은 (0 1 3) 과 같이 맨 앞 숫자가 0 으로 시작하고 확인연산은 (1 1 1) 과 같이 맨 앞 숫자가 1 로 시작한다
        또한 확인연산의 경우 확인 결과에 따라서 YES 와 NO 를 출력한다
        1 < N,M < 100,000
'''
# def find(parent,a):
#     if parent[a] != a:
#         parent[a] = find(parent,parent[a])
#     return parent[a]

# def union(parent,a,b):
#     a = find(parent,a)
#     b = find(parent,b)
#     value = min(a,b)
#     parent[a]=parent[b]=value

# print('팀의 수 N, 연산 횟수 M 을 입력해주세요 : ')

# n,m =  map(int,input().split())

# parent =  [0]*(n+1)

# for i in range(n+1):
#     parent[i] = i

# print('연산 node_1 node_2 : ')

# for i in range(m):
#     a,b,c = map(int, input().split())
#     if a == 0:
#         union(parent,b,c)
#     elif a==1:
#         if find(parent,b) == find(parent,c):
#             print('YES!')
#         else:
#             print('Noooooooooo')
'''
만약 바로 서로소 집합 알고리즘을 기억해 냈다면, 상당히 쉬운 예제였다. 
'''        

############################################  도시 분할 계획  ############################################
'''
Given)  마을은 N 개의 집과 M 개의 길로 이루어져 있다. 길은 방향성을 가지지 않으며, 유지비가 존재한다
        여기서 Input 은 (A B C) 로 A 번 집에서 B 번집으로 연결되어있는 간선의 유지비는 C 이다.
Target) 마을을 둘로 나누고싶고 동시에 길이 너무 많다 (유지비가 많이 든다) 따라서 유지비를 최소로 하면서 마을을 둘로 나눈다
        이는 크루스칼 알고리즘을 통해 최적의 길을 남기고 그 후에 크루스칼 알고리즘 결과값에서 가장 큰 간선을 제거하여
        마을을 둘로 나눈다.
'''

# def find_parent(parent,a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent,parent[a])
#     return parent[a]

# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     val = min(a,b)
#     parent[a] = parent[b] = val
    
# n,m = 7,12
# data = [[1,2,3],[1,3,2],[3,2,1],[2,5,2],[3,4,4],[7,3,6],[5,1,5],[1,6,2],[6,4,1],[6,5,3],[4,5,3],[6,7,4]]
# data.sort(key=lambda data:data[2])
# count = 0
# last = 0
# parent = [0]*(n+1)
# for i in range(n+1):
#     parent[i] = i

# for i in data:
#     if find_parent(parent,i[0]) != find_parent(parent,i[1]):
#         union_parent(parent,i[0],i[1])
        
#         count += i[2]
#         last = i[2]

# print(parent)
# print(count - last)
