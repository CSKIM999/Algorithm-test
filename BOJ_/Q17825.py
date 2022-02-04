table = [[i*2 for i in range(21)] + [0,0,0,0,0]]
table.append([10,13,16,19,25,30,35,40,0,0,0,0,0])
table.append([20,22,24,25,30,35,40,0,0,0,0,0,0])
table.append([30,28,27,26,25,30,35,40,0,0,0,0,0,0])
position = [[(i*0)+1 for i in j] for j in table] #position
nodes = [[0,0] for _ in range(4)]
turn = list(map(int,input().split()))
test_25 = [[1,4],[2,3],[3,4]]
test_30 = [[1,5],[2,4],[3,5]]
test_35 = [[1,6],[2,5],[3,6]]
test_40 = [[0,20],[1,7],[2,6],[3,7]]
# 30,35 를 추가하니 더 빨리 틀렸습니다가 뜸. 두 내용을 다시 확인해볼것.
def canMoveList(point,N,P):
    Glist = []
    temp = []
    for node in range(4):
        a,b = N[node]
        if b!=0 and table[a][b] == 0:
            continue
        flag = False
        if P[a][b+point] and (a,b+point) not in temp:
            if table[a][b+point] == 40:
                for ta,tb in test_40:
                    if ta==a and tb==b+point:
                        continue
                    if P[ta][tb] == 0:
                        flag = True
            elif table[a][b+point] == 25:
                for ta,tb in test_25:
                    if ta==a and tb==b+point:
                        continue
                    if P[ta][tb] == 0:
                        flag = True
            elif table[a][b+point] == 30:
                for ta,tb in test_30:
                    if ta==a and tb==b+point:
                        continue
                    if P[ta][tb] == 0:
                        flag = True
            elif table[a][b+point] == 35:
                for ta,tb in test_35:
                    if ta==a and tb==b+point:
                        continue
                    if P[ta][tb] == 0:
                        flag = True
            
            
            if flag:
                continue
            temp.append((a,b+point))
            Glist.append([table[a][b+point],node])

    return Glist

def moveNode(shem,P,N,point): #P 데이터 갱신 // shem 데이터 갱신
    o1,o2 = shem[N]
    n1,n2 = o1,o2+point

    if o1 != 0 and o2 == 0:
        # 10 20 30 의 경우
        now = table[o1][o2]
        P[0][now//2] = 1
    
    if n1 == 0 and table[o1][o2+point]%10 == 0:
        if table[o1][o2+point]//10 != 4:
            n1 = table[o1][o2+point]//10
            n2 = 0
            P[o1][o2+point] = 0

            
    
    P[o1][o2] = 1
    P[n1][n2] = 0
    if table[n1][n2] == 0:
        P[n1][n2] = 1
    shem[N] = [n1,n2]

    return P,shem
answer = 0
def dfs(Nodes,Position,C,result):
    global answer
    if C==10:
        answer = max(answer,result)
        return
    lst = canMoveList(turn[C],Nodes,Position)
    if not lst:
        dfs(Nodes,Position,C+1,result)
    for earn,node in lst:
        p,n = moveNode([i[:] for i in Nodes],[j[:] for j in Position],node,turn[C])
        dfs(n,p,C+1,result+earn)

    
dfs(nodes,position,0,0)
print(answer)


#40 만 겹치는게 아니라 25부터 40까지 모두 겹친다. 이부분을 다시 생각해서 체크해보자