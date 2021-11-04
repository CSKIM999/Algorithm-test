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
# #     m = len(grid[0])
# #     data = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
# #     for i in range(n):
# #         for j in range(m):
# #             for k in range(4):
# #                 if data[i][j][k] == 0:
# #                     count +=1
# #                     data,temp = move(k,[i,j],data,count,0,grid)
# #                     answer.append(temp)
# #     answer.sort()
# #     return answer
# #     import collections

# # a = [0,1,2,3,4,5]
# # print(a[:0] + [a[0]+a[2]] + a[3:])

# # r,c = 3,3
# # data = [[i+(c*j) for i in range(1,1+c)] for j in range(r)]
# # for i in data:
# #     print(i)

# # xy = [1,1,2,2]
# # ax,ay,bx,by = xy
# # temp = [data[ax-1][ax-1:by],[i[by-1] for i in data[ax-1:bx]],data[bx-1][ax-1:by],[i[ay-1] for i in data[ax-1:bx]]]
# # print(temp)

# # def turn(temp):
# #     alp = []
# #     for x in temp[:2]:
# #         alp.append(x[:-1])
# #     for x in temp[2:]:
# #         alp.append(x[1:])
# #     tmp = alp[:]
# #     alp[0] = [tmp[-1][0]] + tmp[0]
# #     alp[1] = [tmp[0][-1]] + tmp[1]
# #     alp[2] = tmp[2] + [tmp[1][-1]]
# #     alp[3] = tmp[3] + [tmp[2][0]]

# #     return alp
    
# # temp = turn(temp)
# # print()
# # print(temp)



# # data = [
# #     [0, 0, 0, 0, 0, 0],
# #     [0, 0, 0, 0, 0, 0],
# #     [0, 0, 1, 0, 6, 0],
# #     [0, 0, 0, 0, 0, 0]
# # ]

# # data[0][2:] = [ 4 for _ in range(len(data[0][2:]))]
# # print(data)

# # pp = [ i for i in range(5,-1,-1)]
# # print(pp)



# # def solution(n, money):
# #     answer = 0
# #     def search(n, i):
# #         nonlocal answer
# #         if i == 0:
# #             if n % money[i] == 0: #남은 돈이 최소단위로 나뉘어진다면 case 아니라면 case-out
# #                 answer += 1
# #             return
# #         else:
# #             for j in range(0, n // money[i]+1): #0~(n//money[i])+1 까지
# #                 search(n-money[i]*j, i-1)
# #     search(n, len(money)-1) #len(money)-1 = 2
# #     return answer

# # n = 5
# # money = [1,2,5]
# # for i in range(15):
# #     print(f'{i} 입니다')
# #     print(solution(i,money))

# give = []
# n,m,h = map(int,input().split())
# for i in range(m):
#     give.append(map(int,input().split()))

# def i_is_i(ladder):
#     for i in range(n):  # i가 i로 가는지 확인한다
#         col = i
#         for row in range(h):  # 마지막 가로줄(H) 가기 전까지 확인
#             if col < n-1 and ladder[row][col]:  # col번 세로선과 col+1번 세로선이 row번 가로선에 의해 연결되는가?
#                 col += 1  # 다음 세로줄로 이동
#             elif 0 < col and ladder[row][col-1]:  # col-1 세로선과 col 세로선이 row 가로선에 의해 연결되는가?
#                 col -= 1
#         if col != i:
#             return False
#     return True

# data = [[False]*(n-1) for _ in range(h)]
# for a,b in give:
#     data[a-1][b-1] = True #사다리 데이터 받아오기
# result = 4
# def dfs(x,count,limit,a):
#     global result
#     l,h = len(x[0]),len(x)
#     if count == limit:
#         if i_is_i(x):
#             result = min(result,count)
#             return
#         return
#     for i in range(a,h):
#         for j in range(l):
#             if 0<j<l-1:
#                 if x[i][j] or x[i][j-1] or x[i][j+1]:
#                     continue
#             elif j == l-1:
#                 if x[i][j] or x[i][j-1]:
#                     continue
#             else:
#                 if x[i][j] or x[i][j+1]:
#                     continue
#             x[i][j] = True
#             dfs([q[:] for q in x],count+1,limit,i)
#             if result != 4:
#                 return
#             x[i][j] = False
#     return

