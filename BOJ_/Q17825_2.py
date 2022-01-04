# bfs 로 풀기로 해놓고 자꾸 그리디로 풀어서 다시정리

#Given 테이블
mainTable = [2*i for i in range(21)]
CrossTable = [[],[13,16,19,25,30,35,40],[22,24,25,30,35,40],[28,27,26,25,30,35,40]]
result = 0

# bfs 에서 변경될 변수리스트 -> 슬라이싱 사용복제
socket = [False for _ in range(41)]
socket[0] = True 
nodes = [[2,4,6,8,10] for _ in range(4)] #각 노드의 획득기댓값
nodePosition = [[0,0,False] for _ in range(4)]

def dfs(Count,Result,Sockets,Nodes,Nodeposition):
    global result
    if Count == 10:
        result = max(result,Result)
        return
    Count +=1



    return