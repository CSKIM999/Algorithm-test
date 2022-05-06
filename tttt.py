'''
각 방 사이에 경로가 주어지며 각 방마다 이동하기 위한 비용이 존재
함정 방에 도달하면, 함정방과 연결된 모든 간선의 방향이 반대가 됨.
함정방은 여러번 방문 가능.
방의 갯수 n ( 2 <= n <= 2,000 ), 출발 방의 번호 n이하의 자연수 start , end , roads 의 총 갯수 3000개 이하
각 roads 의 원소는 P/Q/S 로
P 에서 Q 까지 가는데 S 만큼의 비용이 소요
start와 end 를 제외한 함정방의 갯수는 최대 10개
>>> start와 end 는 같을 수 있음!!
>>> 두 방 사이에 직접 연결된 길이 여러개 존재할 수 있음
'''


import sys
lim = 1000000
sys.setrecursionlimit(lim)
result = 4
n,start,end = 5,1,5
roads = [[1, 2, 1], [2, 3, 1], [3, 2, 1], [3, 5, 1], [1, 5, 10]]
traps = [3]
table = [[{},{},0] for _ in range(n+1)] # in & out
ans = None 
for a,b,c in roads:
    try:
        table[b][0][a] = min(table[b][0][a],c)
    except KeyError:
        table[b][0][a] = c
    try:
        table[a][1][b] = min(table[b][0][a],c)
    except KeyError:
        table[a][1][b] = c

def trap(node,table):
    In,Out = table[node][0],table[node][1]
    for i in list(In):
        table[i][0][node] = table[i][1][node]
        del table[i][1][node]
    for i in list(Out):
        table[i][1][node] = table[i][0][node]
        del table[i][0][node]
    table[node][0],table[node][1] = Out,In
    return table

def dfs(node,cost,table):
    global ans
    table[node][2] += 1
    if ans != None:
        if cost >= ans:
            return
    key = list(table[node][1])
    for i in key:
        if table[i][2] >= 2:
            if i not in traps:
                continue

        icost = cost+table[node][1][i]
        if i == end:
            if ans == None:
                ans = icost
                continue
            else:
                ans = min(ans,icost)
        if i in traps:
            dfs(i,icost,trap(i,table))
        else:
            dfs(i,icost,[j[:] for j in table])
    return

dfs(start,0,[k[:] for k in table])
print(ans)