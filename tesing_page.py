def solution(n, start, end, roads, traps):
    
    table = [[{},{}] for _ in range(n+1)] # in & out
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
        nonlocal ans
        if ans != None:
            if cost >= ans:
                return
        key = list(table[node][1])
        for i in key:
            icost = cost+table[node][1][i]
            if i == end:
                if ans == None:
                    ans = icost
                else:
                    ans = min(ans,icost)
            if i in traps:
                dfs(i,icost,trap(i,table))
            else:
                dfs(i,icost,[j[:] for j in table])
        return

    dfs(start,0,[k[:] for k in table])
    
    answer = ans
    return answer

result = 4
n,start,end = 3,1,3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]

print(solution(n,start,end,roads,traps))