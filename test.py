from collections import deque
n,m,k = list(map(int,input().split()))
table = [list(map(int,input().split())) for _ in range(n)]
person = []
for _ in range(m):
    a,b = list(map(int,input().split()))
    person.append([a-1,b-1])
pl = len(person)
a,b = list(map(int,input().split()))
exit = [a-1,b-1]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def transCoord(x,y,dist):
    nx = dist - x
    ny = y
    return [ny,nx]

def calAbs(x,y):
    ex,ey = exit
    return (abs(ex-x) + abs(ey-y))

def checkPerson():
    ex,ey = exit
    dist = 0
    while True:
        dist += 1
        for i in range(-dist,dist+1,1):
            for j in range(-dist,dist+1,1):
                if i == 0 and j == 0:
                    continue
                nex,ney = ex+i,ey+j
                if [nex,ney] in person:
                    return (nex,ney,dist)

def getRec(i,j,dist):
    ex,ey = exit
    rx,ry = 1e9,1e9
    if ex <= i:
        rx = i-dist
    else:
        rx = ex-dist
    if ey <= j:
        ry = j - dist
    else:
        ry = j - dist
    return (rx,ry,dist)

def rot(i,j,dist):
    global exit,person
    rec = [k[j:j+dist+1] for k in table[i:i+dist+1]]
    newRec = []
    print('b4',exit)
    print('b4',person)
    newPerson = []
    newExit = [-1,-1]
    for k in range(i+dist+1):
        temp = []
        for l in range(j+dist,j-1,-1):
            if table[l][k] == 0:
                if [l,k] in person:
                    nl,nk = transCoord(l,k,dist)
                    newPerson.append([nl,nk])
                elif [l,k] == exit:
                    nl,nk = transCoord(l,k,dist)
                    newExit = [nl,nk]
                temp.append(0)
            else:
                now = rec[l][k]
                if now > 0:
                    now -= 1
                temp.append(now)
        newRec.append(temp)
    if newPerson:
        person = newPerson[:]
    if newExit:
        exit = newExit
    print(rec)
    print(newRec)
    print("after",exit)
    print("after",person)

def personMove(x,y):
    now = calAbs(x,y)
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and table[nx][ny] == 0:
            new = calAbs(nx,ny)
            if new < now:
                return [nx,ny]
    return [-1,-1]

time = 0
while time < 1:
    time += 1
    for i in range(pl):
        x,y = person[i]
        nx,ny = personMove(x,y)
        if nx == -1:
            continue
        else:
            person[i] = [nx,ny]
    a,b,c = checkPerson()
    a,b,c = getRec(a,b,c)
    rot(a,b,c)