# for i in range(4):
#     dfs(data,0,i,0)
# if result == 4:
#     result = -1
# print(result)


def xprint(a):
    for i in a:
        print(i)
# import heapq

# n,m,k = map(int,input().split())
# now = 0
# feed = []
# woods = []
# ground = [[5]*n for _ in range(n)]

# for i in range(n):
#     feed.append(list(map(int,input().split())))
# for j in range(m):
#     a,b,c = list(map(int,input().split()))
#     heapq.heappush(woods,(c,a-1,b-1))


# def spring():
#     global ground,now,woods
#     now = 0
#     temp_spring = []
#     for _ in range(len(woods)):
#         o,x,y = heapq.heappop(woods)
#         if ground[x][y] >= o:
#             ground[x][y] -= o
#             heapq.heappush(temp_spring,(o+1,x,y))
#         else:
#             ground[x][y] += int(o/2)
#     woods = temp_spring[:]

# # def summer():
# #     global ground,woods
# #     for _ in range(len(woods)):
# #         o,x,y = heapq.heappop(woods)
# #         if o < 0:
# #             ground[x][y] += int(-o/2)
# #         else:
# #             heapq.heappush(woods,(o,x,y))
# #             break
    

# def fall():
#     global ground,woods
#     temp_fall = []
#     for _ in range(len(woods)):
#         o,x,y = heapq.heappop(woods)
#         if o % 5 == 0:
#             for q in range(-1,2):
#                 for w in range(-1,2):
#                     if 0<=x+q<n and 0<=y+w<n:
#                         if q==0 and w==0:
#                             continue
#                         heapq.heappush(temp_fall,(1,x+q,y+w))
#             heapq.heappush(temp_fall,(o,x,y))
#         else:
#             heapq.heappush(temp_fall,(o,x,y))
#     woods = temp_fall[:]


# def winter():
#     global ground,now
#     for i in range(n):
#         for j in range(n):
#             ground[i][j] += feed[i][j]
#     now = len(woods)


# for _ in range(k):
#     spring()
#     # summer()
#     fall()
#     winter()
#     # print(woods)
# print(len(woods))

n,m,k = map(int,input().split())
now = 0
feed = []
woods = []
ground = [[5]*n for _ in range(n)]
db = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    feed.append(list(map(int,input().split())))
for j in range(m):
    woods.append(list(map(int,input().split())))
for x,y,z in woods:
    db[x-1][y-1].append(z)


for _ in range(k):
    #성장과 죽음
    for i in range(n): 
        for j in range(n):
            db[i][j].sort()
            for k in range(len(db[i][j])):
                if ground[i][j] >= db[i][j][k]:
                    ground[i][j] -= db[i][j][k]
                    db[i][j][k] += 1
                else:
                    for q in db[i][j][k:]:
                        ground[i][j] += q//2
                    db[i][j] = db[i][j][:k]
                    break
    
    #번식
    for i in range(n): 
        for j in range(n):
            if len(db[i][j]) != 0:
                for k in range(len(db[i][j])):
                    if db[i][j][k]%5 == 0:
                        for q in range(-1,2):
                            for w in range(-1,2):
                                if 0<=i+q<n and 0<=j+w<n:
                                    if q==0 and w==0:
                                        continue
                                    db[i+q][j+w].append(1)

    #r2d2
    for i in range(n):
        for j in range(n):
            ground[i][j] += feed[i][j]
now = 0
for i in range(n):
    for j in range(n):
        if len(db[i][j]) != 0:
            now += len(db[i][j])

print(now)