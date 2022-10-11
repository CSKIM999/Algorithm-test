import sys
from collections import deque
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2206
#######  TODAY  #######
##### 2022. 10. 11 #####
GIVEN ) >>> 벽 부수고 이동하기 <<< 
        n,m 크기의 행렬에 빈칸 혹은 벽이 설치되어있다
        1,1 에서 n,m 위치로 최소비용으로 이동하고자 한다.
        이 과정에서 벽을 단 한번 부술 수 있을 때 최소 비용을 출력하라
INPUT ) n,m 은 1000 이하의 자연수이다.
        또한 시작점과 끝점은 항상 빈칸이다.
OUTPUT) 최단비용 혹은 불가능한 경우 -1 을 출력하라
Approach )bfs 에 와일드카드를 넣어서 돌려보자
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
n, m = list(map(int, input().split()))
table = []
for _ in range(n):
    table.append(list(map(int, input())))
vtable = [[[1e9, 1e9] for _ in range(m)]for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
q = deque()
q.append([0, 0, 1, True])
vtable[0][0] = [1, 1]
result = 1e9
while q:
    x, y, count, ticket = q.popleft()
    if x == n-1 and y == m-1 and count < result:
        result = count
        continue

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if ticket:
                if table[nx][ny] == 0 and vtable[nx][ny][0] > count+1:
                    vtable[nx][ny][0] = count+1
                    q.append([nx, ny, count+1, ticket])
                else:
                    if vtable[nx][ny][1] > count + 1:
                        vtable[nx][ny][1] = count+1
                        q.append([nx, ny, count+1, False])
            else:
                if table[nx][ny] == 0 and vtable[nx][ny][1] > count+1:
                    vtable[nx][ny][1] = count+1
                    q.append([nx, ny, count+1, False])

if result == 1e9:
    result = -1
print(result)
