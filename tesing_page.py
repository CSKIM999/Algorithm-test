direction = [[0,1],[0,-1],[-1,0],[1,0]]

n,k = map(int,input().split())
data = []
dot = []
for i in range(n):
    data.append(list(map(int,input().split())))
for j in range(k):
    a,b,c = map(int,input().split())
    dot.append([a-1,b-1,c-1])
for i in range(n):
    data[i] = [2]+data[i]+[2]
data = [[2]*(n+2)] + data + [[2]*(n+2)]
socket = [[[] for _ in range(n)] for _ in range(n)]
for i,a in enumerate(dot):
    x,y,d =a
    socket[x][y].append(i)
flag = True
result = 1


def check():
    for i in range(n):
        for j in range(n):
            if len(socket[i][j]) >= 4:
                return False
    return True

def white(idx):
    x,y,d = dot[idx]
    I = socket[x][y].index(idx)
    nx,ny = x+direction[d][0],y+direction[d][1]
    C = socket[x][y][I:]
    for n1 in C:
        nd = dot[n1][2]
        dot[n1] = [nx,ny,nd]
    dot[idx] = [nx,ny,d]
    socket[nx][ny] += (socket[x][y][I:])
    del socket[x][y][I:]

def red(idx):
    x,y,d = dot[idx]
    I = socket[x][y].index(idx)
    nx,ny = x+direction[d][0],y+direction[d][1]
    C = socket[x][y][I:]
    for n1 in C:
        nd = dot[n1][2]
        dot[n1] = [nx,ny,nd]
    socket[nx][ny] += list(reversed(socket[x][y][I:]))
    del socket[x][y][I:]

def blue(idx):
    x,y,d = dot[idx]
    if d%2 == 1:
        d-=1
    else:
        d+=1
    dot[idx] = [x,y,d]
    nx,ny = x+direction[d][0],y+direction[d][1]
    if data[nx+1][ny+1] == 2:
        return
    elif data[nx+1][ny+1] == 1:
        red(idx)
    else:
        white(idx)

def operation(lst):
    global flag
    for i in range(len(lst)):
        x,y,d = lst[i]
        nx,ny = x+direction[d][0],y+direction[d][1]
        if data[nx+1][ny+1] == 1:
            red(i)
        elif data[nx+1][ny+1] == 2:
            blue(i)
        else:
            white(i)
        if not check():
            flag = False
            break


while True:
    operation(dot)
    if flag == False:
        break
    if result > 1000:
        result = -1
        break
    result += 1

print(result)