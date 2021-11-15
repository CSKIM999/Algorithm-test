from collections import deque
import sys
import math
from copy import deepcopy
from itertools import combinations

starts = [(0,1,0),(0,3,0)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

n,c = 7,1
maps = [
    [0,2,0,2,0,0,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1]
]

# maps 안에 0이 있는지 여부. 
# bfs로 모든 바이러스 전파가 끝났는데 0이 남아 있다면 더 이상 바이러스를 퍼뜨릴 수 없다는 의미.
def check(maps):
    for y in range(len(maps)):
        for x in range(len(maps)):
            if maps[y][x] == 0:
                return -1
    return 0

def bfs(start, maps):
    visited = [[0 for _ in range(len(maps))] for _ in range(len(maps))]
    maps = deepcopy(maps)
    queue = deque()

    # start에 들어갈 값이 'n개 바이러스 중 c개를 선택한 모든 경우의 수' 이므로 extend 사용
    queue.extend(start)
    
    # 0이 2로 바뀌는 마지막 순간만을 확인하면 된다. 
    # (비활성 바이러스가 활성화되는 경우는 '빈 칸에 바이러스를 퍼뜨리는' 경우가 아니기 때문)
    
    last_change = 0
    while queue:
        cy, cx, cnt = queue.popleft()
        visited[cy][cx] = 1
        for i in dirs:
            ny, nx = cy+i[0], cx+i[1]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps) and not visited[ny][nx] and maps[ny][nx] != 1:
                visited[ny][nx] = 1
                if maps[ny][nx] == 0:
                    maps[ny][nx] = 2
                    last_change = cnt+1
                queue.append((ny, nx, cnt+1))
    
    # bfs 끝나고 maps 확인. 남아있는 0의 개수가 없어야 한다.
    val = check(maps)
    if val == 0:
        return last_change
    else:
        return -1
    
mins = math.inf

# 바이러스 위치 n개 중 c개를 선택하는 모든 경우의 수
candidates = list(combinations(starts, c))

for value in candidates:
    result = bfs(value, maps)
    if mins > result and result != -1:
        mins = result
        
if mins == math.inf:
    print(-1)
else:
    print(mins)