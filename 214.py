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

