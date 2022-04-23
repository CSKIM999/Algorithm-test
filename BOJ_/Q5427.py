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
from collections import deque
maxCost = 1e9

w,h = map(int,input().split())
table = []

for i in range(h):
    table.append(list(input()))
    
d = [[-1,0],[1,0],[0,-1],[0,1]]

def spreadFire(table):
    returnTable = [i[:] for i in table[:]]
    for x in range(len(table)):
        for y in range(len(table[0])):
            if table[x][y] == '*':
                for i in range(4):
                    nx,ny = d[i][0] + x , d[i][1] + y
                    if returnTable[nx][ny] == '.':
                        returnTable[nx][ny] = '*'

    return returnTable

getTable = spreadFire(table)
xprint(spreadFire(getTable))
print()
xprint(table)