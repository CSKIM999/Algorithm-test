import heapq as h
n = 7
path = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [
    2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]

hpush = h.heappush
hpop = h.heappop
dist = {i: [] for i in range(n+1)}

for t, f, d in path:
    dist[t].append([d, f])
    dist[f].append([d, t])
gates.sort()
summits.sort()
gates = set(gates)


def dijkstra(start, summit=False):
    temp = [1e9]*(n+1)
    q = [[0, start]]
    temp[start] = 0
    while q:
        point, node = hpop(q)
        if temp[node] < point:  # or end?
            continue
        for a, b in dist[node]:
            if summit and b != summit and b in summits:
                continue
            a = max(a, point)
            if temp[b] > a:
                hpush(q, [a, b])
                temp[b] = a

    return temp


answer = [0, 1e9]
sdic = {i: {} for i in summits}
gdic = {i: {} for i in gates}
for summit in summits:
    gtable = dijkstra(summit, summit)
    for gate in gates:
        sdic[summit][gate] = gtable[gate]

for gate in gates:
    stable = dijkstra(gate)


# for summit in summits:
#     gtable = dijkstra(summit, summit)
#     for gate in gates:
#         if gtable[gate] > answer[1]:
#             continue
#         m = max(gtable[gate], dijkstra(gate)[summit])
#         if answer and answer[1] > m:
#             answer = [summit, m]

print(sdic)
