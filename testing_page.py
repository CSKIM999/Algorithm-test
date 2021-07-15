from itertools import combinations


n= int(input())
data = [[] for _ in range(n)]
s,t,el = [],[],[]
for i in range(n):
    data[i] = list(map(str,input().split(' ')))
    for j in range(n):
        if data[i][j] == 'S':
            s.append([i,j])
        elif data[i][j] == 'T':
            t.append([i,j])
        else:
            el.append([i,j])
            data[i][j] = 'X'
temp = list(combinations(el,3))

def detect(data,t):
    for x,y in t:
        u,d,l,r = 0,0,0,0
        while x-u >=0 :
            if data[x-u][y] == 'S':
                return False
            elif data[x-u][y] == 'O':
                break
            else:
                u += 1
        
        while x + d < n:
            if data[x+d][y] == 'S':
                return False
            elif data[x+d][y] == 'O':
                break
            else:
                d += 1
        
        while y - l >=0:
            if data[x][y-l] == 'S':
                return False
            elif data[x][y-l] == 'O':
                break
            else:
                l += 1

        while y + r < n:
            if data[x][y+r] == 'S':
                return False
            elif data[x][y+r] == 'O':
                break
            else:
                r += 1
        
    return True

ck = False
for i in temp:
    for j in range(3):
        data[i[j][0]][i[j][1]] = 'O'
    if detect(data,t) == True and ck == False:
        print('YES')
        ck = True
    for j in range(3):
        data[i[j][0]][i[j][1]] = 'X'
if ck == False:
    print('NO')