from collections import deque
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q7576
#######  TODAY  #######
##### 2022. 10. 05 #####
GIVEN ) 격자 안에 익거나 안익은 토마토 혹은 빈칸이 존재한다.
        안익은 토마토는 인접한 격자에 익은 토마토가 있으면 익게 된다.
        반대로 저절로 익는 경우는 없다.
        토마토가 모두 익는데 걸리는 시간을 출력하라
        만약 처음부터 모두 다 익어있다면, 0을 출력하고
        모두 익지 못하는 상황이라면 -1 을 출력하라
INPUT ) 첫째 줄에 상자의 크기를 나타내는 M,N 이 주어지며 둘 다 2 이상 1,000 이하의 자연수이다.
        M 은 가로의 칸, N은 세로의 칸을 나타낸다.
        이후 N개의 줄에 걸쳐 M 개의 격자정보가 주어진다.
        -1 은 빈칸, 0 은 안익은 토마토, 1은 익은 토마토를 나타낸다.
OUTPUT) 모두 익을때까지의 최소날짜를 출력하라.
Approach )  먼저 쭉 순회하면서 익은토마토 위치, 안익토 위치 받아내기
만약 안익토 없으면 0 출력
bfs 돌려서 각 익토마다 인접행렬 익혀버리기
더이상 큐에 들어간거 없는데 아직 안익토가 있으면 -1출력
'''
# sys.setrecursionlimit(25000)


# input = sys.stdin.readline
# m, n = map(int, input().split())
# dx = [-1, 0, 0, 1]
# dy = [0, -1, 1, 0]
# table = [list(map(int, input().split())) for _ in range(n)]
# comp, yet = set(), set()
# q = deque()
# for i in range(n):
#     for j in range(m):
#         if table[i][j] == 0:
#             yet.add((i, j))
#         elif table[i][j] == 1:
#             comp.add((i, j))
#             q.append([(i, j), 0])
# result = 0
# if not comp:
#     print(-1)
# elif not yet:
#     print(0)
# else:
#     while q:
#         node, count = q.popleft()
#         x, y = node
#         if count > result:
#             result = count
#         if not yet:
#             continue

#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if (nx, ny) in yet:
#                     yet.remove((nx, ny))
#                     q.append([(nx, ny), count+1])
#     if yet:
#         print(-1)
#     else:
#         print(result)


from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
table = [list(map(int, input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if table[i][j] == 1:
            q.append([i, j])
result = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if table[nx][ny] == 0:
                table[nx][ny] = table[x][y] + 1
                q.append([nx, ny])

flag = True
answer = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == 0:
            answer = -1
            flag = False
            break
    if flag:
        answer = max(answer, max(table[i])-1)
    else:
        break
print(answer)
'''
modified algorithm
'''