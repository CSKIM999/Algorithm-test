from heapq import *
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


class construct:
    def __init__(self, n, m):
        self.res = 0
        self.group = {i: i for i in range(n+1)}
        self.heap = []
        for _ in range(m):
            a, b, c = map(int, input().split())
            self.res += c

            heappush(self.heap, (c, a, b))

    def find(self, node):
        if self.group[node] == node:
            return node
        else:
            self.group[node] = self.find(self.group[node])
            return self.group[node]

    def union(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        self.group[max(aa, bb)] = min(aa, bb)

    def check(self, a, b):
        return self.find(a) != self.find(b)

    def play(self):
        while self.heap:
            cost, f, t = heappop(self.heap)
            if self.check(f, t):
                self.union(f, t)
                self.res -= cost
        temp = set()
        for i in range(1, n+1):
            temp.add(self.find(i))
        if len(temp) > 1:
            print(-1)
        else:
            print(self.res)


const = construct(n, m)
const.play()
