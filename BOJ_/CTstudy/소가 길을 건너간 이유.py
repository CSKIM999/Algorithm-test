from collections import deque
import heapq

n,m = list(map(int,input().split()))
table = [list(map(int,input().split())) for _ in range(n)]
# 큐에다가 x,y,eatcount,mc,time 넣어줘야겠다
# 그리고 큐가 n-1,n-1 에 도달하면 체크해주기
def getDistArr(x):
    distArr = []
    for i in range(-x,x+1):
        for j in range(-x,x+1):
            if x == 2:
                if i+j == x and not (i == 0 and j == 0):
                    distArr.append((i,j,x))
            else:
                if abs(i)+abs(j) == x and not (i == 0 and j == 0):
                    distArr.append((i,j,x))
    return distArr
d = getDistArr(1)
d2 = getDistArr(2)
d3 = getDistArr(3)
d.extend(d2)
d.extend(d3)
q = [[0,0]]
heapq.heapify(q)
# x,y,moveCount,time,hist
dd = [[-1,0],[0,-1],[0,1],[1,0]]
result = None
hist = [[1e9 for _ in range(n)] for _ in range(n)]
hist[0][0] = 0

while q:
    x,y = heapq.heappop(q)
    now = hist[x][y]
    if now > hist[-1][-1]:
        continue
    
    for dx,dy,dist in d:
        nx,ny = x+dx,y+dy
        if 0> nx or nx >= n or 0 > ny or ny >= n:
            continue
        new = hist[nx][ny]
        cost = table[nx][ny]
        if dist == 2:
            if nx == n-1 and ny == n-1 and now+2*m < new:
                hist[nx][ny] = now+2*m
            continue
        cost += 3*m
        if 0<= nx < n and 0<=ny<n and now+cost < new:
            hist[nx][ny] = now+cost
            if nx == n-1 and ny == n-1:
                continue    
            heapq.heappush(q,[nx,ny])

print(hist[-1][-1])