'''
Programmers level test
'''
# s = "3people unFollowed me"

# data = list(s.split(' '))
# answer = ''
# for i in data:
#     temp = list(i)
#     temp_str = ''
#     for j in range(len(temp)):
#         if j == 0:
#             temp_str+=temp[0].upper()
#         else:
#             temp_str += temp[j].lower()
#     if len(answer) == 0:
#         answer += temp_str
#     else:
#         answer += ' '+temp_str

# print(answer)

# 북0 동1 남2 서3 
# count = 0
# length = []
# dx,dy = [-1,0,1,0],[0,1,0,-1]
# # grid = ["SL","LR"]
# # grid = ["R","R"]
# n = len(grid)
# m = len(grid[0])
# data = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
# def rot(node,dest):
#     x,y = node[0],node[1]
#     if grid[x][y] == 'S':
#         return dest
#     elif grid[x][y] == 'L':
#         dest -=1
#         if dest == -1:
#             dest = 3
#         return dest
#     else:
#         dest+=1
#         if dest == 4:
#             dest = 0
#         return dest
# def move(dest,node,give,count,len_count):

#     global length
#     len_count += 1
#     x,y = node[0],node[1]
#     nx,ny = dx[dest]+x,dy[dest]+y
#     if nx<0:
#         nx = n-1
#     elif nx>=n:
#         nx = 0
#     if ny<0:
#         ny = m-1
#     elif ny>=m:
#         ny = 0
#     ndest = rot([nx,ny],dest)
#     give[x][y][dest] = count
#     if give[nx][ny][ndest] != 0:
#         length.append(len_count)
#         return give
#     return move(ndest,[nx,ny],[i[:] for i in give[:]],count,len_count)

# # data = move(2,[0,0],data,count,0)
# # print(data)
# # print(length)
# for i in range(n):
#     for j in range(m):
#         for k in range(4):
#             if data[i][j][k] ==0:
#                 count +=1
#                 data = move(k,[i,j],data,count,0)
# answer = length
# print(data)
# print(length)

# '''
# 노래 찾기
# '''
# m = "ABC"
# MI = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# dic = {'C':'0','C#':'1','D':'2','D#':'3','E':'4','F':'5','F#':'6','G':'7','G#':'8','A':'9','A#':'A','B':'B'}
# def trans(dic,string):
#     flag = False
#     result = ''
#     for i in range(len(string)):
#         if flag:
#             flag =False
#             continue
#         if i != len(string)-1:
#             if string[i+1] == '#':
#                 j = string[i]+string[i+1]
#                 result += dic[j]
#                 flag = True
#                 continue
#         result += dic[string[i]]
    
#     return result
        
# m = trans(dic,m)

# data = []
# for i in MI:
#     temp = list((i.split(',')))
#     s,e = list(map(int,temp[0].split(':'))),list(map(int,temp[1].split(':')))
#     rt = (e[0]-s[0])*60+(e[1]-s[1])
#     str_temp = trans(dic,temp[3])
#     data.append([rt,temp[2],str_temp])

# # print(data)
# info = []
# for rt,name,mi in data:
#     count = len(mi)
#     reps = rt//count
#     el = rt%count
#     temp = ''
#     for i in range(el):
#         temp += mi[i]
#     info.append([mi*reps + temp,name])
# # print(info)

# for i,name in info:
#     if m in i:
#         print(name)
################################################################################
################################################################################
################################################################################
# s ="{{4,2,3},{3},{2,3,4,1},{2,3}}"

# s =s.lstrip('{')
# s =s.rstrip('}')
# data = s.split('},{')

# for i in range(len(data)):
#     data[i] = list(map(int,data[i].split(',')))
# data.sort(key= lambda x: len(x))
# result = [[] for _ in range(len(data))]
# for i in range(len(data)):
#     temp = 0
#     for j in data[i]:
#         if j not in result:
#             temp = j
#             break
#     result[i] = temp
# print(result)
################################################################################
################################################################################
################################################################################

# def check(data):
#     stack = []
#     if len(data) == 1:
#         return False
#     for i in range(len(data)):
#         if data[i] == '(':
#             stack.append(data[i])
#         elif data[i] == '{':
#             stack.append(data[i])
#         elif data[i] == '[':
#             stack.append(data[i])
#         if len(stack) != 0:
#             if data[i] == ')':
#                 if stack.pop() == '(':
#                     continue
#                 else:
#                     return False
#             elif data[i] == '}':
#                 if stack.pop() == '{':
#                     continue
#                 else:
#                     return False
#             elif data[i] == ']':
#                 if stack.pop() == '[':
#                     continue
#                 else:
#                     return False
#         else:
#             return False
#     if len(stack) != 0:
#         return False
#     return True

# s = '{}[](([]))'
# count = 0
# for i in range(len(s)):
#     if check(s):
#         count+=1
#     s = s[1:]+s[0]
# print(count)

