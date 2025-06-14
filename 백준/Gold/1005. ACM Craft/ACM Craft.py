import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    build_times = list(map(int, input().split()))

    # 일반 dict로 인접 리스트 초기화
    adj = {i: [] for i in range(1, n + 1)}
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for _ in range(k):
        src, dst = map(int, input().split())
        adj[src].append(dst)
        indegree[dst] += 1

    w = int(input())
    # 초기 진입차수 0인 노드 큐에 추가
    queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    for node in queue:
        dp[node] = build_times[node - 1]

    while queue:
        node = queue.popleft()
        for nxt in adj[node]:
            dp[nxt] = max(dp[nxt], dp[node] + build_times[nxt - 1])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    print(dp[w])
