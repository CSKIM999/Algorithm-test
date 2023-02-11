from collections import deque
import sys
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
bl = len(bomb)
answer = ""
q = deque(string)
compare = deque()
qi = deque()
while q:
    now = q.popleft()
    compare.append(now)
    if len(compare) > bl:
        cleft = compare.popleft()
        qi.append(cleft)
    if ''.join(compare) == bomb:
        compare = deque()
        try:
            for _ in range(bl-1):
                compare.appendleft(qi.pop())
        except IndexError:
            continue
while compare:
    qi.append(compare.popleft())
answer = ''.join(qi)
if answer == '':
    answer = "FRULA"
print(answer)
