from collections import deque

paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
n = 7
gates = [3,7]
summits = [1,5]
#일부 시간초과, 일부 틀림
def solution(n, paths, gates, summits):
    gates.sort()
    summits.sort()
    pathdata = {}
    nodelink = [[] for _ in range(n+1)]
    for f,t,c in paths:
        try:
            pathdata[c].append([f,t])
        except KeyError:
            pathdata[c] = [[f,t]]
    links = list(pathdata)
    links.sort()

    def dfs(now,hist):
        nonlocal flag
        if now in gates:
            flag = True
            return
        hist.append(now)
        for i in nodelink[now]:
            if i in hist:
                continue
            if i in summits:
                continue
            if flag:
                return
            dfs(i,[i for i in hist])
        return


    answer = []
    for cost in links:
        costlst = pathdata[cost]
        for a,b in costlst:
            nodelink[a].append(b)
            nodelink[b].append(a)
        for smm in summits:
            flag = False
            dfs(smm,[])
            if flag == False:
                continue
            else:
                return([smm,cost])
    return(-1)
    ## [14,15,16, // 20,21,22,24]

print(solution(n,paths,gates,summits))
        