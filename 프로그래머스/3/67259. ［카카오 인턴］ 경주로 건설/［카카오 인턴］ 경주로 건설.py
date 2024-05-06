from collections import deque
def solution(board):
    d = [[-1,0,1,0],[0,-1,0,1]]
    n = len(board)
    table = [[[1e9,1e9] for _ in range(n)] for _ in range(n)]
    table[0][0] = [0,0]
    q = deque()
    q.append([0,0,0]) # x,y, direction
    q.append([0,0,3])
    while q:
        x,y,dr = q.popleft()
        di = dr % 2
        value = table[x][y][di]
        for i in range(4):
            nx,ny = x + d[0][i], y + d[1][i]
            ii = i%2
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny]:
                continue
            if dr % 2 == i % 2:
                spend = 100
            else:
                spend = 600
            if nx == 2 and ny == 6:
                print(x,y,dr,i,value, spend)
            if value + spend < table[nx][ny][ii]:
                table[nx][ny][ii] = value+spend
                q.append([nx,ny,i])
    return min(table[-1][-1])