from collections import deque
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
table = []
for _ in range(n):
    table.append(list(map(int, input().strip())))
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
