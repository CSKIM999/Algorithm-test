# id_list = ["con", "ryan"]

# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# report = set(report)

# k=3
# data = {}
# friends_data = {}
# result = [0]*len(id_list)

# for i in range(len(id_list)):
#     data[id_list[i]] = 0
#     friends_data[id_list[i]] = []

# for i in report:
#     a,b = i.split(' ')
#     data[b] += 1
#     if a not in friends_data:
#         friends_data[a] = [b]
#     else:
#         friends_data[a] += [b]

# for i in range(len(id_list)):
#     for j in friends_data[id_list[i]]:
#         if data[j] >= k:
#             result[i] += 1

# print(data)
# print(friends_data)
# print(result)

    

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
# import math

# def convert(n,k):

#     data = "0123456789A"
#     a,b = divmod(n,k)
    
#     if a == 0:
#         return data[b]
#     else:
#         return convert(a,k) + data[b]

# def is_prime(n):
#     array = [True for i in range(n+1)]
#     for i in range(2,int(math.sqrt(n))+1):
#         if array[i] == True:
#             j = 2
#             while i*j <=n:
#                 array[i*j] = False
#                 j += 1
#     return [i for i in range(2,n+1) if array[i]]


# lst = convert(110011,10)
# n = len(lst)
# temp = ''
# result = []

# for i in range(n):
#     if lst[i] != '0' and i != n-1:
#         temp  += '{}'.format(lst[i])
#     elif lst[i] == '0' and i != n-1 and len(temp) != 0:
#         if int(temp) in is_prime(int(temp)):
#             result.append(temp)
#             temp = ''
#         else:
#             temp = ''
#     else:
#         if lst[i] != '0' and len(temp) != 0:
#             temp  += '{}'.format(lst[i])
#             if int(temp) in is_prime(int(temp)):
#                 result.append(temp)
#         else:
#             if len(temp) != 0:
#                 if int(temp) in is_prime(int(temp)):
#                     result.append(temp)

# print(len(result))



# import math

# def convert(n,k):
#     data='0123456789A'
#     a,b = divmod(n,k)
        
#     if a== 0:
#         return data[b]
#     else:
#         return convert(a,k) + data[b]
# def is_prime(n):
#     array = [True for i in range(n+1)]
#     for i in range(2,int(math.sqrt(n))+1):
#         if array[i] == True:
#             j = 2
#             while i*j <=n/2:
#                 array[i*j] = False
#                 j += 1
#     return [i for i in range(2,n+1) if array[i]]

# def solution(n, k):
#     lst = convert(n,k)
#     n = len(lst)
#     temp = ''
#     result = []
#     print(lst)
#     for i in range(n):
#         if lst[i] != '0' and i != n-1:
#             temp += '{}'.format(lst[i])
#         elif lst[i] == '0' and i != n-1 and len(temp) !=0:
#             if int(temp) in is_prime(int(temp)):
#                 result.append(temp)
#                 print(temp)
#                 temp = ''
#             else:
#                 temp = ''
#         else:
#             if lst[i] != '0' or len(temp) != 0:
#                 temp += '{}'.format(lst[i])
#                 if int(temp) in is_prime(int(temp)):
#                     result.append(temp)
#             else:
#                 if len(temp) != 0:
#                     if int(temp) in is_prime(int(temp)):
#                         result.append(temp)
#     answer = len(result)
    
#     return answer

# print(solution(2,3))

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
# import math

# fees = [1, 461, 1, 10]
# records =  ["00:00 1234 IN"]
# n = len(records)
# data = {}
# time = []
# for i in range(n):
#     m = len(data)
#     t,n,io = records[i].split(' ')
#     if n not in data:
#         data[n] = [m,True]
#         time.append([t,0])
#     elif data[n][1] == True and io == 'OUT':
#         ih,im = map(int,time[data[n][0]][0].split(':'))
#         oh,om = map(int,t.split(':'))
#         tim,tom = (ih*60)+im,(oh*60)+om
#         time[data[n][0]][1] += tom-tim
#         data[n][1] = False
#     elif data[n][1] == False and io == 'IN':
#         time[data[n][0]][0] = t
#         data[n][1] = True
# for i in data:
#     index = data[i][0]
#     if data[i][1] == True:
#         ih,im = map(int,time[index][0].split(':'))
#         oh,om = 23,59
#         tim,tom = (ih*60)+im,(oh*60)+om
#         time[index][1] += tom-tim
#         time[index][0] = i
#         data[n][1] = False
#     else:
#         time[index][0] = i
# result = []
# time.sort()
# for i,j in time:
#     if j > fees[0]:
#         fee = (math.ceil((j-fees[0])/fees[2]))*fees[3]
#         result.append((fees[1]+fee))
#     else:
#         result.append(fees[1])
# print(result)


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
check = [10,9,8,7,6,5,4,3,2,1,0]
rion = [0]*11
count = 0
R_point = 0
A_point = 0
m4x=[0,[]]
def dfs(rion,count,info):
    if count == 5:
        R_point = 0
        A_point = 0
        for i in range(11):
            if rion[i] > info[i]:
                R_point += check[i]
            elif rion[i] == 0 and info[i] == 0:
                continue
            elif rion[i] <= info[i]:
                A_point += check[i]
        rs = R_point - A_point
        if rs == m4x[0]:
            pass
        elif rs>m4x[0]:
            m4x[1] = rion
            rion = [0]*11
            count = 0
            return m4x
    count += 1
    for i in range(11):
        if rion[i] > info[i]:
            continue
        if count <= 5:
            rion[i] += 1
            dfs(rion,count,info)



print(dfs(rion,count,info))
print(m4x)

############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
# from collections import deque
# # board =[[1,2,3],[4,5,6],[7,8,9]]
# # n = len(board)
# # m = len(board[0])
# # skill =[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
# # def attack(f1,f2,t1,t2,deg):
# #     for i in range(f1,t1+1):
# #         for j in range(f2,t2+1):
# #             board[i][j] -=deg
# # def heal(f1,f2,t1,t2,deg):
# #     for i in range(f1,t1+1):
# #         for j in range(f2,t2+1):
# #             board[i][j] +=deg

# # for i in skill:
# #     s,f1,f2,t1,t2,deg = i
# #     if  s== 1:
# #         attack(f1,f2,t1,t2,deg)
# #     else:
# #         heal(f1,f2,t1,t2,deg)
# # count = 0
# # for i in range(n):
# #     for j in range(m):
# #         if board[i][j] > 0:
# #             count+=1

# # print(count)
        

# board =[[1,2,3],[4,5,6],[7,8,9]]
# n = len(board)
# m = len(board[0])
# skill =[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
# q=deque(skill)
# def attack(board,f1,f2,t1,t2,deg):
#     for i in range(f1,t1+1):
#         for j in range(f2,t2+1):
#             board[i][j] -=deg
# def heal(board,f1,f2,t1,t2,deg):
#     for i in range(f1,t1+1):
#         for j in range(f2,t2+1):
#             board[i][j] +=deg
# while q:
#     s,f1,f2,t1,t2,deg = q.popleft()
#     if  s== 1:
#         attack(board,f1,f2,t1,t2,deg)
#     else:
#         heal(board,f1,f2,t1,t2,deg)
# # for i in skill:
# #     s,f1,f2,t1,t2,deg = i
# #     if  s== 1:
# #         attack(board,f1,f2,t1,t2,deg)
# #     else:
# #         heal(board,f1,f2,t1,t2,deg)
# count = 0
# for i in range(n):
#     for j in range(m):
#         if board[i][j] > 0:
#             count+=1
# print(board)
# board[0][1:3] -=2
# print(board)