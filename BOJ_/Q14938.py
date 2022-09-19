import sys
from lib import xprint, Prepare_Coding_Test
import heapq
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q14938
#######  TODAY  #######
##### 2022. 09. 19 #####
GIVEN ) N 개의 지역이 R 개의 길로 연결되어있다.
        임의의 지역에서 시작하여 최대 m 만큼의 범위를 움직일 수 있을때
        가장 큰 기대수익을 갖는 경우를 구하라
INPUT ) 첫째 줄에 지역의 개수 n ( 100 이하의 자연수 ),  수색범위 m ( 15 이하의 자연수 ), 길의 개수 r ( 100 이하의 자연수 )
        둘째 줄에는 총 n 개의 지역에 있는 아이템의 갯수가 ( 30 이하의 자연수 ) 주어진다.
        셋째 줄부터 r+2 번째 줄까지 두 지역의 번호와 길이값 l 이 주어진다 ( l 15 이하의 자연수 )
OUTPUT) 최대 기대 아이템개수를 출력하라
Approach )  개선데이크를 각 노드별로 돌리는게 플로이드워셜보단 낫지않나?
개선 데이크 함수

다익스트라 ( 노드수, 원하는 시작점 )
    만들되 만약 m 을 넘어가는 노드는 안가버리기
for 문 돌려서 
    모든 노드 순회

'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

push = heapq.heappush
hpop = heapq.heappop

n, m, r = map(int, input().split())
table = list(map(int, input().split()))
lane = [[] for _ in range(n)]

for i in range(r):
    a, b, c = map(int, input().split())
    lane[a-1].append([c, b-1])
    lane[b-1].append([c, a-1])


def dijkstra(targetNode):
    t = targetNode
    dist = [1e9 for _ in range(n)]
    q = []
    push(q, [0, t])

    while q:
        far, node = hpop(q)
        if dist[node] <= far:
            continue
        dist[node] = far
        for xdist, x in lane[node]:
            cost = xdist+far
            if cost > m:
                continue
            if cost < dist[x]:
                push(q, [cost, x])
    result = 0
    for i in range(n):
        if dist[i] != 1e9:
            result += table[i]
    return result


ans = 0
for i in range(n):
    ans = max(ans, dijkstra(i))
print(ans)
