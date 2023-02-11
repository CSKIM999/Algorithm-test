import sys
from collections import deque
# import bisect
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
i = 0
bl = len(bomb)
bombed = set()
answer = ""
q = deque()
qi = deque()
l = len(string)
while string:
    if i + bl - len(q) > l:
        break
    if i in bombed:
        i += 1
        continue
    q.append(string[i])
    qi.append(i)
    if len(q) > bl:
        q.popleft()
        qi.popleft()
    if ''.join(q) == bomb:
        while qi:
            bombed.add(qi.popleft())
        q = deque()
        i -= bl
        if i < 0:
            i = 0
    else:
        i += 1
if len(bombed) == len(string):
    answer = "FRULA"
else:
    for i in range(l):
        if i not in bombed:
            answer += string[i]

print(answer)
