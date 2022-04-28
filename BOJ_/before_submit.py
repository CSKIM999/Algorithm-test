import sys
input = sys.stdin.readline
from collections import deque
def spreadFire(Queue,table):
    fireTable = [i[:] for i in table[:]]
    q = deque()
    while Queue:
        x,y = Queue.popleft()
        fireTable[x][y] = '0'
        q.append([x,y,0])
    while q:
        x,y,c = q.popleft()
        for i in range(4):
            nx,ny = x+d[i][0], y+d[i][1]
            if 0<=nx<len(table) and 0<=ny<len(table[0]):
                if not fireTable[nx][ny].isdigit() and fireTable[nx][ny] == '.': 
                    fireTable[nx][ny]=str(c+1)
                    q.append([nx,ny,c+1])
                elif fireTable[nx][ny].isdigit():
                    if int(fireTable[nx][ny])>c+1:
                        fireTable[nx][ny] = str(c+1)
                        q.append([nx,ny,c+1])
    return fireTable


def bfs(table):
    global hist
    fireq = deque()
    a = False
    for x in range(len(table)):
        for y in range(len(table[0])):
            if table[x][y] == "@":
                table[x][y] = '.'
                a,b = x,y
            elif table[x][y] == '*':
                fireq.append([x,y])
            elif table[x][y] == "#":
                table[x][y] = '-1'
    maxCost = 0
    q = deque()
    q.append([a,b,0])
    fireTable = spreadFire(fireq,table)
    while q:
        x,y,c = q.popleft()
        if maxCost and c>maxCost:
            continue
        table[x][y] = c
        for i in range(4):
            nx,ny = x+ d[i][0], y+d[i][1]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                maxCost = c+1
                continue
            if fireTable[nx][ny]=='.' or int(fireTable[nx][ny])>c+1:
                if table[nx][ny] =='.':
                    q.append([nx,ny,c+1])
                    table[nx][ny] = c+1
                elif table[nx][ny] < c+1:
                    continue
    if maxCost == 0:
        print('IMPOSSIBLE')
    else:
        print(maxCost)

tc = int(input())
d = [[-1,0],[1,0],[0,-1],[0,1]]
for i in range(tc):
    hist = []
    w,h = map(int,input().split())
    table = []
    for i in range(h):
        table.append(list(input()))
    bfs(table)