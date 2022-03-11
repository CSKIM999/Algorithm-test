from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q20056
#######  TODAY  #######
##### 2022. 03. 10 #####
GIVEN ) N*N 크기의 공간안에 M 개의 파이어볼이 위치한다.
        공간의 위 아래는 연결되어 N+1 = 0, -1 = N 이 되고 방향은 시계방향으로 0~7로 간주한다
        각각의 파이어볼은 r행 c열에 위치하고 질량m, 방향d, 속력s 를 갖는다.
        각 움직임마다 각각의 파이어볼은 다음과같이 행동한다.
        1. 모든 파이어볼이 di 로 si만큼 이동한다. < 이동 중 한 칸에 여러개의 파이어볼이 위치할 수 있다 >
        2. 이동이 모두 끝난 뒤 2개 이상의 파이어볼이 있는 칸은 다음의 규칙을 따른다.
            2.1. 같은 칸에 있는 모든 파이어볼은 합쳐진다.
            2.2. 합쳐진 파이어볼은 무조건 4개로 나뉘어진다.
            2.3. 나누어지는 파이어볼의 m,s,d 는 다음을 따른다.
                2.3.1. 질량은 floor(sum(m)/5)
                2.3.2. 속도는 floor((sum(s)/sum(fireball count)))
                2.3.3. 방향은 합쳐진 모든 파이어볼의 방향이 홀수 혹은 짝수라면 직각으로 아니라면 대각으로 발사된다
                2.3.4. 질량이 0 인 파이어볼은 소멸된다.

        상어가 K 번 명령 후 남아있는 파이어볼의 질량합을 구하라
INPUT ) 첫째 줄에 N,M,K 가 주어진다
        둘째 줄부터 M 개의 줄에 파이어볼의 정보가 하나씩 주어진다.
            파이어볼의 정보는 r,c,m,s,d 순서로 주어진다
        서로 다른 파이어볼의 위치가 같은 경우는 주어지지 않는다.
OUTPUT) 이동이 완전히 끝난 후 남은 파이어볼의 질량합을 출력하라
Approach )  구현문제. 따라서 각각의 행동을 모듈화하여 구현하자
            1. move < 각 파이어볼이 d 방향으로 s 만큼 이동
            2. 공간을 순회하여 2개 이상 들어있는 칸 탐색
            3. 파이어볼 나누기
                1.질량 합을 5로 나누어 내림 하기.
                1.1. 만약 0이라면 현재 공간 청소
                2.속도 계산해서 각각으로 나누기
                3. 첫번째 d 가 홀수라면 나머지 %2 해서 1 나와야 대각
                    짝수라면 %2 해서 0 나와야 대각
                    나머진 직각
            
'''
# import sys
# input = sys.stdin.readline

from math import floor
N,M,K = list(map(int,input().split()))
table = [[[] for _ in range(N)] for _ in range(N)]
nd = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
for i in range(M):
    r,c,m,s,d = list(map(int,input().split()))
    table[r-1][c-1].append([m,s,d])

def move_detail(r,c,i): #m,s,d
    m,s,d = table[r][c][i]
    t = []
    temp = [r+nd[d][0]*s,c+nd[d][1]*s]
    for q in temp:
        if q<0:
            t.append(N-(-q%N))
        elif q>=N:
            t.append(q%N)
            pass
        else:
            t.append(q)
    nx,ny = t
    return nx,ny,m,s,d

def check():
    Clst = []
    for i in range(N):
        for j in range(N):
            if len(table[i][j]) >1:
                Clst.append([i,j])
    return Clst

def move():
    given = []
    for i in range(N):
        for j in range(N):
            if table[i][j]:
                for k in range(len(table[i][j])):
                    nx,ny,m,s,d = move_detail(i,j,k)
                    given.append([nx,ny,m,s,d])
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for alpha in given:
        nx,ny,m,s,d = alpha
        temp[nx][ny].append([m,s,d])
    return temp

for _ in range(K):
    print("BEFORE")
    xprint(table)
    table = move()
    lst = check()
    L = len(lst)+1
    for x,y in lst:
        M = floor(sum([k[0] for k in table[x][y]])/5)
        if not M:
            table[x][y] = []
            continue
        S = floor(sum([k[1] for k in table[x][y]])/L)
        D = [k[2] for k in table[x][y]]
        flag = True
        table[x][y] = []
        if D[0]%2 == 1:
            for z in D:
                if z%2 !=1:
                    flag = False
                    break
        else:
            for z in D:
                if z%2 != 0:
                    flag = False
                    break
        if flag:
            for d in range(0,7,2):
                table[x][y].append([M,S,d])
        else:
            for d in range(1,8,2):
                table[x][y].append([M,S,d])
    print("AFTER")
    xprint(table)
result = 0
def calcul():
    global result
    for i in range(N):
        for j in range(N):
            result += sum([k[0] for k in table[i][j]])
    print(result)

calcul()