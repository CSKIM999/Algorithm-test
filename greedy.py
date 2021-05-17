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


