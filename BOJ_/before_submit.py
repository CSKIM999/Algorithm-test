import sys
input = sys.stdin.readline
from collections import deque

table = []
for _ in range(8):
    a = list(input().strip())
    temp = []
    for i in a:
        if i == "#":
            temp.append(1)
        else:
            temp.append(0)
    table.append(temp)
case = []
case.append(table)

for i in range(1,9):
    temp = []
    for j in range(i):
        temp.append([0]*8)
    temp.extend(table[:-i])
    case.append(temp)

def sol():
    q = deque()
    q.append([7,0,0])
    while q:
        x,y,sec = q.popleft()
        for i in range(-1,2):
            for j in range(-1,2):
                nx,ny = x+i,y+j
                if 0<= nx < 8 and 0<= ny < 8:
                    try:
                        if not case[sec+1][nx][ny] and not case[sec][nx][ny]:
                            if nx==0 and ny ==7:
                                return 1
                            q.append([nx,ny,sec+1])
                    except IndexError:
                        return 1
    return 0

print(sol())
