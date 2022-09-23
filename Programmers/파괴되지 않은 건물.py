board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2],
         [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
n, m = len(board), len(board[0])
dic = {}
for i in range(n):
    dic[i] = {}
    for j in range(m):
        dic[i][j] = 0


for item in skill:
    pnm, x0, y0, x1, y1, d = item
    if pnm == 1:
        pnm = -1
    else:
        pnm = 1
    dic[x0][y0] += pnm*d
    if 0 <= y1+1 < m:
        dic[x0][y1+1] -= pnm*d
    if 0 <= x1+1 < n:
        dic[x1+1][y0] -= pnm*d
    if 0 <= x1+1 < n and 0 <= y1+1 < m:
        dic[x1+1][y1+1] += pnm*d
c = 0
for i in range(n):
    for j in range(m):
        if j != 0:
            l = dic[i][j-1]
        else:
            l = 0
        dic[i][j] += l
for i in range(n):
    for j in range(m):
        if i != 0:
            u = dic[i-1][j]
        else:
            u = 0
        dic[i][j] += u
for i in range(n):
    for j in range(m):
        board[i][j] += dic[i][j]
        if board[i][j] > 0:
            c += 1
print(c)
