from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1260
#######  TODAY  #######
##### 2022. 03. 09 #####
GIVEN ) 그래프를 dfs 로 탐색한 결과와 bfs 로 탐색한 결과를 출력하는 프로그램을 작성하라.
        만약 동시에 여러개의 노드를 방문할 수 있다면 낮은 번호의 노드부터 방문한다.
INPUT ) 첫째 줄에 노드의 개수 N ( 1<= N <= 1,000 ), 간선의 개수 M ( 1 <= M <= 10,000 ), 탐색을 시작할 노드의 번호 V 가 주어진다.
        다음 M 개의 줄에는 간선에 연결된 두 노드가 주어진다.
OUTPUT) 첫째줄에 DFS 의 결과, 둘째 줄에 BFS 의 결과를 출력하라
Approach )  쉬운듯?
'''
# import sys
# input = sys.stdin.readline

from collections import deque

n,m,v = map(int,input().split())

node = [[] for _ in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    node[a].append(b)
    node[b].append(a)

def bfs(given,start):
    for i in range(n+1):
        given[i].sort()
    print(given)
    q = deque(given[start])
    hist = [False for _ in range(n+1)]
    result = f"{start} "
    hist[start] = True
    while q:
        now = q.popleft()
        if not hist[now]:
            result += f"{now} "
            hist[now] = True
            for bnode in given[now]:
                if not hist[bnode]:
                    q.append(bnode)
    print(result)

def dfs(given,start):
    for i in range(n+1):
        given[i].sort(reverse = True)
    q = deque(given[start])
    hist = [False for _ in range(n+1)]
    result = f"{start} "
    hist[start] = True
    while q:
        now = q.pop()
        if not hist[now]:
            result += f"{now} "
            hist[now] = True
            for bnode in given[now]:
                if not hist[bnode]:
                    q.append(bnode)
    print(result)
dfs(node,v)
bfs(node,v)

'''
맞는데 왜 틀리대 ㅅㅂ

'''