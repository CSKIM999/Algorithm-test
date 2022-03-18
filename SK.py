def xprint(a):
    for i in a:
        print(i)

# '''
# 냅색 알고리즘 사용예정

# target = money
# 생산단가 = costs
# '''


# money = 1999
# point = [1,5,10,50,100,500]
# costs = [2, 11, 20, 100, 200, 600]



# # l = int(input())
# # nodes = list(map(int,input().split()))
# # stack = [0 for i in range(len(nodes)+1)]
# # for i in range(1,len(stack)):
# #     stack[i] = stack[i-1]+nodes[i-1]
# # result = sum(stack)

# # dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
# # dp[0] = stack
# # for i in range(2,1+l): # 덩어리크기
# #     for j in range(1,l-i+2): #시작 노드
# #         temp = []
# #         for k in range(i-1):
# #             temp.append(dp[j][j+k] + dp[j+k+1][j+i-1])
# #         dp[j][j+i-1] = min(temp) + (dp[0][j+i-1]-dp[0][j-1])#누적합 더하기
# # result = dp[1][l]            
# # print(f"{result}")

# dp = [[0 for _ in range(money+1)] for _ in range(6)]
# # dp[0][1] = costs[0]
# for i in range(1,money+1):
#     dp[0][i] = dp[0][i-1]+costs[0]

# for i in range(1,6): # 동전크기선택
#     now = point[i]
#     for j in range(1,money+1):
#         if now > j:
#             dp[i][j] = dp[i-1][j]
#         elif now==j:
#             dp[i][j] = min(dp[i][j-now]+costs[i],dp[i-1][j])
#         else:
#             dp[i][j] = min(dp[i][j-now]+costs[i],dp[i-1][j])
#         # dp[i+j][j] = 
#         pass

# print(dp[-1][-1])

'''
단순구현문제
'''

# n  = 7
# c = n-1
# node = 1
# table = [[0 for _ in range(n)] for _ in range(n)]
# temp = [i for i in range(node,c+node)]
# node += c
# f = temp[0]
# tb = temp+[f]
# print(tb)

# c -=2
# temp = [i for i in range(node,c+node)]
# node += c
# f = temp[0]
# tb = temp+[f]
# print(tb)
# c -=2
# temp = [i for i in range(node,c+node)]
# node += c
# f = temp[0]
# tb = temp+[f]
# print(tb)
# n = 6
# Clockwise = False
# table = [[0 for _ in range(n)] for _ in range(n)]

# if n <= 2:
#     result = [[1]*n for _ in range(n)]
# else:
#     ml = n-1
#     node = 1
#     for i in range(n):
#         if ml<1:
#             if ml == 0:
#                 table[i][i] = node
#             break
#         temp = [i for i in range(node,ml+node)]
#         if Clockwise:
#             tb = temp+[node]
#         else:
#             temp = list(reversed(temp))
#             tb = [node]+temp
#         table[i][i:i+ml+1] = tb
#         table[-(i+1)][i:i+ml+1] = tb
#         table[-(i+1)][i:i+ml+1] = list(reversed(table[-(i+1)][i:i+ml+1]))
#         for j in range(len(tb)):
#             table[j+i][i] = tb[-(j+1)]
#             table[j+i][-(i+1)] = tb[j]
#         node += ml
#         ml -=2
# ans = [[1,5,4,3,2,1],[2,6,8,7,6,5],[3,7,9,9,8,4],[4,8,9,9,7,3],[5,6,7,8,6,2],[1,2,3,4,5,1]]
# xprint(table)
# print()
# xprint(ans)
# print(ans==table)

from collections import deque
n = 4
edges = [[2,3],[0,1],[1,2]]
data = [[] for _ in range(n)]
for a,b in edges:
    data[a].append(b)
    data[b].append(a)
#  data = [[1, 2], [0, 3, 4], [0], [1], [1]]
result = 0

for i in range(n):
    hist = [i]
    q = deque([])
    for ttt in data[i]:
        q.append([ttt,1])
        hist.append(ttt)
    while q:
        now,count = q.popleft()
        for j in data[now]:
            if j not in hist:
                cc = count *2
                q.append([j,cc])
                hist.append(j)
                result += count
print(result)
# w,h = 3,3

# dp = [[0 for _ in range(w)] for _ in range(h)]
# dp[0] = [1 for _ in range(w)]
# for i in range(h):
#     dp[i][0] = 1
# for i in range(1,h):
#     for j in range(1,w):
#         dp[i][j] = dp[i-1][j]+dp[i][j-1]
# xprint(dp)

# print(dp[-1][-1])


'''
import sys
sys.setrecursionlimit(60000)

def matrix_mult(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k]
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n//2)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(A, n-1)
        return matrix_mult(temp, A)

m = 1000000007
def solution(n):
    dp=[0 for _ in range(n+1)]
    dp[1],dp[2] =1,2
    if n==0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-2]+dp[i-1]
    answer = dp[-1]
    return answer

aa = [[1,1],[1,0]]
# print(solution(1000)%m)
print(matrix_pow(aa,100))
피보나치 행렬제곱
'''