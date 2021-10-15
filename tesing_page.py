# def rot(node,dest,grid):
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
    
# def move(dest,node,give,count,len_count,grid):
#     len_count+=1
#     n = len(grid)
#     m = len(grid[0])
#     dx,dy = [-1,0,1,0],[0,1,0,-1]
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
#     ndest = rot([nx,ny],dest,grid)
#     give[x][y][dest] = count
#     if give[nx][ny][ndest] !=0:
#         return give,len_count
#     return move(ndest,[nx,ny],[i[:] for i in give[:]],count,len_count,grid)
    
# def solution(grid):
#     count = 0
#     answer = []
#     n = len(grid)
#     m = len(grid[0])
#     data = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             for k in range(4):
#                 if data[i][j][k] == 0:
#                     count +=1
#                     data,temp = move(k,[i,j],data,count,0,grid)
#                     answer.append(temp)
#     answer.sort()
#     return answer
#     import collections

# a = [0,1,2,3,4,5]
# print(a[:0] + [a[0]+a[2]] + a[3:])

# r,c = 3,3
# data = [[i+(c*j) for i in range(1,1+c)] for j in range(r)]
# for i in data:
#     print(i)

# xy = [1,1,2,2]
# ax,ay,bx,by = xy
# temp = [data[ax-1][ax-1:by],[i[by-1] for i in data[ax-1:bx]],data[bx-1][ax-1:by],[i[ay-1] for i in data[ax-1:bx]]]
# print(temp)

# def turn(temp):
#     alp = []
#     for x in temp[:2]:
#         alp.append(x[:-1])
#     for x in temp[2:]:
#         alp.append(x[1:])
#     tmp = alp[:]
#     alp[0] = [tmp[-1][0]] + tmp[0]
#     alp[1] = [tmp[0][-1]] + tmp[1]
#     alp[2] = tmp[2] + [tmp[1][-1]]
#     alp[3] = tmp[3] + [tmp[2][0]]

#     return alp
    
# temp = turn(temp)
# print()
# print(temp)


'''
6 7
4 3 3
1 1 1 1 1 1 1
1 0 1 0 1 1 1
1 0 1 0 0 0 1
1 0 0 0 1 1 1
1 1 1 0 1 1 1
1 1 1 1 1 1 1
'''