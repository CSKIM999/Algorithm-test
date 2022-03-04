import sys
from collections import deque 
input = sys.stdin.readline



n,k = map(int,input().split())
J = []
bP = []
for i in range(n):
    a,b = list(map(int,input().split()))
    J.append(tuple([b,a]))
for i in range(k):
    a = int(input())
    bP.append((a))

J.sort(reverse=True)
bP.sort()
q = deque(J)
result = 0
while q:

    if len(bP) == 0:
        break
    V,M = q.popleft()
    if M > bP[-1]:
        continue
    end = len(bP)-1
    start = 0
    # 이분탐색 시작
    while True:
        mid = (end-start)//2
        if bP[mid] >= M:
            end = mid
        else:
            start = mid

        if end-start <= 1:
            if bP[start]>M:
                node = start
                del bP[start]
            else:
                node = end
                del bP[end]
            result += V
            break

print(result)