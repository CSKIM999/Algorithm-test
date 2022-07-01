from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q20058
#######  TODAY  #######
##### 2022. 07. 01 #####
GIVEN ) 마법사상어와 파이어스톰
        마법사상어가 2^N * 2^N 크기의 얼음판위에서 파이어스톰을 연습한다.
        매 파이어스톰을 시전할때마다 단계 L 을 결정한다. 이는 얼음판을 2^L*2^L 크기로 나눈 후
        모든 각각의 격자를 90도 시계방향으로 회전 후 얼음 3개 이상과 인접하지 않은 칸이 1씩 줄어드는 마법이다.
        각각의 칸에 위치한 정수는 얼음의 양을 의미하며 0 은 얼음이 없음을 의미한다.
        모든 마법이 끝나고 남아있는 얼음의 합과 그 중 가장 큰 덩어리의 크기를 구하라
INPUT ) 첫 번째 줄에 N,Q 가 주어진다. (2<=N<=6 , 1<= Q <= 1,000 )
        둘째 줄부터 얼음판의 데이터가 빈칸으로 구분되어 주어진다. 0 혹은 100 이하의 자연수
        마지막 줄에 마법사가 시전하는 마법의 단계들이 총 Q 개 주어진다.
OUTPUT) 첫째 줄에 남은 얼음의 합, 둘째 줄에 가장 큰 덩어리의 칸 개수를 출력하라. 만약 덩어리가 없다면 0 을 출력하라

Approach ) 
모듈 1 - 마법모듈
    모듈(N)
        i in 레인지(0,x,N)
            임시 = []
            j in 레인지(0,y,N)
                임시 = [ q[j:j+2] for q in 데이터[i:i+2]]
                for k in range(N):


얼음녹이기

모듈 2 - 유니온파인드
'''
import sys
from collections import deque
sys.setrecursionlimit(25000)
input = sys.stdin.readline
d = [[1,0],[0,-1],[0,1],[-1,0]]
N,Q = map(int,input().split())
table = []
X = 2**N
for _ in range(X):
    table.append(list(map(int,input().split())))
queue = list(map(int,input().split()))
def magic(S): # S mean Size
    for i in range(0,X,S):
        TX = table[i:i+S]
        for j in range(0,X,S):
            TY = [q[j:j+S] for q in TX]

            for ti in range(S):
                for tj in range(S):
                    table[i+ti][j+tj] = TY[-(tj+1)][ti]

def unionFind():
    
    dummy = [[0]*X for _ in range(X)]
    result = 0
    for ui in range(X):
        for uj in range(X):
            if table[ui][uj] and not dummy[ui][uj]:
                q = deque()
                hq = deque()
                q.append([ui,uj])
                hq.append([ui,uj])
                c = 0
                while q:
                    qx,qy = q.popleft()
                    for qd in range(4):
                        qnx,qny = qx+d[qd][0],qy+d[qd][1]
                        if 0<=qnx<X and 0<=qny<X and table[qnx][qny] and not dummy[qnx][qny]:
                            q.append([qnx,qny])
                            hq.append([qnx,qny])
                            dummy[qnx][qny] = 1
                            c += 1 
                
                while hq:
                    qx,qy = hq.popleft()
                    dummy[qx][qy] = c
                if result < c:
                    result = c
    return result

for M in queue:

    magic(2**M)
    melt = [[0]*X for _ in range(X)]
    for MI in range(X):
        for MJ in range(X):
            c = 0
            for MD in range(4):
                nx,ny = MI+d[MD][0],MJ+d[MD][1]
                if 0<=nx<X and 0<=ny<X and table[nx][ny]:
                    c +=1
            if c < 3:
                melt[MI][MJ] = 1
    for MI in range(X):
        for MJ in range(X):
            if melt[MI][MJ] and table[MI][MJ]:
                table[MI][MJ] -=1
    
res = sum([sum(i) for i in table])
u = unionFind()
print(res)
print(u)


'''
unionFind 부분에서 뒷걸음치다 쥐잡은격으로 union 크기가 구해졌는데 아무튼 좋은게 좋은거지
'''