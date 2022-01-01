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

get = [1,2,3,4,1,2,3,4,1,2] # A = 190
nodes = [[2,4,6,8] for _ in range(4)]
mainTable =[2*i for i in range(1,21)]
Table1 = [13,16,19,25,30,35,40]
Table2 = [22,24,25,30,35,40]
Table3 = [28,27,26,25,30,35,40]
result = 0
for i in range(4):

    a,b,c,d = [[nodes[j][i],j] for j in range(4)]
    point, node = max(a,b,c,d)
    result += point
    pointIndex = mainTable.index(point)+1
    nodes[node] = mainTable[pointIndex:pointIndex+4]
    print(nodes[node])
    print(result)

    print(f'point : {point} && node : {node}')

    pass

print(mainTable)