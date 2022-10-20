import sys
import heapq
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1238
#######  TODAY  #######
##### 2022. 10. 20 #####
GIVEN ) N 개의 숫자로 구분된 각각의 마을에 한명의 학생이 살고있다.
        이중 N 명의 학생이 파티를 열고자 했고, 각 마을 사이엔 M 개의
        단방향 도로가 존재하며 i 번째 길을 지나는데 Ti 만큼의 자원을 소모한다.
        각각의 학생은 X번 마을에 파티에 참석하기 위해 항상 최단거리로 오간다.
        N 명의 학생 중 오고,가는데 가장 많은 비용을 소모한 학생을 찾아라.
INPUT ) 첫째 줄에 N,M,X 가 주어진다. ( 1,000 이하의 자연수 N , 10,000 이하의 자연수 M )
        그 이후 M 개의 줄에 걸쳐 간선의 정보가 주어진다.
            여기서 시작점과 끝점이 같은 중복되는 간선정보는 주어지지 않으며
            A,B,C 는 A에서 B로 향하는 간선의 비용이 C ( 100 이하의 자연수 )라는 뜻.
            여기서 입력은 모든 학생이 무조건 X마을로 오고갈수있는 데이터가 주어진다.
OUTPUT) 가장 많은 비용을 지출한 학생의 비용을 출력하라
Approach ) X 번에서 다익스트라 돌리고 테이블로 사용
for 문 돌려서 데이크스트라 to X
'''
sys.setrecursionlimit(25000)

qpush, qpop = heapq.heappush, heapq.heappop
input = sys.stdin.readline
n, m, x = list(map(int, input().split()))
dist = {i: [] for i in range(n+1)}
for i in range(m):
    a, b, c = list(map(int, input().split()))
    dist[a].append((c, b))


def dijkstra(now, togo=None):
    q = []
    qpush(q, (0, now))
    table = {i: 1e9 for i in range(n+1)}
    table[now] = 0
    if togo != None:
        while q:
            cost, node = qpop(q)
            if table[togo] != 1e9 and cost > table[togo]:
                continue

            for nc, nn in dist[node]:
                if nc+cost < table[nn]:
                    table[nn] = nc+cost
                    qpush(q, (nc+cost, nn))
        return table[togo]
    else:
        while q:
            cost, node = qpop(q)
            for nc, nn in dist[node]:
                if nc+cost < table[nn]:
                    table[nn] = nc+cost
                    qpush(q, (nc+cost, nn))
        return table


Xtable = dijkstra(x)
result = 0
for i in range(1, n+1):
    if i == x:
        continue
    toX = dijkstra(i, x)
    if result < toX + Xtable[i]:
        result = toX+Xtable[i]
print(result)
