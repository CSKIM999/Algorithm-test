'''
직사각형 모양의 방을 로봇청소기로 청소하고자 한다. 일부 칸에는 가구가 놓여있고 로봇은 가구 위를 이동할 수 없다.
로봇은 오직 인접한 한 칸으로만 이동할 수 있을 때 모든 더러운칸을 청소하는데 필요한 최소 이동횟수를 반환하라

입력은 여러개의 테스트케이스로 주어진다
각 테스트케이스의 첫째 줄에는 가로크기 w, 세로크기 h 가 주어진다.(1<=w,h<=20) 둘째 줄 부터 h개의 줄에 방의 정보가 주어진다.
. : 깨끗한 칸 ,, * : 더러운 칸 ,, x : 가구 ,, o : 로봇청소기의 시작위치
더러운 칸의 개수는 10개 이하이며, 로봇청소기는 오직 하나만 존재한다.
입력의 마지막 줄에는 0 이 2개 주어진다.

각 테스트케이스마다, 더러운 칸을 모두 깨끗한 칸으로 바꾸는 최소 이동횟수를 한줄에 하나씩 출력하라.
만약 방문할 수 없는 더러운 칸이 존재하는 경우 -1을 출력하라
'''
from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline


while True:
    result = 1e9
    w,h = map(int,input().split())
    if w == 0:
        break
    case = []
    for i in range(h):
        case.append(list(input().strip()))
    dic = {'.':0,'*':-1,'x':2,'o':1}
    dxdy = [[0,-1],[1,0],[0,1],[-1,0]]
    table = []
    robot = []
    trashes = []

    for i in range(h): #table 의 str 을 int 로 변환
        temp = []
        for j in case[i]:
            temp.append(dic[j])
        table.append(temp)

    def casing(alpha):
        garo= len(alpha[0])
        mit = [2]*(garo+2)
        temp = []
        temp.append(mit)
        for i in alpha:
            temp.append([2]+i+[2])
        temp.append(mit)
        return temp

    table = casing(table)

    for i in range(len(table)): #로봇과 쓰레기위치 입력
        for j in  range(len(table[0])):
            now = table[i][j]
            if now == 2 or now == 0:
                continue
            elif now == 1:
                robot.append(i)
                robot.append(j)
            else:
                trashes.append([i,j])


    def setVisitTable(G): #지금 사용할 방문테이블
        garo,sero = len(G[0]),len(G)
        return [[False]*garo for _ in range(sero)]

    flag = True

    def bfs(Robot,Tlist): #tlist 에 permutaion 리스트가 삽입될것
        global flag,result

        fuel = 0
        Fflag = True
        for node in Tlist:
            if Fflag:
                start = Robot
                Fflag = False
            else:
                start = [nx,ny]
            if fuel > result:
                return 1e9
            inflag = False
            dx,dy = trashes[node]
            queue = deque([[start[0],start[1],0]])
            visit = setVisitTable(table)
            visit[start[0]][start[1]] = True
            while queue:
                x,y,c = queue.popleft()
                for a,b in dxdy:
                    nx,ny = x+a,y+b
                    if nx==dx and ny == dy:
                        fuel += c+1
                        inflag = True
                        queue.clear()
                        break
                    if table[nx][ny] != 2 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        queue.append([nx,ny,c+1])
            if not inflag:
                return -1
        return fuel
    n = len(trashes)
    tindex = [i for i in range(n)]
    perm = list(permutations(tindex,n))
    dist = [1e9 for _ in range(len(perm))]
    for i in range(len(perm)):
        Travel = perm[i]
        temp = bfs(robot,Travel)
        if temp == -1:
            result = -1
            flag = False
            break
        dist[i] = temp
    if flag:
        result = min(dist)
    print(result)