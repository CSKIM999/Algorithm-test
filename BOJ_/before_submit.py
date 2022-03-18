import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
lst = list(map(int,input().split()))
cut = int(input())
data = [[] for _ in range(N)]
root = 0
for i in range(N):
    parent = lst[i]
    if parent == -1:
        root = i
        continue
    if i == cut:
        continue
    data[parent].append(i)
data[cut] = []
q = deque([])
q.append(root)
result = 0

while q:
    Pnode = q.popleft()
    if Pnode == cut:
        continue
    if data[Pnode]:
        for i in data[Pnode]:
            q.append(i)
    else:
        result += 1
print(result)