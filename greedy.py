from collections import deque
from functools import partial

########### 동전 거슬러주기 ###########

# n = 1260
# count = 0

# coin_types=[500,100,50,10]
# for coin in coin_types:
#     count+=n//coin
#     n%=coin


# print(count)


########### N,M,K 큰수의 법칙 ###########
# m, k=map(int,input().split())
# data = list(map(int,input().split()))

# n = len(data)
# data.sort()
# result = 0
# count = 0
# for i in range(m):
#     if count == k:
#         print('둘째 큰 값')
#         result += data[-2]
#         count = 0
#     else:
#         print('첫번째로 큰 값')
#         result += data[-1]
#         count +=1

# print('총합은 :' + str(result))
    


########### 숫자 카드 게임 ###########
# n = int(input())
# result = []
# for i in range(n):
#     data = list(map(int,input().split()))
#     data.sort()
#     result.append(data[0])
# result.sort()
# print(result[-1])


########### 1이 될 때 까지 ###########
# n, k = map(int,input().split())
# count = 0
# while True:
#     if n % k !=0:
#         if n == 1:
#             break
#         n -=1
#         count +=1
#         print('1'+ '  n :' +str(n))
#     elif n != 0:
#         n = n/k
#         count +=1
#         print('2' + '  n :' +str(n))
    
#     else:
#         print('END')
#         break

# print(count)

########### 시간 속 3 ###########

# n = int(input())
# count=0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in (str(i)+str(j)+str(k)):
#             # if 3 in (str(i)+str(j)+str(k)):  <<= str 값 안에 3 이 있는가를 비교해야하므로 3또한 str로 바꿔야함
#                 count+=1

# print(count)
########### 상하좌우 ###########

# moves = input().split()
# limit=5
# location = [1,1]
# lst={'L':-1,'R':1,'D':1,'U':-1}

# for move in moves:
#     if move == 'L' or move == 'R':
#         print('X')
#         location[1] += lst[move]
#         if location[1] == 0:
#             location[1] = 1
#         elif location[1] > limit:
#             location[1] = limit
#     if move =='D' or move == 'U':
#         print('Y')
#         location[0] += lst[move]
#         if location[0] == 0:
#             location[0] = 1
#         elif location[0] > limit:
#             location[0] = limit
    

# print(location[0], location[1])





########### 체스판 나이트의 움직임 ###########

# print('나이트의 위치를 입력해주세요 : ',end='')


# data = input()
# values = ('a','b','c','d','e','f','g','h')
# if (int(data[1])<1 or int(data[1])>8) or (data[0].lower() not in values):
#     print('\"A1\" 과 같이 기본형식에 맞춰 입력해주세요')
#     raise ValueError
# area = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
# data_mapping = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

# loc = (int(data[1]),data_mapping[data[0].lower()])
# count = 8
# for i in area:
#     grid = [loc[0]+i[0],loc[1]+i[1]]
#     if (grid[0] > 8 or grid[0] <1 ) or ( grid[1] >8 or grid[1] < 1):
#         count -=1

# print(count)

########### 게임 시뮬레이션 ###########
# 북 서 남 동 순서 0 1 2 3
# i=0

# dx= [-1,0,1,0]
# dy= [0,-1,0,1]
# x,y = 1,1
# hist = []
# location = (x,y)
# hist.append(location)
# map_data = [(1,1,1,1),(1,0,0,1),(1,1,0,1),(1,1,1,1)]
# turn_count = 0
# def turn():
#     global i
#     i+=1
#     if i == 4:
#         i=0

# while True:
#     turn()
#     nx = x+dx[i]
#     ny = y+dy[i]
#     if map_data[nx][ny] ==1 or (nx,ny) in hist:
#         turn_count+=1
#         pass
#     elif map_data[nx][ny] ==0 and (nx,ny) not in hist:
#         x,y = nx,ny
#         location = (x,y)
#         hist.append(location)
#         print('move! {}'.format(location))
#         turn_count = 0
#     if turn_count == 4:
#         if map_data[x-dx[i]][y-dy[i]] == 1:
#             break
#         x,y = x-dx[i],y-dy[i]
#         location = (x-dx[i],y-dy[i])
#         turn_count =0


# print(len(hist))



###################### 아이스크림 덩어리세기 ######################

# n,m = 3,3
# graph = [
#     [0,0,1],
#     [0,1,0],
#     [1,0,1]
# ]

