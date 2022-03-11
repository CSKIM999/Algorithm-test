import sys
input = sys.stdin.readline
N = int(input())
table = []
for i in range(N):
    table.append(list(map(int,input().split())))
lane = []
S = [N//2,N//2]
c,d = 1,[1,-1]
result = 0
while True:
    for i in range(1,c+1):
        lane.append([S[0],S[1],S[0],S[1]+d[1]])
        S = [S[0],S[1]+d[1]]
    for i in range(1,c+1):
        lane.append([S[0],S[1],S[0]+d[0],S[1]])
        S = [S[0]+d[0],S[1]]
    d = [d[0]*-1,d[1]*-1]
    c +=1
    if c == N:
        for i in range(1,c):
            lane.append([S[0],S[1],S[0],S[1]+d[1]])
            S = [S[0],S[1]+d[1]]
        break
def move(lst):
    global result
    x,y,nx,ny = lst
    new = table[nx][ny]
    s = list(map(int,[(new*0.05),(new*0.1),(new*0.1),(new*0.07),(new*0.07),(new*0.02),(new*0.02),(new*0.01),(new*0.01)]))
    new = new-sum(s)
    d = [[0,2],[1,1],[-1,1],[1,0],[-1,0],[2,0],[-2,0],[-1,-1],[1,-1]]
    if y!=ny: #가로이동의 경우
        iD = ny-y
        table[nx][ny] = 0
        if not 0<= ny+iD < N:
            result += new
        else:
            table[nx][ny+iD] += new
        for i in range(len(d)):
            if not 0<= nx+d[i][0]*iD<N or not 0<= ny+d[i][1]*iD < N:
                result += s[i]
                continue
            table[nx+d[i][0]*iD][ny+d[i][1]*iD] += s[i]
    else: #세로이동
        iD = nx-x
        table[nx][ny] = 0
        if not 0<= nx+iD < N:
            result += new
        else:
            table[nx+iD][ny] += new
        for i in range(len(d)):
            if not 0<= nx+d[i][1]*iD <N or not 0<= ny+d[i][0]*iD<N:
                result += s[i]
                continue
            table[nx+d[i][1]*iD][ny+d[i][0]*iD] += s[i]
for i in lane:
    move(i)
print(result)