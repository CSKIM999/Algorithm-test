import sys
input = sys.stdin.readline

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
                if not hist[bnode] and bnode not in q:
                    q.append(bnode)
    print(result)
dfs(node,v)
bfs(node,v)