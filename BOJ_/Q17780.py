'''
Given ) N*N 크기의 판에서 K개의 말이 순서에 따라 움직인다. 말은 방향을 가지며 두 개 이상 겹쳐질 수 있으나 순서를 구분한다. 턴 한번에 1번부터 K 번 말까지 순서대로 이동시킨다.
        현재 말이 다음에 이동할 다음칸에 대한 룰은 다음과 같다.
        1. 흰색의 경우 -> 그 칸으로 이동한다. 만약 다른 말이 이미 존재한다면 가장 위에 A번 말을 올려놓는다.
            A번 말의 위에 다른말이 있는경우 모든 말이 함께 이동한다.
            ex ) D,E 말이 이미 존재하고 A,B,C 말이 그 위로 이동한다면 E,D,A,B,C 가 된다.
        2. 빨간색의 경우 -> 이동한 후 이동한 말의 순서가 반대로 바뀐다.
            A,B,C 가 이동하고 이동하려는 칸에 말이 없는 경우 C,B,A 가 위치한다.
            A,D,F,G 가 이동하고, 이동하려는 칸에 E,C,B로 있는 경우에는 E,C,B,G,F,D,A 가 된다.
        3. 파란색의 경우 -> 현재 이동하려는 말의 방향을 반대로 하고 한칸 이동한다.
            만약 반대방향이 막혀 이동할 수 없다면 이동하지 않고 가만히 있는다.
        4. 체스판을 벗어나는 경우
            3번으로 취급하여 처리한다.
Input ) 첫째 줄에 체스판의 크기 N, 말의 개수 K 이 주어진다.
        둘째 줄부터 N개의 줄에 걸쳐 체스판의 정보가 주어진다. 0은 흰색, 1 은 빨간색, 2는 파란색을 의미한다.
        다음 K 개의 줄에 말의 정보가 1번부터 순서대로 주어진다. 각 행은 순서대로 행,열,방향 이 주어진다.
        방향은 1,2,3,4 순서로 동,서,북,남 방향이다.
Output) 한 칸에 말이 4개 이상 올라간다면 그 즉시 게임은 종료된다.
        게임이 종료되는 턴의 번호를 출력한다. 그 값이 1000을 넘어간다면, -1을 출력한다.
'''

def xprint(a):
    for i in a:
        print(i)

n,k = 4,4
data = [
    [0, 0, 2, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 2],
    [0, 2, 0, 0]
]
dot = [[1,0,0],[2,1,2],[1,1,0],[3,0,1]]
direction = [[0,1],[0,-1],[-1,0],[1,0]]

# n,k = map(int,input().split())
# data = []
# dot = []
# for i in range(n):
#     data.append(list(map(int,input().split())))
# for j in range(k):
#     a,b,c = map(int,input().split())
#     dot.append([a-1,b-1,c-1])

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
    global dot
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
    global dot
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
    global dot
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
    global dot
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

# while True:
#     operation(dot)
#     if flag == False:
#         break
#     if result > 1000:
#         result = -1
#         break
#     result += 1
nodeAct = [True]*n
print(socket[2][1])
def W(dotIndex):
    x,y,d = dot[dotIndex]
    nx,ny = x+direction[d][0],y+direction[d][1]
    nfs = socket[x][y][:]
    for node in nfs:
        d = dot[node][2]
        dot[node] = [nx,ny,d]
    if not socket[nx][ny]:
        nodeAct[dotIndex-1] = False
    socket[nx][ny] += (socket[x][y][:])
    del socket[x][y][:]

def R(dotIndex):
    x,y,d = dot[dotIndex]
    nx,ny = x+direction[d][0],y+direction[d][1]
    nfs = socket[x][y][:]
    for node in nfs:
        d = dot[node][2]
        dot[node] = [nx,ny,d]
    if not socket[nx][ny]:
        nodeAct[dotIndex-1] =False
    else:
        nodeAct[dotIndex-1] = False
        
    socket[nx][ny] += list(reversed(socket[x][y][:]))
    del socket[x][y][:]

def B(dotIndex):
    x,y,d = dot[dotIndex]
    if d%2 == 1:
        d-=1
    else:
        d+=1
    dot[dotIndex][2] = d
    nx,ny = x+direction[d][0],y+direction[d][1]
    if data[nx+1][ny+1] == 2:
        return
    elif data[nx+1][ny+1] == 1:
        R(dotIndex)
    else:
        W(dotIndex)