# def dfs(x,y):
#     # 범위를 벗어날 경우 즉시종료
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
#     # 현재 노드를 만약 방문하지 않았다면
#     if graph[x][y] ==0:
#         # 해당 노드 방문처리
#         graph[x][y] =1
#         # 현재 위치에서 상, 하, 좌, 우 모두 재귀적 호출
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False

# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i,j) ==True:
#             result +=1
# """
# 한번의 메서드 dfs 에서 True 가 몇번 return 되는지는 중요하지 않았다
# line 173 에서의 조건문은 메인 메서드 dfs 값이 True 인지 아닌지만 확인된다면
# result 값을 1 더하는 것일 뿐, 메인 메서드에서 재귀로 인한 메서드가 호출되고 
# 그 호출 메서드의 return True 값은 result 에 영향을 주지 않음
# 물론 당연히도 호출 메서드가 True 를 return 한다면 메인 메서드 또한 True를 return할 것이기 때문에
# 호출 메서드의 True return 이 의미가 없는것은 아닐 듯 함
# """

# print(result)

###################### 최단거리 길찾기 ######################

# n,m = 4,7

# graph = [
#     [1,0,1,1,1,1,1],
#     [1,0,1,0,1,0,1],
#     [1,0,1,0,1,0,1],
#     [1,1,1,0,1,0,1]
# ]
# x,y=0,0

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# count = 0
# def bfs(x,y):
#     global count

#     start =[x,y]
#     queue =deque([start])
#     while queue:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             new = [nx,ny]
#             if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
#                 count +=1
#             elif (graph[nx][ny] ==1) and (new not in queue):
#                 queue.append(new)
#                 x=nx
#                 y=ny
#                 count = 0

#             elif (graph[nx][ny] ==0) or (new in queue):
#                 count +=1

            
#             if count == 4:
#                 count = 0
#                 graph[x][y] = 0
#                 v = queue.pop()
#                 x= v[0]
#                 y= v[1]
#                 print('pop')
                

#         if x == n-1 and y == m - 1:
#             print(len(queue))
#             break

# bfs(0,0)

# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()
#         print(x,y,y)
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]

# print(bfs(0,0))


###################### 성적순 정렬 ######################


# print('학생 수를 입력해주세요 : ',end='')
# Input =[]
# n = int(input())
# for i in range(n):
#     Input.append(input().split())
#     map(int,Input[i][1])

# Input =[
#     ['이순신',95],
#     ['홍길동',85],
#     ['김찬섭',88]
# ]

# Input.sort(key=lambda Input : Input[1])
# # Input = sorted(Input, key=lambda Input : Input[1])

'''
sort 와 sorted 의 사용법을 구분하자
'''


###################### 두 배열의 원소 교체 ######################

# n,k = 5,3

# A = [1,2,5,4,3]
# B = [5,5,6,6,5]

# A.sort()
# B.sort(reverse=True)

# print(A,B)

# for i in range(k):
#     A[i],B[i] = B[i],A[i]

# print(A,B)

# print('답은 :' + str(sum(A)))

###################### 부품 찾기 ######################
'''
이 문제를 이진탐색으로도, 집합자료형으로도 풀어보고자 한다
'''
# # binary-search
# n = 5 #내가 가지고있는 부품의 종류
# n_list = [8,3,7,9,2]

# m = 3 #원하는 부품의 종류 수
# m_list = [5,7,9]

# # return 은 가지고있는지 없는지 여부를 'yes' or 'no' 로 입력
# n_list.sort()
# m_list.sort()

# def binary_search(array,target,start,end):
#     mid = (start+end) // 2
#     if len(array[start:end+1]) ==2 and target !=array[start] and target !=array[end]:
#         print('No')
#         return False
    
#     if target == array[mid]:
#         print('Yes')
#         return True
#     elif target > array[mid]:
#         return binary_search(array,target,mid+1,end)
#     elif target<array[mid]:
#         return binary_search(array, target,start,mid-1)

# for i in m_list:
#     result = binary_search(n_list,i,0,len(n_list)-1)
#     if result == True:
#         print('{} 번 부품은 보유중입니다.'.format(i))
#     else:
#         print('{} 번 부품은 보유중이지 않습니다.'.format(i))

# # 집합자료형
# n = 5 #내가 가지고있는 부품의 종류
# n_list = [8,3,7,9,2]

# m = 3 #원하는 부품의 종류 수
# m_list = [5,7,9]

# n_list,m_list = set(n_list),set(m_list)
# print(type(n_list))
# print(n_list)
# # set 자료형은 알아서 오름차순으로 정렬이 됨.

# for i in m_list:
#     if i in n_list:
#         print('yes')
#     else:
#         print('no')



