from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q20057
#######  TODAY  #######
##### 2022. 03. 11 #####
https://www.acmicpc.net/problem/20057
GIVEN ) N*N 격자 안에 토네이도가 움직인다. 각 칸에는 모래가 위치하며 토네이도 움직임에 따라 모래가 움직인다.
        그림에 따른 규칙으로 토네이도는 움직이고, 모래는 흩날려서 해당 위치에 더해진다.
INPUT ) 첫째 줄에 N 이 주어지고 그 뒤 N개의 줄에 테이블의 상태가 주어진다.
OUTPUT) 격자 밖으로 밀어내진 모래의 크기를 출력하라
Approach )  필요한 모듈들
            토네이도 이동 리스트 (무조건 0,0 까지 움직임) [[2,2,2,1]....] << [fromx,fromy,tox,toy]
            이동에 따른 모래 밀어내기 (밀어낼 때 밖으로 떨어지면 즉각 result 에 더하기)

'''
print(f"CORRECT : 22961")

# import sys
# input = sys.stdin.readline


N = int(input())
table = []
for i in range(N):
    table.append(list(map(int,input().split())))
lane = []
S = [N//2,N//2]
c,d = 1,[1,-1]
result = 0
while True: #토네이도 경로반환 [x,y,nx,ny]
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

'''
1트 SOLVE // 엄청 깔끔하고 쉽게 풀렸는데 왠지는 모르겠다. 모듈화도 안했는데 모듈화 할때보다 오히려 더 쉬웠다.
'''