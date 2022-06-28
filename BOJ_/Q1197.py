from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1197
#######  TODAY  #######
##### 2022. 06. 28 #####
GIVEN ) 최소 스패닝 트리 -> 최소신장트리 알고리즘 ( 크루스칼 알고리즘 )
        크루스칼알고리즘에서는 매번 우선순위큐를 사용하여 가장 작은 가중치를 이어준다.
        동시에 이어주는값이 사이클을 만들지 않도록 부모union 값을 확인해준다.
INPUT ) 첫째 줄에 정점의 개수 V (1만 이하의 자연수) 와 간선의 개수 E (10만 이하의 자연수) 가 주어진다.
        다음 E 개의 줄에 간선에 대한 정도 A,B,C 가 주어지며
        각각 A노드에서 B 노드까지 가중치 C 의 간선이 연결되어있다는 뜻이다.
        C 는 음수일 수 있으며, 절댓값이 100만 이하의 값이다.
        그래프의 모든 노드는 연결되어있으며, 번호가 매겨진다.
OUTPUT) 최소신장의 모든 더한 값을 출력하라
Approach ) union-find 와 크루스칼을 사용하자.  
'''
import sys
import heapq as h
hpush = h.heappush
hpop = h.heappop

sys.setrecursionlimit(25000)
# input = sys.stdin.readline
def find(par,node):
    if par[node] != node:
        return find(par,par[node])
    else:
        return par[node]
def union(par,a,b):
    a,b = find(par,a),find(par,b)
    if a>b:
        par[a] = b
        return False
    elif a<b:
        par[b] = a
        return False
    else:
        return True

n,m = map(int,input().split())
linked = []
for _ in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    hpush(linked,[c,a,b])
parent = [i for i in range(n)]
result = 0
while linked:
    dist,a,b = hpop(linked)
    if union(parent,a,b):
        continue
    result += dist
print(result)