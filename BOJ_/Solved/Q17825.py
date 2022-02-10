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
        if b!=0 and table[a][b] == 0: #시작점이 아닌데 현재 딛고있는 점수가 0 일경우
            continue
        flag = False # 중복칸 플래그
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
            elif table[a][b+point] == 30 and a!=0:
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

'''
2회차 > 결국 정답판정을 받았다. 거의 다 왔는데 자꾸 한 두개 케이스에서 오답이 나와서 정답 코드를 가져다가 문제점을 찾았다
        찾고보니 30점짜리 테이블이 중앙을 가로지르는 3개의 테이블의 중간에도 있지만, 메인테이블과 30테이블의 0번 인덱스에서도 겹쳤다.
        따라서 그부분을 예외로 두고 코드를 짜니 정답판정을 받았다.
        지금 다시와서 보니 각각의 노드에 특수한 인덱스를 주어 딕셔너리로 관리하는것이 이런 오차를 줄이는데 훨씬 도움이 되었을 것 같다.
'''