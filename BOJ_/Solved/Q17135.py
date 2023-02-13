import itertools
from collections import deque
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q17135
#######  TODAY  #######
##### 2023. 02. 13 #####
GIVEN ) N,M 격자판 안에 적 혹은 빈칸이 존재한다
        N행의 바로 아래는 성이 존재하여 성 위에는 궁수를 배치할 수 있다
        하나의 칸에는 최대 1명의 궁수만 존재할 수 있고
        각 턴마다 궁수는 사거리 내에 가장 가까운, 만약 둘 이상이라면 가장 왼쪽의
        적을 공격한다.
        모든 궁수는 동시에 공격하며 적도 동시에 여러 궁수에게 공격받을 수 있다.
        적이 성이 있는 칸에 도달하면 사라지며, 모든 적이 사라지거나 공격받아 제거되면
        게임은 종료된다.
        궁수가 처치할 수 있는 최대 적의 수를 구하라.
INPUT ) 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 사정거리 D 가 주어진다.
        이후 N 개의 줄에 걸쳐 격자판의 상태 ( 0 은 빈칸, 1 은 적 ) 이 주어진다.
OUTPUT) 최대로 제거할 수 있는 적의 수를 구하라.
Approach )
    그냥 빡구현같음. 경우의 수가 많지 않음.
'''
sys.setrecursionlimit(25000)

# input = sys.stdin.readline
n, m, d = list(map(int, input().split()))
tableInput = [list(map(int, input().split())) for _ in range(n)]
tableEnemies = set()
comb = list(itertools.combinations(range(m), 3))
for i in range(n):
    for j in range(m):
        if tableInput[i][j]:
            tableInput[i][j] = (i, j)
            tableEnemies.add((i, j))


class newSimul:
    def __init__(self):
        self.table = [i[:] for i in tableInput]
        self.enemies = tableEnemies.copy()
        self.archors = []
        self.dx = [[0, -1], [-1, 0], [0, 1]]
        self.dist = d
        self.point = 0
        pass

    def position(self, archors):
        self.archors = archors[:]

    def eMove(self):
        for i in self.table[-1]:
            if i:
                self.enemies.remove(i)
        self.table = [[0]*m, *self.table[:-1]]

    def aim(self):
        target = set()
        for archor in self.archors:
            q = deque()
            hist = set()
            hist.add((n-1, archor))
            q.append((n-1, archor, 1))
            while q:
                x, y, dist = q.popleft()
                if dist > self.dist:
                    continue
                if self.table[x][y]:
                    target.add((x, y))
                    break
                else:
                    for i, j in self.dx:
                        nx, ny = x+i, y+j
                        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in hist:
                            hist.add((nx, ny))
                            q.append((nx, ny, dist+1))
        for x, y in target:
            v = self.table[x][y]
            self.enemies.remove(v)
            self.table[x][y] = 0
            self.point += 1

    def play(self):
        while self.enemies:
            self.aim()
            self.eMove()
        return self.point


answer = 0
for pos in comb:
    now = newSimul()
    now.position(pos)
    value = now.play()
    answer = max(value, answer)

print(answer)

'''
1트 solve

직전에 class 사용한 tire 문제 풀었는데 class 가 생각보다 좋은 점이 많아서
이번에도 class 로 풀어보니 푸는시간은 좀 걸렸어도 채점에서 아주 넉넉하게 시간도 통과하고
풀때도 분리해서 구현하기 편해서 좋은듯? 👀👍

'''
