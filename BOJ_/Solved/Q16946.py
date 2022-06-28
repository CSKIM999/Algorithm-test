from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q16946
#######  TODAY  #######
##### 2022. 06. 28 #####
GIVEN ) 맵이 N*M 크기의 행렬로 표현되며 맵의 요소는 벽 1, 빈칸 0 으로 나타내진다.
        상하좌우로 인접한 칸만 이동할 수 있을 때 다음을 구하라
        각각의 벽에 대해 선택된 벽을 허물어 이동할 수 있는 칸으로 간주한다.
        그리고 그 위치에서 이동할 수 있는 칸의 최대갯수를 구하라
INPUT ) 첫째 줄에 N ( 1000 이하의 자연수 ) M ( 천 이하의 자연수 ) 가 주어지며
        다음 N 개의 줄에 M 개의 숫자로 맵이 주어진다
OUTPUT) 맵의 형태로 정답을 출력하라. 원래 빈칸인 곳은 0, 벽인 곳은 이동할 수 있는 칸의 갯수를 10으로 나눈 나머지를 출력
Approach ) 매 노드에다가 bfs 돌리는건 분명 비합리적일 것같음
            빈칸을 bfs 돌려서 메모이제이션 하자 한개의 벽만 허물 수 있으니 상하좌우 만나는 빈칸을 더해주면 될것.


def bfs(지금)
    방문리스트 = []
    큐.지금
    방문리스트 += 지금
    반복 큐:
        지금 = 큐팝
        for 인접 in 지금
            만약 0 & 방문 x?
                방문리스트 += 인접
                큐.인접
    카운트 = 방문리스트 길이
    for 방문리스트
        테이블 방문리스트값 = -카운트



for N
    for M
        만약 지금 == 0?
            bfs(지금)
테이블 세팅 완료

for N
    for M
        만약 지금 == 1?
            임시 = 1
            for 4
                인접 < 0 ?
                    임시 += -(인접)
            답.지금 = 임시
        아니라면?
            답.지금 = 0
'''
import sys
input = sys.stdin.readline
from collections import deque
d = [[1,0],[-1,0],[0,1],[0,-1]]
N,M = list(map(int,input().split()))
data = []
for _ in range(N):
    data.append(list(map(int,input().strip())))
answer = [[0 for _ in range(M)] for _ in range(N)]
blocks = 1
def bfs(now):
    global blocks
    q= deque()
    hist = []
    q.append(now)
    hist.append(now)
    while q:
        x,y = q.popleft()
        data[x][y] = -1
        for i in range(4):
            nx,ny = x+d[i][0], y+d[i][1]
            if 0<= nx< N and 0<=ny< M:
                if data[nx][ny] == 0:
                    data[nx][ny] = -1
                    hist.append([nx,ny])
                    q.append([nx,ny])
    c = len(hist)
    for i in hist:
        x,y = i
        data[x][y] = [c,blocks]
    blocks += 1

for n in range(N):
    for m in range(M):
        if data[n][m] == 0:
            bfs([n,m])

for n in range(N):
    for m in range(M):
        if data[n][m] == 1:
            temp = 1
            hist = []
            x,y = n,m
            for i in range(4):
                nx,ny = x+d[i][0], y+d[i][1]
                if 0<= nx< N and 0<=ny< M and data[nx][ny] != 1:
                    newV,newU = data[nx][ny]
                    if newU not in hist:
                        temp += newV
                        hist.append(newU)
            answer[x][y] = temp%10

for i in answer:
    print(''.join(map(str,i)))

'''
bfs 를 돌리되 각 벽에서 bfs 가 아닌 빈칸에 대고 bfs 를 돌리고 메모이제이션을 한 아이디어

대부분의 구상 및 구현까지는 30분컷.
한글로 필요 코드를 적어놓고 하나씩 구현해 나가는방법이 유효했다고 생각함.
풀다가 인접 4방향을 순회하지만, 각각의 방향에 중복되는 union 의 존재를 생각하지 못했음.

>>> union 의 중복처리 필요성에 따라, 처음엔 시간복잡도를 생각하지 않고,
    data값에 [value, unionIndex] 형태로 줄까 싶었지만 그렇게 할 경우 코드를 많이 고쳐야해서 딕셔너리 방식을 생각함

>>> union 의 중복처리를 위해 딕셔너리를 만들고 (x,y) 의 키값으로 union 을 주는 코드를 짜보았으나,
    해당 코드는 시간초과 판정을 받음.
>>> 따라서 시간초과판정 해결을 위해 여러부분을 고쳐봤지만, 결국 문제는 딕셔너리 키밸류 추가코드로 인해 발생한것으로 보여짐.
    원래 생각한대로 [value, unionIndex] 형태로 작성하니 정답판정.
'''