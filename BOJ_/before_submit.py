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
