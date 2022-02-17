'''
Given ) N*N 크기의 격자 안에 M마리의 상어가 들어있다.
        각 상어들은 매 움직임마다 냄새를 남기고 그 냄새는 k 번 이동후에 사라진다.
        각 상어들은 현재 바라보는 방향에 따라 각각의 우선순위 방향을 가진다
        이동방향을 결정할 때의 규칙은 다음과 같다.
            인접한 칸으로만 이동할 수 있다.
            1.인접 칸중 아무냄새가 없는 칸
            2.자신의 냄새가 있는 칸
        바라보는 방향은 바로 직전에 움직인 방향을 따른다.
        만약 이동이 끝난 후 격자에 상어가 2마리 이상 위치한다면, 가장 작은 번호의 상어를 제외하고 모두 쫒겨난다.
        ( 2<= N <= 20  //&&//  2 <= M <= N**2  //&&//  1 <= k <= 1,000 )
        첫째 줄에 N,M,K 가 주어지고 그 이후 N 개의 줄에 걸쳐 격자의 모습이 주어진다.
        그 다음 각 상어의 방향이 4줄에 걸쳐 차례대로 주어진다
            1번째 줄 : 위를 향할때의 우선순위
            2번째 줄 : 아래를 향할때의 우선순위
            3번째 줄 : 왼쪽를 향할때의 우선순위
            4번째 줄 : 오른쪽를 향할때의 우선순위
            각 줄에는 4개의 자연수가 주어지며 1 3 2 4 라면 [위,왼쪽,아래,오른쪽] 순서인 셈
        
        맨 처음 주어지는 세팅값은 각 상어마다 무조건 인접빈칸이 존재한다.

        이를통해 1번 상어만 격자에 남게 되는 시간을 출력하라. 만약 1,000이 넘는다면 -1을 출력하라.

Approach >> 사용하게 될 function들을 먼저 정리해보자
            G : 상어리스트 // 만약 제외되면 이 리스트에서 해당 인덱스 제거
                상어의 방향리스트 // 3차원 리스트로 관리    
            1. 각 상어의 다음 이동칸 list return
            2. 상어들의 이동 ( 이동과 함께 냄새를 묻히기 )
            3. 테이블 순회 후 냄새 지속시간 -1
            순서도 1,2,3 순서를 따르게 구현해보자

'''
from lib import xprint

n,m,k = map(int,input().split())
d = [[-1,0],[1,0],[0,-1],[0,1]]

table = [[0]*n for _ in range(n)]
table = []
for i in range(n):
    table.append(list(map(int,input().split())))
nodes = list(map(int,input().split()))
Shark = [[] for _ in range(m)]
for i in range(n):
    for j in range(n):
        if table[i][j]:
            now = table[i][j] - 1
            Shark[now] = [i,j,nodes[now]-1]
            table[i][j] = [now,k]
# Shark = [[2,0,3],[1,1,3],[0,4,2],[2,4,0]]
# for i in range(m):
#     a,b,c = Shark[i]
#     table[a][b] = [i,k]

SharkDlst = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        temp = []
        temp = list(map(int,input().split()))
        for q in range(len(temp)):
            temp[q] = temp[q] -1
        SharkDlst[i].append(temp)

def getNextNode(Slst):
    # todo...  shark 리스트 순회해서 각 상어의 방향에 따른 다음 방문예정 노드리스트 반환
    tlst = []
    for i in range(m):
        if Slst[i]: # 상어가 제외되지 않았다
            x,y,Nd = Slst[i]
            Ndnumlst = SharkDlst[i][Nd]
            zflag,hflag = False,False
            z,h=[],[]
            for a in Ndnumlst:
                ax,ay = d[a]
                nx,ny = x+ax,y+ay
                if not 0<=nx<n or not 0<=ny<n:
                    continue
                if table[nx][ny] == 0 and not zflag:
                    # 아직 빈칸을 못만났다
                    zflag = True
                    z = [nx,ny,a]
                if table[nx][ny] != 0 and table[nx][ny][0] == i and not hflag:
                    # 아직 내가 자취를 못만났다
                    hflag = True
                    h = [nx,ny,a]
            if z:
                tlst.append(z)
            else:
                tlst.append(h)
        else:
            tlst.append([])
    return tlst

def moveSharks(mlst):
    temp = []
    for i in range(m):
        if mlst[i]:
            a,b,c = mlst[i]
            if (a,b) in temp:
                Shark[i] = []
                continue
            temp.append((a,b))
            table[a][b] = [i,k+1]
            Shark[i] = mlst[i]

def check():
    cC = 0
    for i in Shark:
        if i:
            cC+=1
    if cC == 1:
        return False
    else:
        return True

def flow():
    for i in range(n):
        for j in range(n):
            if table[i][j]:
                table[i][j][1] -=1
                if table[i][j][1] == 0:
                    table[i][j] = 0

Count = 0
flag = True
while flag:
    Count += 1
    moveSharks(getNextNode(Shark))
    flow()
    flag = check()
    if Count > 1000:
        flag = False
        Count = -1

print(Count)

# xprint(table)
# print(Shark)

'''
1트 SOLVE
'''