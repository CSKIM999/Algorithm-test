
import heapq
import sys
qpush, qpop = heapq.heappush, heapq.heappop
input = sys.stdin.readline
n, m, x = list(map(int, input().split()))
dist = {i: [] for i in range(n+1)}
for i in range(m):
    a, b, c = list(map(int, input().split()))
    dist[a].append((c, b))


def dijkstra(now, togo=None):
    q = []
    qpush(q, (0, now))
    table = {i: 1e9 for i in range(n+1)}
    table[now] = 0
    if togo != None:
        while q:
            cost, node = qpop(q)
            if table[togo] != 1e9 and cost > table[togo]:
                continue

            for nc, nn in dist[node]:
                if nc+cost < table[nn]:
                    table[nn] = nc+cost
                    qpush(q, (nc+cost, nn))
        return table[togo]
    else:
        while q:
            cost, node = qpop(q)
            for nc, nn in dist[node]:
                if nc+cost < table[nn]:
                    table[nn] = nc+cost
                    qpush(q, (nc+cost, nn))
        return table


Xtable = dijkstra(x)
result = 0
for i in range(1, n+1):
    if i == x:
        continue
    toX = dijkstra(i, x)
    if result < toX + Xtable[i]:
        result = toX+Xtable[i]
print(result)
