import heapq
import sys
input = sys.stdin.readline
hpush = heapq.heappush
hpop = heapq.heappop

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    s, g, h = s-1, g-1, h - 1
    dest = []
    data = [[] for _ in range(n)]
    for i in range(m):
        a, b, d = map(int, input().split())
        a, b = a-1, b-1
        data[a].append((d, b))
        data[b].append((d, a))
    for i in range(t):
        dest.append(int(input()))

    q = [[0, s]]
    dist = [[1e9, 0] for _ in range(n)]
    dist[s] = [0, 0]
    while q:
        nowDist, now = hpop(q)
        if nowDist > dist[now][0]:
            continue
        for x, y in data[now]:

            if dist[y][0] >= dist[now][0] + x:
                if dist[y][0] == dist[now][0] + x:
                    if not dist[now][1] and [y, now] not in [[g, h], [h, g]]:
                        continue
                if dist[now][1] or [y, now] in [[g, h], [h, g]]:
                    dist[y] = [dist[now][0] + x, 1]
                else:
                    dist[y][0] = dist[now][0] + x
                    if dist[y][1]:
                        dist[y][1] = dist[now][1]
                hpush(q, [dist[now][0] + x, y])

    dest.sort()
    answer = []
    for i in dest:
        if dist[i-1][1]:
            answer.append(f'{i}')
    print(' '.join(answer))
