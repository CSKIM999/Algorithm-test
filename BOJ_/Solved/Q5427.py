from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q5427
#######  TODAY  #######
##### 2022. 04. 23 #####
GIVEN ) 빈 공간과 벽으로 이루어진 건물 안에 불이 났다. 불이 매 초마다 동서남북 인접 공간으로 퍼져 나갈때,
        상근이도 인접한 칸으로 이동할 수 있으며, 마찬가지로 1 초가 걸린다. 상근이가 불을 피해 탈출하는데 걸리는 시간을 구하라.
        상근이는 벽, 불이 붙으려는 칸으로는 이동할 수 없다. 하지만, 현재 자리로 불이 옮겨옴과 동시에 다른 칸으로는 움직일 수 있다.
        '.' : 빈공간 , '#' : 벽 , '@' : 상근이의 시작위치 , '*' : 불
INPUT ) 첫째 줄에 테스트 케이스의 갯수가 주어진다. 이는 최대 100개이다.
        각 테스트케이스의 첫째 줄은 지도의 너비와 높이 w,h 가 주어진다. ( 1 <= w,h <= 1,000 )
        그리고 그 다음 h 개의 줄에 w 개의 문자로 빌딩의 지도가 주어진다.
OUTPUT) 탈출하는데 필요한 가장 짧은 시간을 출력하라. 만약 불가능하다면, IMPOSSIBLE 를 출력하라

Approach )  spread fire -> move(bfs) -> check 의 순서로 진행되야할 듯 하다.
            bfs [maxcost<now -> move]
'''
# import sys
# input = sys.stdin.readline
# from collections import deque

# def spreadFire(table):
#     returnTable = [i[:] for i in table[:]]
#     for x in range(len(table)):
#         for y in range(len(table[0])):
#             if table[x][y] == '*':
#                 for i in range(4):
#                     nx,ny = d[i][0] + x , d[i][1] + y
#                     if returnTable[nx][ny] == '.':
#                         returnTable[nx][ny] = '*'
#     return returnTable
# def bfs(table):
#     global hist
#     a = False
#     for x in range(len(table)):
#         for y in range(len(table[0])):
#             if table[x][y] == "@":
#                 a,b = x,y
#                 break
#         if a:
#             break
#     maxCost = 0
#     # x,y = man
#     q = deque()
#     q.append([a,b,0])
#     table = spreadFire(table)
#     q.append([-1,-1,-1])
#     while q:
#         x,y,c = q.popleft()
#         if maxCost and c>maxCost:
#             continue
#         if x == -1:
#             if not q:
#                 if maxCost:
#                     return print(maxCost)
#                 return print('IMPOSSIBLE')
#             table = spreadFire(table)
#             q.append([-1,-1,-1])
#             continue
#         hist.append([x,y])
#         for i in range(4):
#             nx,ny = x+ d[i][0], y+d[i][1]
#             if nx<0 or nx>=h or ny<0 or ny>=w:
#                 maxCost = c+1
#                 continue
#             if table[nx][ny] == '.':
#                 if [nx,ny] not in hist:
#                     q.append([nx,ny,c+1])
# tc = int(input())
# for i in range(tc):
#     hist = []
#     w,h = map(int,input().split())
#     table = []
#     for i in range(h):
#         table.append(list(input()))
#     d = [[-1,0],[1,0],[0,-1],[0,1]]
#     bfs(table)










#############################
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
                if maxCost:
                    maxCost = min(maxCost,c+1)
                else:
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




'''
6트 Solve ,, TC 가 상당히 깐깐해서 오래걸림,, 지속사용가능한 bfs 테이블 만들기 포인트
'''