# bfs 로 풀기로 해놓고 자꾸 그리디로 풀어서 다시정리

#Given 테이블
get = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2] #181
mainTable = [2*i for i in range(21)]
CrossTable = [[],[13,16,19,25,30,35,40],[22,24,25,30,35,40],[28,27,26,25,30,35,40]]
result = 0

debugCount = 0

# bfs 에서 변경될 변수리스트 -> 슬라이싱 사용복제
socket = [False for _ in range(42)]
specialsocket = [16,22,24,26,28,30]
for i in specialsocket:
    socket[i] = [False,False] # 0은 메인 1은 크로스인덱스

nodes = [[2,4,6,8,10] for _ in range(4)] #각 노드의 획득기댓값
nodePosition = [[0,0,False] for _ in range(4)]


def pushNode(Cnum,Sockets,node,point,Np,N): #(nNP[1],Sockets,nodenum,point,Nodeposition,Nodes)

        try:
            pointIndex = CrossTable[Cnum].index(point)
            alpha = 5 - (len(CrossTable[Cnum]) - (pointIndex+1)) #4
            temp = CrossTable[Cnum][pointIndex+1:]
            for _ in range(alpha):
                temp += [0]
        except:
            if point == 0:
                N.remove(N[node])
                Np.remove(Np[node])
                return
            temp = [0]*5

        N[node] = temp[:]
        Np[node][0] = pointIndex

def socketControl(Sockets,node,point,Np): # Sockets,nodenum,point,NP,Nodes
    #pushNode 전에 실행시킬 것 Np 의 변화가 있으면 안됨
    global specialsocket
    nNP = Np[node] #[현재노드인덱스 , 현재 지나는 테이블 , 크로스테이블 진입여부]
    if nNP[2]:
        Now = CrossTable[nNP[1]][nNP[0]]
    else:
        Now = mainTable[nNP[0]]

    if Now == 30 and point == 30: #단 한개의 예외
        Sockets[30][0] = False
        Sockets[30][1] = True
        return

    #탈출 // Now 사용
    if Now in specialsocket: # 동일 포인트를 가지는 노드
        if nNP[2]: #중앙부를 지나고있다면
            Sockets[Now][1] = False
        else: #메인테이블을 지난다면
            Sockets[Now][0] = False
    else: #일반노드들
        Sockets[Now] = False

    #진입 // point 사용
    if point == 0:
        pass
    elif point in specialsocket:
        if nNP[2]:
            Sockets[point][1] = True
        else:
            Sockets[point][0] = True
    else:
        Sockets[point] = True
def indfs(nodenum,Count,Result,Sockets,Nodes,Nodeposition,debugCount):

    debugCount += 1
    if debugCount == 100:
        print('Now')
    nNP = Nodeposition[nodenum]

    point = Nodes[nodenum][get[Count]-1] #10
    if point in specialsocket:
        if point == 30 and Sockets[30][0] and Sockets[30][1]:
            return
        elif nNP[2]:
            if Sockets[point][1]:
                return
        else:
            if Sockets[point][0]:
                return
    elif Sockets[point]: #해당 위치 체크
        return

    Result += point
    
    
    #소켓
    if nNP[2]:
        Now = CrossTable[nNP[1]][nNP[0]]
    else:
        Now = mainTable[nNP[0]]
    # Sockets[nNP[1]][Now] = False
    # Sockets[nNP[1]][point] = True

    

    if point%10 == 0 and not nNP[2]:
        # pointIndex = mainTable.index(point)
        socketControl(Sockets,nodenum,point,Nodeposition)
        Nodes[nodenum] = CrossTable[point//10][:5]
        Nodeposition[nodenum] = [0,point//10,True]

    elif nNP[2]:
        if nNP[0] == 0:
            # 둘 다 걸쳐있는 특수인덱스
            pass
        socketControl(Sockets,nodenum,point,Nodeposition)
        pushNode(nNP[1],Sockets,nodenum,point,Nodeposition,Nodes)

    else:
        socketControl(Sockets,nodenum,point,Nodeposition)
        pointIndex = mainTable.index(point)
        try:
            Nodes[nodenum] = mainTable[pointIndex+1:pointIndex+6]
        except IndexError:
            temp = mainTable[pointIndex+1:]
            if len(temp) < 5:
                alpha = 5 - len(temp)
                for _ in range(alpha):
                    temp += [0]
            Nodes[nodenum] = temp[:]
        Nodeposition[nodenum][0] = pointIndex


def dfs(Count,Result,Sockets,Nodes,Nodeposition,debugCount): #0,0,socket,[2,4,6,8,10],[0,0,False]
    global result,get,mainTable
    if Count >= len(get):
        result = max(result,Result)
        return
    
    if len(Nodes) == 4:
        indfs(0,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
        indfs(1,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
        indfs(2,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
        indfs(3,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
    elif len(Nodes) == 3:
        indfs(0,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
        indfs(1,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
        indfs(2,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
    else:
        indfs(0,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
        indfs(1,Count,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)
    
    dfs(Count+1,Result,Sockets[:],Nodes[:],Nodeposition[:],debugCount)

dfs(0,result,socket[:],nodes[:],nodePosition[:],debugCount)
print(result)