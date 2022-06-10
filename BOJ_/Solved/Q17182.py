from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q17182
#######  TODAY  #######
##### 2022. 06. 10 #####
GIVEN ) 모든 행성을 탐사하는 데 필요한 최소시간을 구하고자 한다.
        각 행성에서 다른 행성으로 이동하는데 필요한 자원이 2차원행렬로 주어지며
        탐사 후 시작행성으로 돌아올 필요는 없으며, 재방문또한 가능하다.
INPUT ) 행성의 개수 N ( 2<= N <= 10 ) 행성의 위치 K ( 0<= K <= N )
        다음 N 줄에 걸쳐 행성간 이동시 필요자원이 띄어쓰기로 구분되어 주어진다. ( 0 <= E <= 1,000 )
OUTPUT) 모든 행성을 탐사하기 위한 최소비용을 출력하라 
Approach )  플로이드 워셜 알고리즘을 추천한다. 행성의 개수가 10개여서 N^3 해봐야 1,000 이긴 하다.
'''
import sys
from collections import deque
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

q = deque()
N, K = map(int,input().split())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))
res = [[1e19]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            res[i][j] = min(res[i][j],data[i][j],data[i][k]+data[k][j])

a = [0]*N
a[K] =1
result = 1e19
basic = ''.join(map(str,a))
q.append([0,K,basic])
xprint(res)
while q:
    count,now, bit  = q.popleft()
    if bit == '1'*N:
        result = min(count,result)
        continue

    if result != 1e19:
        if count > result:
            continue
    
    bit = list(map(int,bit))
    for i in range(N):
        # 같은노드 처리
        if i == now:
            continue
        # 미방문 노드라면?
        temp = bit[:]
        if not bit[i]:
            temp[i] = 1
            q.append([count+res[now][i],i,''.join(map(str,temp))])

print(result)

'''
플로이드 워셜을 자주 안써서 루프처리를 따로 해야하나 계속 고민했음.
각 노드에 대한 최단거리가 이미 구해진 값이기때문에 백트래킹 돌리면서 모든 노드 방문여부만 비트마스킹으로 체크해주면 되는거였음.
'''