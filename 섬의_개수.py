from collections import deque
d = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
while True:
    n,m = list(map(int,input().split()))
    if n== 0 and m == 0:
        break
    table = []
    count = 2
    for _ in range(m):
        table.append(list(map(int,input().split())))
    def bfs(a,b,index):
        q = deque()
        q.append([a,b])
        table[a][b] = index
        while q:
            x,y = q.popleft()
            for dx,dy in d:
                nx,ny = x+dx,y+dy
                if nx >= m or nx < 0 or ny>=n or ny < 0:
                    continue
                if table[nx][ny] != 1:
                    continue
                table[nx][ny] = index
                q.append([nx,ny])
    for ii in range(m):
        for jj in range(n):
            if table[ii][jj] == 1:
                bfs(ii,jj,count)
                count += 1
    print(count-2)