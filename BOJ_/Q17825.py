'''
>>> Q 17825 주사위 윷놀이 <<<

Given ) 특수한 패턴을 갖는 말판 위에 숫자가 쓰여있고 시작점에 4개의 말이 위치한다.
        다음칸이 아닌 특수한 위치로 이동시키는 특수칸이 존재한다.
        게임은 10회의 주사위 던지기로 이루어지며, 매턴마다 1에서5 까지 한면에 하나씩 적혀있는 5면체 주사위를 던져
        도착지점에 있지 않은 임의의 말을 이동시킨다.
        만약 임의의 말 A 가 움직이고자 하는 칸에 다른 말 B 가 존재한다면, 그 A 말은 움직일 수 없다. 만약 그 칸이 도착칸이라면 이동할 수 있다.
        말이 이동을 마칠 때 위치하는 칸의 숫자만큼 점수에 추가된다.
Input ) 주사위에서 나올 수 10개가 주어진다.
Output) 적절히 움직여 얻을 수 있는 최대점수를 출력한다


Approach )  말의 개수가 4개이므로, 말 각각의 앞 5칸까지의 획득가능 점수테이블을 작성하고 
            bfs 를 통해 10회의 움직임을 구현하더라도 4^(10) 으로 1,000,000 회정도에 불과하다
            점수테이블 갱신에 신경쓴다면 문제없을듯 하다

'''
get = [5,5,5,2,5,5,2,5,2] # A = 190
socket = [False for _ in range(41)]
socket[0] = True
nodes = [[2,4,6,8,10] for _ in range(4)]
mainTable =[2*i for i in range(21)]
CrossTable = [[],[13,16,19,25,30,35,40],[22,24,25,30,35,40],[28,27,26,25,30,35,40]]
result = 0
nodePosition = [[0,0,False] for _ in range(4)] # 현재위치, 크로스테이블 인덱스 , 크로스테이블 진입여부
flag = False

for i in get:
    i -= 1
    #4개의 노드 테이블 중 i 인덱스 데이터와 해당 노드의 숫자 추출
    maxTable = [[nodes[j][i],j] for j in range(4)] # [2,4,6,8,10]


    #4개의 노드가 갈 수 있는 길 중 현재 주어진 input 인덱스에서 가장 큰 값 반환
    while True:
        point, node = max(maxTable)
        if point == 0: #자리가 없어서 골라인으로 한개는 들어가야 할 때
            nodetemp = []
            for a,maxTableNode in maxTable:
                Val,CIndex,CNodeBool = nodePosition[maxTableNode]
                nodetemp.append([CrossTable[CIndex][Val],maxTableNode])
            
            div,node= max(nodetemp)
            nodePosition[node][0] = 40
            socket[div] = False #비워주기
            flag = True
            
            break
        ########################################################### <<<<<<<<<<<<< 22/01/03 크로스테이블 인덱스 정리중이었음
        now = mainTable[nodePosition[node][0]] #현재 max값을 반환받은 노드의 위치
        if socket[point]:
            maxTable.remove([point,node])
            continue
        socket[now] = False
        socket[point] = True
        break
        # if socket[point]:
        #     maxTable.remove([point,node])
        # else:
        #     now = nodePosition[node][0]
        #     if point==0:
        #         socket[now] = False
        #         break
        #     socket[now] = False
        #     socket[point] = True
        #     break
    
    result += point
    if flag:
        point = 40
        flag = False
    def pushNode(num):
        pointIndex = CrossTable[num].index(point)+1
        alpha = 5 - (len(CrossTable[num]) - pointIndex) #4
        temp = CrossTable[num][pointIndex:]
        for _ in range(alpha):
            temp += [0]
        nodes[node] = temp[:]
        nodePosition[node][0] = pointIndex-1
        # try:
        #     nodes[node] = CrossTable[num][pointIndex:pointIndex+5]
        # except IndexError:
        #     temp = CrossTable[num][pointIndex:]
        #     if len(temp) < 5:
        #         alpha = 5 - len(temp)
        #         for _ in range(alpha):
        #             temp += [0]
        #     nodes[node] = temp[:]
        # nodePosition[node][0] = pointIndex

    #노드 앞의 5칸 갱신
    if point%10 == 0 and not nodePosition[node][2]: # 파란색 원의 경우
        pointIndex = mainTable.index(point)+1
        nodes[node] = CrossTable[point//10][:5]
        nodePosition[node] = [pointIndex-1,point//10,True]

    elif nodePosition[node][2]:
        pushNode(nodePosition[node][1])
        # now = nodes[node][0]
        # if 13<=now<=19:
        #     pushNode(1)
        # elif 22<=now<=24:
        #     pushNode(2)
        # else:
        #     pushNode(3)
    else:
        pointIndex = mainTable.index(point)+1
        try:
            nodes[node] = mainTable[pointIndex:pointIndex+5]
        except IndexError:
            temp = mainTable[pointIndex:]
            if len(temp) < 5:
                alpha = 5 - len(temp)
                for _ in range(alpha):
                    temp += [0]
            nodes[node] = temp[:]
        nodePosition[node][0] = pointIndex-1
    print(nodePosition)
    print()
