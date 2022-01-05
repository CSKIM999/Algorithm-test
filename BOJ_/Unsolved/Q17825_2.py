# bfs 로 풀기로 해놓고 자꾸 그리디로 풀어서 다시정리

#Given 테이블


get = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2] #181
mainTable = [2*i for i in range(21)]
CrossTable = [[],[13,16,19,25,30,35,40],[22,24,25,30,35,40],[28,27,26,25,30,35,40]]
result = 0

# bfs 에서 변경될 변수리스트 -> 슬라이싱 사용복제
socket = [[False for _ in range(22)],[False for _ in range(7)],[False for _ in range(6)],[False for _ in range(7)]]

nodes = [[2,4,6,8,10] for _ in range(4)] #각 노드의 획득기댓값
nodePosition = [[0,0,False] for _ in range(4)]


def pushNode(Cnum,node,point,Np,N):
        try:
            pointIndex = CrossTable[Cnum].index(point)
            alpha = 5 - (len(CrossTable[Cnum]) - (pointIndex+1)) #4
            temp = CrossTable[Cnum][pointIndex+1:]
            for _ in range(alpha):
                temp += [0]
        except IndexError:
            temp = [0]*5

        N[node] = temp[:]
        Np[node][0] = pointIndex

def move(Count,Result,Nodes,Sockets,Nodeposition,nodenum):
    nNP = Nodeposition[nodenum]

    point = Nodes[nodenum][get[Count]-1] #10
    if nNP[1] == 0: #해당 위치 체크
        
        return
    Result += point
    
    
    #소켓
    if nNP[2]:
        Now = CrossTable[nNP[1]][nNP[0]]
    else:
        Now = mainTable[nNP[0]]
    Sockets[Now] = False
    Sockets[point] = True

    

    if point%10 == 0 and not nNP[2]:
        pointIndex = mainTable.index(point)
        Nodes[nodenum] = CrossTable[point//10][:5]
        nNP = [pointIndex,point//10,True]
    
    elif nNP[2]:
        pushNode(nNP[1],nodenum,point,Nodeposition,Nodes)

    else:
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


def dfs(Count,Result,Sockets,Nodes,Nodeposition): #0,0,socket,[2,4,6,8,10],[0,0,False]
    global result,get,mainTable
    if Count >= len(get):
        result = max(result,Result)
        return
        

    for nodenum in range(4):
        nNP = Nodeposition[nodenum]

        point = Nodes[nodenum][get[Count]-1] #10
        if Sockets[point]: #해당 위치 체크
            continue
        Result += point
        
        
        #소켓
        if nNP[2]:
            Now = CrossTable[nNP[1]][nNP[0]]
        else:
            Now = mainTable[nNP[0]]
        Sockets[Now] = False
        Sockets[point] = True

        

        if point%10 == 0 and not nNP[2]:
            # pointIndex = mainTable.index(point)
            Nodes[nodenum] = CrossTable[point//10][:5]
            Nodeposition[nodenum] = [0,point//10,True]
        
        elif nNP[2]:
            pushNode(nNP[1],nodenum,point,Nodeposition,Nodes)

        else:
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

        dfs(Count+1,Result,Sockets,Nodes,Nodeposition)
    
        


    return

dfs(0,result,socket[:],nodes[:],nodePosition[:])
print(result)