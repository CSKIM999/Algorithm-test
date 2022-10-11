import heapq as h
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1753
#######  TODAY  #######
##### 2022. 10. 11 #####
GIVEN ) 다익스트라.
        V 개의 노드 ( 20,000 이하의 자연수 )
        E 개의 간선 ( 300,000 이하의 자연수 )
        각 간선의 가중치는 10 이하의 자연수
        각 노드 사이에는 두 개 이상의 간선이 존재할 수 있다.
INPUT ) 첫째 줄에 노드의 개수 V 와 간선의 수 E 가 주어진다.
        둘째 줄에 시작 노드번호가 주어지고
        셋째 줄부터 E 개의 줄에 걸쳐 간선 정보 u,v,w 가 주어진다.
        u 노드에서 v 노드까지의 w 가중치의 간선이 있다는 뜻.
OUTPUT) 첫째 줄부터 V 개 줄에 걸쳐 거리를 출력하라
        자기자신은 0 이어지지 않은 간선은 INF 를 출력하라
Approach ) 데이크스트라  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

hi, ho = h.heappush, h.heappop

n, m = map(int, input().split())
start = int(input())
dist = {i: {} for i in range(n+1)}
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    try:
        if dist[a][b] > c:
            dist[a][b] = c
    except KeyError:
        dist[a][b] = c

table = []
for i in range(n+1):
    temp = []
    for j in dist[i]:
        temp.append([dist[i][j], j])
    table.append(temp)

dist = [1e9 for _ in range(n+1)]
dist[start] = 0
q = [[0, start]]
while q:
    dv, now = ho(q)
    for v, node in table[now]:
        if v+dv < dist[node]:
            hi(q, [v+dv, node])
            dist[node] = v+dv

for i in range(1, n+1):
    if dist[i] != 1e9:
        print(dist[i])
    else:
        print("INF")
