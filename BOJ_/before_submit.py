import sys
input = sys.stdin.readline
from collections import deque
d=[[1,0],[-1,0],[0,1],[0,-1]]
dic = {0:'.',1:'x','x':1,'.':0}
r,c = map(int,input().split())
table = []
for i in range(r):
    t = map(lambda x:dic[x],list(input().strip()))
    table.append(list(t))
n = int(input())
stick = list(map(int,input().split()))
def check():
    q = deque()
    flag = True
    rt = [[0 for _ in range(c)] for _ in range(r)]
    count = 0
    for i in range(r):
        for j in range(c):
            if table[i][j] and not rt[i][j]:
                count += 1
                tempq = deque()
                tempq.append([i,j])
                q.append([i,j])
                rt[i][j] = count
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx,ny = d[k][0]+x,d[k][1]+y
                        if 0<=nx<r and 0<=ny<c: #테이블 유효범위
                            if not rt[nx][ny] and table[nx][ny]:
                                q.append([nx,ny])
                                tempq.append([nx,ny])
                                rt[nx][ny] = count
                
                if count not in rt[-1][:]:
                    flag = False
                    while tempq:
                        x,y = tempq.popleft()
                        rt[x][y] *= -1
    if flag:
        return rt,True
    else:
        return rt,False

def fall(given):
    R = []
    for i in range(c):
        temp = [j[i] for j in given]
        if min(temp)<0:
            # R.append(i)
            rm = r
            mc = 0
            for k in range(1,r+1):
                if not temp[-k]:
                    mc += 1
                elif temp[-k]>0:
                    mc = 0
                else:
                    rm = min(rm,mc)
            R.append([i,rm])
    m = min([i[1] for i in R])
    for i in range(c):
        temp = [j[i] for j in given]
        if min(temp)<0:
            for k in range(1,r+1):
                if given[-k][i]<0:
                    table[-k][i] = 0
                    table[-k+m][i] = 1
def broke(h,s):
    if s == -1:
        for i in range(c):
            if table[-h][i]:
                table[-h][i] = 0
                return
    else:
        for i in range(1,c+1):
            if table[-h][-i]:
                table[-h][-i] = 0
                return


lr = -1
for i in stick:
    broke(i,lr)
    lr *= -1
    a,t = check()
    if t:
        continue
    else:
        fall(a)

ans = []
for i in table:
    temp = ''
    for j in i:
        temp += dic[j]
    ans.append(temp)
for i in ans:
    print(i)


