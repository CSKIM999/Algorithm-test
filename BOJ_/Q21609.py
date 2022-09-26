from collections import deque
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q21609
#######  TODAY  #######
##### 2022. 09. 26 #####
GIVEN ) 다음 룰에 의해 반복되는 게임이 있다.
        1. 크기가 가장 큰 블록을 찾는다.
            그 순서는 같은 색이 가장 많은 순, 무지개 포함 가장 큰 순, 그래도 같다면 기준블록의 행이 큰 순, 열이 큰 순을 선택한다.
        2. 해당 블록을 모두 제거하고, 그 블록의 수가 B 라면 B^2 점을 획득한다
        3. 격자에 중력을 작용
        4. 90도 반시계방향 회전 후 다시 중력작용
INPUT ) 첫째 줄에 한변의 크기 N, 색상의 개수 M 이 주어진다. ( N : 20 이하 자연수, M: 5 이하 자연수 )
OUTPUT) 모든 작업이 끝난 후 획득 점수를 출력하라
Approach )  
1.블록찾기 bfs
2.중력작용
3.로테이트
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline


n, m = list(map(int, input().split()))
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
d = [[-1, 0, 0, 1], [0, -1, 1, 0]]


def bfs():
    rtable = [[6 for _ in range(n)] for _ in range(n)]

    dic = {i: [0, 0, [0, 0], []] for i in range(m+1)}
    for ix in range(n):
        for iy in range(n):
            if rtable[ix][iy] != 6:
                continue
            if table[ix][iy] == -1 or table[ix][iy] == []:
                if table[ix][iy] == []:
                    continue
                rtable[ix][iy] = -1
                continue
            q = deque()
            node = table[ix][iy]
            rtable[ix][iy] = node
            q.append([ix, iy])
            hist = [[[ix, iy]], []]
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx, ny = x+d[0][i], y+d[1][i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if table[nx][ny] == node and [nx, ny] not in hist[0]:
                            rtable[nx][ny] = node
                            hist[0].append([nx, ny])
                            q.append([nx, ny])
                        elif node != 0 and table[nx][ny] == 0 and [nx, ny] not in hist[1]:
                            # rtable[nx][ny] = 0
                            hist[1].append([nx, ny])
                            q.append([nx, ny])
            block, zblock = len(hist[0]), len(hist[1])+len(hist[0])
            hist = hist[0]+hist[1]
            if dic[node][0] < block:
                dic[node] = [block, zblock, [ix, iy], [i[:] for i in hist]]
            elif dic[node][0] == block and dic[node][1] < zblock:
                dic[node] = [block, zblock, [ix, iy], [i[:] for i in hist]]
    target = [0, 0, [0, 0]]

    def setTarget(lst):
        nonlocal target
        target = lst

    for i in range(1, m+1):
        a, b, c, _ = dic[i]
        if a >= target[0]:
            if a > target[0]:
                setTarget(dic[i])
                continue
            if b >= target[1]:
                if b > target[1]:
                    setTarget(dic[i])
                    continue
                if c[0] <= target[2][0]:
                    if c[0] < target[2][0]:
                        setTarget(dic[i])
                        continue
                    if c[1] > target[2][1]:
                        setTarget(dic[i])
    if target[0] == 0:
        setTarget(dic[0])
        if target[0] == 0:
            return False
    target = target[3]
    for x, y in target:
        table[x][y] = []


while True:
    if bfs() == False:
        break
    xprint(table)
    print()
