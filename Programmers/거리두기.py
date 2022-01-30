from collections import deque
table = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

d = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs2(x,y,given):
    q = deque([(x,y,0)])
    flag = 0
    visit = [(x,y)]
    while q:
        x,y,c = q.popleft()
        if c == 2:
            continue
        for a,b in d:
            nx,ny = x+a,y+b
            if 0<=nx<5 and 0<=ny<5 and ((nx,ny) not in visit):
                if given[nx][ny] == 'P':
                    flag = 1
                    q = []
                    break
                if given[nx][ny] == 'X':
                    visit.append((nx,ny))
                    continue
                visit.append((nx,ny))
                q.append((nx,ny,c+1))
        
        if flag:
            return False
    return True

for i in range(len(table)):
    now = table[i]
    flag = 0
    result = 1
    for j in range(5):
        for k in range(5):
            if now[j][k] == 'P':
                if not flag:
                    if not bfs2(j,k,now):
                        flag = 1
                        result = 0
    print(result)



