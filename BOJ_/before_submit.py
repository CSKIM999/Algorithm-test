import itertools
from collections import deque
import sys
sys.setrecursionlimit(25000)


input = sys.stdin.readline
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
