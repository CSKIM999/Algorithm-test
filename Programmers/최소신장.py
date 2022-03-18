'''
Programmers QuestionNumber __ 최소신장
#######  TODAY  #######
##### 2022. 03. 18 #####
GIVEN ) 

INPUT ) 

OUTPUT) 

Approach )  
'''
# import sys
# input = sys.stdin.readline
n = 4
costs =[[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]
answer = 0
Pdata = [i for i in range(n)]
def FP(q):
    if Pdata[q] != q:
        return FP(Pdata[q])
    else:
        return q

costs.sort(key=lambda x: x[2])
for a,b,c in costs:
    if FP(a) != FP(b):
        val = min(FP(a),FP(b))
        Pdata[FP(a)] = Pdata[FP(b)] = val
        answer += c
print(answer)