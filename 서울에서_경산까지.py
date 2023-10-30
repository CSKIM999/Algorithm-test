from collections import deque
n,k = list(map(int,input().split()))
walk = []
bike = []
for _ in range(n):
    a,b,c,d = list(map(int,input().split()))
    walk.append([a,b])
    bike.append([c,d])

q = deque()
q.append([-1,0,0])
while q:
    nowIndex,nowTime,nowValue = q.popleft()
    nowIndex += 1
    if nowIndex == n:
        pass
    wt,wv = walk[nowIndex]
    if nowTime + wt <= k:
        q.append([nowIndex,nowTime+wt,nowValue+wv])
    bt,bv = bike[nowIndex]
    if nowTime + bt <= k:
        q.append([nowIndex, nowTime+bt, nowValue + bv])
