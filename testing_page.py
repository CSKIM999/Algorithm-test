from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = [[] for _ in range(n)]
for i in range(n):
    data[i] = list(map(int,input().split()))
virus = []
empty = []
count = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            virus.append([i,j])
        elif data[i][j] == 0:
            empty.append([i,j])
options = list(combinations(empty,3))

def bfs(data,b,h):
    x = [-1,0,1,0]
    y = [0,1,0,-1]
    q = deque()
    q.append([b,h])
    while q:
        check = False
        b,h = q.pop()
        for i in range(4):
            X,Y = x[i],y[i]
            if -1<b+Y<n and -1<h+X<m and (data[b+Y][h+X] !=1 and data[b+Y][h+X] != 2):
                if check == False:
                    q.append([b,h])
                    check = True
                q.append([b+Y,h+X])
                data[b+Y][h+X] = 2
    return data


def test(data,option):
    count = 0
    for i in range(3):
        data[option[i][0]][option[i][1]] = 1
    
    for i in virus:
        x,y = i[0],i[1]
        data = bfs(data,x,y)
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count+=1

    return count

for i in options:
    data_prime = [i[:] for i in data]
    count = max(count,test(data_prime,i))

print(count)
