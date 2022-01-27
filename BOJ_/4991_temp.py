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
from itertools import permutations
import queue
import sys

input = sys.stdin.readline

while True:
    w,h = map(int,input().split())
    if w == 0:
        break
    case = []
    for i in range(h):
        case.append(list(input().strip()))
    dic = {'.':0,'*':-1,'x':2,'o':1}
    dxdy = [[0,-1],[1,0],[0,1],[-1,0]]
    # nowCase = tCase3.split('\n')
    table = []
    robot = []
    trashes = []
    result = 1e9
    for i in range(h):
        temp = []
        for j in case[i]:
            temp.append(dic[j])
        table.append(temp)

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


    def bfs(now):
        visit = [[0]*w for _ in range(h)]
        x,y = now
        visit[x][y] = 1
        q = deque([(x,y)])
        while q:
            x,y = q.popleft()
            for a,b in dxdy:
                nx,ny = x+a,y+b
                if 0<= nx < h and 0<= ny < w and not visit[nx][ny] and table[nx][ny] != 2:
                    visit[nx][ny] = visit[x][y] +1
                    q.append((nx,ny))
        return visit
    t_visit = bfs(robot)
    flag = False
    for a,s in trashes:
        if t_visit[a][s] == 0:
            flag = False
            break
        t_visit[a][s]

    n = len(trashes)
    tindex = [i for i in range(n)]
    Tlist = list(permutations(tindex,n))
    b_flag = True
    for nodes in Tlist:
        flag = True
        temp = 0
        for index in nodes:
            node = trashes[index]
            if flag:
                flag = False
                Vtable = bfs(robot)
                tx,ty = node
                count = Vtable[tx][ty] -1
            else:
                Vtable = bfs([tx,ty])
                tx,ty = node
                count = Vtable[tx][ty] -1
            temp += count

        result = min(result,temp)
    print(result)





# def bfs(now,Tlist,count):
#     global flag,result
#     if not flag:
#         return


#     for dest in Tlist:
#         inflag = False
#         dx,dy = dest
#         bfsDlist = Tlist[:]
#         bfsDlist.remove([dx,dy])
#         queue = deque([[now[0],now[1],count]])
#         visit = setVisitTable(table)
#         visit[now[0]][now[1]] = True
#         while queue:
#             x,y,c = queue.popleft()

#             for a,b in dxdy:
#                 nx,ny = x+a,y+b
#                 if nx==dx and ny==dy:
#                     if not bfsDlist:
#                         result = min(result,c+1)
#                     inflag = True
#                     bfs([nx,ny],bfsDlist,c+1)
#                     break
#                 elif not visit[nx][ny]:
#                     if table[nx][ny] != 2:
#                         queue.append([nx,ny,c+1])
#                         visit[nx][ny] = True
#                     else:
#                         visit[nx][ny] = True
#         if not inflag:
#             flag = False
# bfs(robot,trashes,0)
# if not flag:
#     result = -1
# print(result)