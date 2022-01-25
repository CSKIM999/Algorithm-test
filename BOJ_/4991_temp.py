def xprint(a):
    for i in a:
        print(i)
tCase1 ="""7 5
.......
.o...*.
.......
.*...*.
.......
"""
tCase2 = '''15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
'''
tCase3 = """10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
"""
from collections import deque

dic = {'.':0,'*':-1,'x':2,'o':1}
dxdy = [[0,-1],[1,0],[0,1],[-1,0]]
nowCase = tCase1.split('\n')
w,h = map(int,nowCase[0].split())
table = []
robot = []
trashes = []
for i in range(1,h+1):
    temp = []
    for j in nowCase[i]:
        temp.append(dic[j])
    table.append(temp)

def casing(table):
    garo= len(table[0])
    mit = [2]*(garo+2)
    temp = []
    temp.append(mit)
    for i in table:
        temp.append([2]+i+[2])
    temp.append(mit)
    return temp    
    
table = casing(table)


for i in range(len(table)):
    for j in  range(len(table[0])):
        now = table[i][j]
        if now == 2 or now == 0:
            continue
        elif now == 1:
            robot.append(i)
            robot.append(j)
        else:
            trashes.append([i,j])


def setVisitTable(G):
    garo,sero = len(G[0]),len(G)
    return [[False]*garo for _ in range(sero)]

def bfs(now,Tlist,count): #trashes, 노드와거리
    for dest in trashes:
        dx,dy = dest
        bfsDlist = trashes[:]
        bfsDlist.remove([dx,dy])
        queue = deque([robot[0],robot[1],0])
        visit = setVisitTable(table)
        visit[robot[0]][robot[1]] = True
        while queue:
            x,y,c = queue.popleft()
            for a,b in dxdy:
                nx,ny = x+a,y+b
                if nx==dx and ny==dy:
                    if len(trashes) == 1:
                        result = min(result,c)
                if not visit[nx][ny]:
                    if table[nx][ny] == 0:
                        queue.append([nx,ny,c+1])
                        visit[nx][ny] = True
                    else:
                        visit[nx][ny] = True
