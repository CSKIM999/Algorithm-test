import sys
input = sys.stdin.readline
from itertools import permutations
N,M,K = list(map(int,input().split()))
table = []
rt = []
result =1e9
for i in range(N):
    table.append(list(map(int,(input().split()))))
for i in range(K):
    rt.append(list(map(int,(input().split()))))
get = list(permutations(rt,K))
def rot(table,lst):
    global result
    for x,y,c in lst:
        x = x-c-1
        y = y-c-1
        c = c*2+1
        for j in range(c):
            l,u,r,d = [i[y+j] for i in table[x+j:x+c-j]],table[x+j][y+j:y+c-j],[i[y+c-1-j] for i in table[x+j:x+c-j]],table[x+c-1-j][y+j:y+c-j]
            ll,uu,rr,dd = l[1],u[-2],r[-2],d[1]
            tl,tr = l[1:]+[dd],[uu]+r[:-1]
            table[x+j][y+j:y+c-j],table[x+c-1-j][y+j:y+c-j] = [ll]+u[:-1], d[1:]+[rr]
            # print(tl,tr)
            for i in range(len(tl)):
                table[x+j+i][y+j] = tl[i]
                table[x+j+i][y+c-j-1] = tr[i]
            if 2<=len(l)<=3:
                break
    for i in table:
        result = min(result,sum(i))
for cs in get:
    rot([i[:] for i in table],cs)
print(result)