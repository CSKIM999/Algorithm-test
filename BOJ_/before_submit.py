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