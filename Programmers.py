# from itertools import combinations

# data = [['O',0],['1',1],['2',2],['3',3],['4',4]]
# hist = []
# # for i in range(4): # 입는 의상의 개수
# #     temp = []
# #     for j in range(total): # 경우의 수 따지기
# #         temp.append(j)
# #         if len(temp) != i:
# #             for k in range(total):
# #                 pass10
# #         hist = hist + temp
# #         temp = []
# for time in range(1,6):
#     time_hist = []
#     temp = list(combinations(data,time))
#     for i in temp:
#         check = set()
#         for j in i:
#             check.add(j[1])
#         if len(check) == time:
#             hist.append(i)
#             time_hist.append(i)
#     print()
#     print(f'time hist : {time_hist}')
#     print()

# print(len(hist))


################################################################################
################################################################################
################################################################################
# s = "try hello world"

# ret = s.split()
# print(ret)
# answer = ''

# for i in range(len(ret)):
#     c = -1
#     temp = ''
#     for j in ret[i]:
#         if c >0:
#             temp += j
#         else:
#             temp += j.upper()
#         c = c*-1
#     print(temp)
#     if i != len(ret)-1:
#         answer += temp + ' '
#     else:
#         answer += temp

# print(answer)

################################################################################
################################################################################
################################################################################
#  ROR 게임
# from collections import deque
# data = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     answer = -1
#     visited = [[0]*m for _ in range(n)]
#     visited[0][0] = 1
#     queue = deque([[0,0,1]])
#     rot = [[1,0],[-1,0],[0,1],[0,-1]]
#     if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
#         return -1
#     while queue:
#         x,y,count = queue.popleft()
#         for a,b in rot:
#             nx,ny = x+a,y+b
#             if 0<=nx<n and 0<=ny<m:
#                 if maps[nx][ny] == 1 and visited[nx][ny] ==0:
#                     queue.append([nx,ny,count+1])
#                     visited[nx][ny] = 1
#                 if nx == n-1 and ny==m-1:
#                     answer = count+1
#                     break


#     return answer

# print(solution(data))

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     answer = -1
#     queue = deque([[0,0,1]])
#     rot = [[1,0],[-1,0],[0,1],[0,-1]]
#     while queue:
#         x,y,count = queue.popleft()
#         count +=1
#         for a,b in rot:
#             nx,ny = x+a,y+b
#             if 0<=nx<m and 0<=ny<n:
#                 if maps[nx][ny] == 1:
#                     queue.append([nx,ny,count])
#                     maps[x][y] = 0
#                 if nx == n-1 and ny==m-1:
#                     answer = count
#                     break


#     return answer

# print(solution(data))



################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'>>> 오픈채팅방 <<<'
'''
Approach >> 회원의 데이터는 유저아이디로 처리되며, 만약 아이디가 바뀔경우 전에 입력된 데이터들도 모두 바뀐다
            따라서 딕셔너리와 큐를 사용하여 큐에 사용자별 입/퇴장 데이터를, 딕셔너리에 사용자 이름데이터를 이용하여
            마지막에 하나의 스트링으로 묶어보고자 한다.
'''

# from collections import deque

# dic = {}
# result = []
# queue = deque()
# state_input = {'Enter':0,'Leave':1,'Change':2}
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# for i in record:
#     data = i.split()
#     try:
#         if state_input[data[0]] == 0:
#             dic[data[1]] = data[2]
#             queue.append([0,data[1]])
#         elif state_input[data[0]] == 1:
#             queue.append([1,data[1]])
#         elif state_input[data[0]] == 2:
#             dic[data[1]] = data[2]
#     except KeyError:
#         print('error')
    
# print(queue)
# print(dic)
# while queue:
#     s,u = queue.popleft()
#     if s == 0:
#         result.append(f"{dic[u]}님이 들어왔습니다.")
#     elif s == 1:
#         result.append(f"{dic[u]}님이 나갔습니다.")

# print(result)


'''
1회차 >> 바로정답 존나게 쉽다
'''

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
' >>> 멀쩡한 사각형 <<< '
# a=[8,12]
# total = a[0]*a[1]
# a,b = min(a),max(a)
# # a = 77783/77797


# # print(a)
# from math import ceil,floor
# c = 1/(a/b)
# # print((c*7))
# i=0
# result = 0
# while True:
#     i+=1
#     up = ceil(c*i)
#     low = floor((up)-c)
#     result += up-low
#     if (c*i)%1 == 0:
#         alp = a/i
#         result = result*alp

#         break
# print(result)

# def gcd(a,b):
#     return b if a%b == 0 else gcd(b,a%b)

# print(gcd(7,11))

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
' >>> 기능 개발 <<< '
from math  import ceil
data = [93, 30, 55]
sp = [1, 30, 5]
result = []
ans = []
for i in range(len(data)):
    result.append(ceil((100 - data[i])/sp[i]))
temp = result[0]
j = 1
print(result)
for i in range(1,len(result)):
    if temp<result[i]: #i 보다 i+1 이 더 오래걸릴 때
        ans.append(j)
        temp = result[i]
        j = 0
    j+=1
ans.append(j)
print(ans)