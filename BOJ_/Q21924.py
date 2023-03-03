import sys
from heapq import *
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q21924
#######  TODAY  #######
##### 2023. 03. 03 #####
GIVEN ) 도시건설
        도시에 도로가 건설되어있고 나는 항상 최소한의 비용으로 모든 도시를 연결한다.
        최소비용 연결을 통해 절약하는 비용을 구하고자 한다.
INPUT ) 첫째 줄에 건물의 개수 N ( 3 <= N <= 100,000 ) 과 간선의 개수 M ( 2<= M <= 100,000 ) 개가 주어진다.
        둘째 줄부터 M 개의 줄에 걸쳐 간선의 정보 a,b,c 가 주어지며 a,b 사이를 잇는 간선의 비용은 c 라는 점.
        c 는 1,000,000 이하의 자연수이다.
OUTPUT) 절약 비용을 출력하라
Approach )  유니온 파인드를 사용.
            입력 받으면서 힙에 넣을때 result 값에 모든 간선값 더해주고 heappop 할때마다 간선값에서 빼주자
'''
sys.setrecursionlimit(25000)


input = sys.stdin.readline
n, m = map(int, input().split())


class construct:
    def __init__(self, n, m):
        self.res = 0
        # self.dic = {i: set() for i in range(n+1)}
        self.group = {i: i for i in range(n+1)}
        self.heap = []
        for _ in range(m):
            a, b, c = map(int, input().split())
            self.res += c
            # self.dic[a].add((c, b))
            heappush(self.heap, (c, a, b))

    def find(self, node):
        if self.group[node] == node:
            return node
        else:
            return self.find(self.group[node])

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a > b:
            a, b, = b, a
        self.group[b] = a

    def play(self):
        while self.heap:
            cost, f, t = heappop(self.heap)
            ff = self.find(f)
            tt = self.find(t)
            if ff != tt:
                self.union(f, t)
                self.res -= cost
        print(self.res)


const = construct(n, m)
const.play()
