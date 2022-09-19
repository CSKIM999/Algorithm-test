import heapq
import sys
input = sys.stdin.readline
push = heapq.heappush
hpop = heapq.heappop


n, m, r = map(int, input().split())
table = list(map(int, input().split()))
lane = [[] for _ in range(n)]

for i in range(r):
    a, b, c = map(int, input().split())
    lane[a-1].append([c, b-1])
    lane[b-1].append([c, a-1])


def dijkstra(targetNode):
    t = targetNode
    dist = [1e9 for _ in range(n)]
    q = []
    push(q, [0, t])

    while q:
        far, node = hpop(q)
        if dist[node] <= far:
            continue
        dist[node] = far
        for xdist, x in lane[node]:
            cost = xdist+far
            if cost > m:
                continue
            if cost < dist[x]:
                push(q, [cost, x])
    result = 0
    for i in range(n):
        if dist[i] != 1e9:
            result += table[i]
    return result


ans = 0
for i in range(n):
    ans = max(ans, dijkstra(i))
print(ans)
n, m = list(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
res = 1e10
h, t = 0, 1
while True:
    d = lst[t]-lst[h]
    if d < m:
        if t < n-1:
            t += 1
        else:
            h += 1
            if h == t:
                break
    elif d > m:
        res = min(d, res)
        h += 1
        if h == t:
            if t < n-1:
                t += 1
            else:
                break
    elif d == m:
        res = m
        break
print(res)
