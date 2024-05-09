'''
위상정렬 알고리즘 사용
1. 진입차수가 0인 정점을 큐에 삽입
2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거
3. 간선 제거 이후 진입차수가 0이 된 정점을 큐에 삽입
4. 큐가 빌 때까지 2-3 반복
'''
from collections import deque
n,m = list(map(int,input().split()))
hist = set([i for i in range(1,n+1)])
check = [0 for _ in range(n+1)]
child = [[] for _ in range(n+1)]
answer = []
for _ in range(m):
    a,b = list(map(int,input().split()))
    child[a].append(b)
    check[b] += 1

while hist:
    q = deque()
    for i in hist:
        if check[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        hist.remove(now)
        answer.append(now)
        nowChild = child[now]
        for x in nowChild:
            check[x] -= 1

print(' '.join(map(str, answer)))