import sys
from collections import deque
input = sys.stdin.readline

q = deque()
N, K = map(int,input().split())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))
res = [[1e19]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            res[i][j] = min(res[i][j],data[i][j],data[i][k]+data[k][j])

a = [0]*N
a[K] =1
result = 1e19
basic = ''.join(map(str,a))
q.append([0,K,basic])

while q:
    count,now, bit  = q.popleft()
    if bit == '1'*N:
        result = min(count,result)
        continue

    if result != 1e19:
        if count > result:
            continue
    
    bit = list(map(int,bit))
    for i in range(N):

        if i == now:
            continue

        temp = bit[:]
        if not bit[i]:
            temp[i] = 1
            q.append([count+res[now][i],i,''.join(map(str,temp))])

print(result)