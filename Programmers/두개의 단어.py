'''
Programmers QuestionNumber __ 두개의 단어
#######  TODAY  #######
##### 2022. 03. 19 #####
GIVEN ) 

INPUT ) 

OUTPUT) 

Approach )  
'''
# import sys
# input = sys.stdin.readline

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
def solution(begin,target,words):
    L = len(target)
    WL = len(words)
    visit = [0 for _ in range(WL)]
    for i in range(L):
        flag = True
        for j in range(WL):
            if words[j][i] == target[i]:
                flag = False
                break
        if not flag: break
        if flag: print('FAIL')
    result = 1e9
    def dfs(begin,target,clst,Count,visit):
        nonlocal result
        if Count>result:
            return
        for i in clst: #[0]
            for j in range(L):
                if words[i][j] != begin[j]:
                    if visit[i] >= L:
                        continue
                    else:
                        visit[i] +=1
                        temp = list(begin)
                        temp[j] = words[i][j]
                        begin = ''.join(temp)
                        if begin == target:
                            result = min(result,Count)
                            return
                        else:
                            dfs(begin[:],target,found(begin[:]),Count+1,visit[:])
    def found(X):
        now = X
        lst = [[] for _ in range(WL)]
        for i in range(L):
            for j in range(WL):
                if words[j][i] == now[i]:
                    lst[j].append(i)
        Clst = []
        for i in range(WL):
            if len(lst[i])==L-1:
                Clst.append(i)
        return Clst
    dfs(begin[:],target[:],found(begin[:]),1,visit[:])
    answer = result
    return answer
print(solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"]))
