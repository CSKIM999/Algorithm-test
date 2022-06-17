
import sys
input = sys.stdin.readline
import heapq

hpush = heapq.heappush
hpop = heapq.heappop
inf = 1e9

N = int(input())
M = int(input())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))
path = list(map(int,input().split()))
start = path[0]-1
dist = [inf]*N
dist[start] = 0

q = []
hpush(q,(0,start))

while q:
    c,node = hpop(q)
    if c>dist[node]:
        continue
    for i in range(N):
        if c+1<dist[i] and data[node][i]:
            hpush(q,(c+1,i))
            dist[i] = c+1

flag = 0
for i in path:
    if dist[i-1] == inf:
        flag = 1
        print('NO')
        break
if not flag:
    print('YES')

