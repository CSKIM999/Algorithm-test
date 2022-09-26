from collections import deque

n, m = list(map(int, input().split()))
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
order = []
for i in range(m):
    order.append(list(map(int, input().split())))

d = [[0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]]
dd = [[-1, -1, 1, 1], [-1, 1, -1, 1]]


def cv(togo, dist):
    dist = dist % n
    dx, dy = d[0][togo], d[1][togo]
    # cloud = deque()
    while q:
        x, y = q.popleft()
        nx, ny = x+(dx*dist), y+(dy*dist)
        if nx < 0:
            nx = n+nx
        elif nx >= n:
            nx -= n
        if ny < 0:
            ny = n + ny
        elif ny >= n:
            ny -= n

        table[nx][ny] += 1
        hist.add((nx, ny))


def wv():
    for x, y in hist:
        for i in range(4):
            nx, ny = x+dd[0][i], y+dd[1][i]
            if 0 <= nx < n and 0 <= ny < n and table[nx][ny] > 0:
                table[x][y] += 1


q = deque()
q.extend([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])
for a, b in order:
    hist = set()
    a -= 1
    cv(a, b)
    wv()
    for i in range(n):
        for j in range(n):
            if (i, j) in hist:
                continue
            if table[i][j] >= 2:
                table[i][j] -= 2
                q.append([i, j])
result = 0
for i in range(n):
    result += sum(table[i])
print(result)