'''
괄호 변환 -> 열림 닫힘을 +- 1 로 체크하니 {[(])}같은걸 솎아내지 못했음
'''

################################################################################
################################################################################
################################################################################
# import math
# from itertools import permutations
# def is_prime(x):
#     if x <= 1:
#         return False
#     for i in range(2,int(math.sqrt(x))+1):
#         if x % i ==0:
#             return False
#     return True

# s = "011"
# data = list(map(int,s))
# a = list(permutations(data,2))
# # print(a)
# length = len(s)
# nums = set()
# count = 0
# for i in range(1,length+1):
#     for j in list(permutations(data,i)):
#         temp = ''
#         for k in j:
#             temp += str(k)
#         temp = int(temp)
#         nums.add(temp)
# print(nums)
# for i in nums:
#     if is_prime(i):
#         count +=1
# print(count)
'''
통과!
'''
################################################################################
################################################################################
################################################################################
# from itertools import permutations
# a=[12,1214]
# '''
# 89889 89898
# '''



# nums = [[] for _ in range(10)]
# for i  in range(len(a)):
#     temp = str(a[i])
#     nums[int(temp[0])].append([a[i],i])

# for i in range(10):
#     if len(nums[i])!=0:
#         M = max([len(str(j[0])) for j in nums[i]])
#         for j in range(len(nums[i])):
#             now = nums[i][j][0]
#             if len(str(now)) < M:
#                 sub = M - len(str(now)) 
#                 if str(now)[-1] > str(now)[0]:
#                     now = str(now) + (str(now)[0])*sub   
#                 else:
#                     now = str(now) + str(int(str(now)[0])-1)*sub
#                 nums[i][j][0] = int(now)
# print(nums)
# result = ''
# for i in range(9,-1,-1):
#     if len(nums[i]) > 0:
#         b = sorted(nums[i],key= lambda x: [x[0], a[x[1]]],reverse=True)
#         print(b)
#         for j in b:
#             result += str(a[j[1]])
# result = int(result)
# print(str(result))

# # nums = [[] for _ in range(10)]
# # for i in a:
# #     temp = str(i)
# #     nums[int(temp[0])].append(temp)
# # # print(nums)
# # for i in range(10):
# #     if len(nums[i]) != 0:
# #         length = len(nums[i])
# #         lst = list(permutations(nums[i],length))
# #         M = ''
# #         for j in lst:
# #             temp = ''
# #             for k in j:
# #                 temp += k
# #             M = max(temp,M)
# #         # print(M)
# #         nums[i] = M
# # # print(nums)
# # result = ''
# # for i in range(9,-1,-1):
# #     if len(nums[i]) !=0:
# #         result += nums[i]
# # result = int(result)

# # print(result)

################################################################################
################################################################################
################################################################################
#  ZAAAAAABAAAC
## 조이스틱 정답
# give = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
# data = list(give.split(','))
# dic = {}
# for i in range(len(data)):
#     dic[data[i]] = i
# print(dic)
# a = "JAZ"
# count = 0
# flag = True
# first = 0
# for i in range(len(a)):
#     if a[i] != 'A' and flag:
#         first = i
#         count +=1
#         flag = False
#     elif a[i] !='A':
#         count += 1
# # print(count)
# def rl(x):
#     l,r = count,count
#     for i in range(len(x)):
#         if x[first-i] != 'A':
#             l -=1
#             if l == 0:
#                 return -1
#         if x[first+i] !=  'A':
#             r -=1
#             if r == 0:
#                 return 1

# check = rl(a)
# result = first - 1
# for i in range(len(a)):
#     if check == -1:
#         if a[first-i] != 'A':
#             count -=1
#             result +=1
#         else:
#             result +=1
#         if count == 0:
#             break
#     else:
#         if a[first+i] != 'A':
#             count-=1
#             result +=1
#         else:
#             result += 1
#         if count == 0:
#             break
        
# for i in a:
#     if i != 'A':
#         if dic[i] > 13:
#             temp = 26-dic[i]
#             result += temp
#         else:
#             temp = dic[i]
#             result += temp

# print(result)

from collections import deque
s = 'baabaa'
result = -1


def c(s):
    q = deque(s)
    temp = deque()
    while q:
        a = q.popleft()
        if temp[-1] == a:
            
    return list(temp)
# s = (c(s))
# print(c(s))


def cut(s):
    temp = ''
    flag = True
    if len(s) == 0:
        return 1
    for i in range(len(s)):
        if i == len(s)-1 and flag:
            temp += s[i]
            continue
        elif i == len(s)-1 and flag == False:
            continue
        if s[i] != s[i+1] and flag:
            temp += s[i]
        elif s[i] == s[i+1] and flag:
            flag = False
            continue
        elif flag == False:
            flag = True
            continue
    if s == temp:
        return False
    else:
        return temp

# print(cut(s))
flag = True
while True:
    temp = c(s)
    if temp == s:
        result = 0
        break
    elif len(temp) == 0:
        result = 1
        break
    s = temp[:]

print(result)