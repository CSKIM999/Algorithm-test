###############################################################################################################
##########################################     Q21608 _ 상어 초등학교     #####################################
###############################################################################################################
'''
Given ) 상어초등학교에 N*N 크기의 교실이 있고 학교에 다니는 학생 수는 N*N 명이다. 학생은 1번부터 N*N번까지 번호가
        매겨져있고, 교실의 가장 
'''
# import heapq

# # n = 3

# # data = [
# #     [4, (2,5,1,7)],
# #     [3, (1,9,4,5)],
# #     [9, (8,1,2,3)],
# #     [8, (1,9,3,4)],
# #     [7, (2,3,4,8)],
# #     [1, (9,2,5,7)],
# #     [6, (5,2,3,4)],
# #     [5, (1,9,2,8)],
# #     [2, (9,3,1,4)]
# # ]
# # data = [
# #     [7, (9, 3, 8, 2)], 
# #     [5, (7, 3, 8, 6)],
# #     [3, (5, 2, 4, 9)],
# #     [9, (6, 8, 3, 4)],
# #     [8, (5, 3, 1, 6)],
# #     [6, (3, 8, 5, 4)],
# #     [2, (6, 4, 8, 7)],
# #     [1, (8, 3, 4, 5)],
# #     [4, (7, 9, 3, 8)]

# # ]


# n = int(input())
# data = []
# for i in range(n*n):
#     delta = (list(map(int,input().split())))
#     data.append([delta[0],tuple(delta[1:5])])

# table = [[0]*n for _ in range(n)]

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# def seat(lst,table):
#     delta = [[0,0,0,0] for _ in range(n*n)]
#     num,like = lst
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if table[i][j] != 0:
#                 delta[count][0] += 1
#                 delta[count][1] += 1
#                 delta[count][2] = i
#                 delta[count][3] = j
#                 count +=1
#                 continue
#             delta[count][2] = i
#             delta[count][3] = j
#             for k in range(4):
#                 x,y = i,j
#                 nx,ny = x+dx[k],y+dy[k]
#                 if 0<=nx<n and 0<=ny<n:
#                     if table[nx][ny] in like:
#                         delta[count][0] -=1
#                     elif table[nx][ny] == 0:
#                         delta[count][1] -=1
                    
#             count +=1
#     return delta

# def satisfaction(table):
#     satis = 0
#     grade = [0,1,10,100,1000]
#     for i in range(n):
#         for j in range(n):
#             num = table[i][j]
#             count = 0
#             for k in range(4):
#                 x,y = i,j
#                 nx,ny = x+dx[k],y+dy[k]
#                 if 0<=nx<n and 0<=ny<n:
#                     if table[nx][ny] in data[num-1][1]:
#                         count += 1
#             satis += grade[count]
#     return satis

# for i in data:
#     a = seat(i,table)
#     heapq.heapify(a)
#     best = heapq.heappop(a)
#     x,y = best[2:4]
#     table[x][y] = i[0]

# data.sort()
# print(satisfaction(table))

'''
1회차 > [[ line 53 to 59 ]]
        if table[i][j] != 0:
                        #  delta[count][0] += 1
                        #  delta[count][1] += 1
                        delta[count][2] = i
                        delta[count][3] = j
                        #  count +=1
                        continue
        
        what ? 
        위 코드가 before & after 코드인데 count 또한 continue 전에 한번 더해주었어야했고 이미 사용된 칸이라면 최소힙 큐를
        사용중인 내 코드의 경우엔 delta 의 0,1 인덱스에 무조건 후순위로 밀릴 수 있는 1을 더해주었어야했음.
        앉을 자리를 탐색하는 함수에서 각 자리를 탐색할 때 인접 칸에 빈칸도 없고 좋아하는 친구도 없을때 를 고려하지 않았음

        why ?
        그렇다면 왜 위의 문제를 필터링하지 못했을까?
        힙큐를 이용해 [인접 좋아하는 학생수 , 인접 빈칸, 행번호, 열번호] 를 통해 seat() 함수가 빠르게 최적의 자리를 찾아주길 원했음
        하지만 힙큐는 최소힙큐에 기반하기때문에 인접칸에 대한 앞의 두 인덱스는 음수, 좌표 번호에 대한 뒤의 두 인덱스는 양수로 넣어서
        착오가 생겼었음. 본래 코드에서 위의 주석 세 줄로 정답판정을 받을 수 있었고 사용된 번호 처리가 조금 부족했던 것 같음  
'''


###############################################################################################################
############################################     Q12100 _ 2048     ############################################
###############################################################################################################
'''
Given ) 2048 게임을 하려고 한다. n*n 의 보드에서 주어진 데이터로 5번 움직일 때 얻을 수 있는 최댓값 블록을 출력하라
        1<= N <= 20
'''
'''
1회차 > 각 방향으로의 이동함수를 작성하고 해당 함수들을 dfs 로 순회시켜서 max 값을 가져오고자 함.
'''

n = 4
data = [
    [2,2,2,0],
    [2,4,0,4],
    [8,4,4,8],
    [16,8,4,4]
]
count = 0
ans = 0
result = []
def move_right(data,ans,count):

    count +=1
    for i in range(n):
        h_count = 1
        for j in range(1,n+1):
            if j < n:
                if data[i][-j] == data[i][-j-1]:
                    data[i][-h_count] = data[i][-j]*2
                    data[i][-j-1] = 0
                    h_count += 1
                elif data[i][-j] == 0:
                    continue
                else:
                    data[i][-h_count] = data[i][-j]
                    h_count += 1
            else:
                data[i][-h_count] = data[i][0]
                if n-h_count !=0:
                    data[i][0] = 0
    if count == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans,data[i][j])
        result.append(ans)

def move_right(data):
    temp = []
    for i in range(n): #행
        for j in range(1,n+1): #열
            h_count = 1
            if j<n:
                if data[i][-j] == 0:
                    continue
                else:
                    if len(temp) == 0:
                        temp.append(data[i][-j])
                    else:
                        if temp[0] == data[i][-j]
            else:
                data[i][-h_count] = data[i][0]
                if n-h_count !=0:
                    data[i][0] = 0
            if len(temp) == 2:
                pass



def move_left(data,ans,count):
    count +=1
    for i in range(n):
        h_count = 0
        for j in range(n):
            if j < n-1:
                if data[i][j] == data[i][j+1]:
                    data[i][h_count] = data[i][j]*2
                    data[i][j+1] = 0
                    h_count += 1
                elif data[i][j] == 0:
                    continue
                else:
                    data[i][h_count] = data[i][j]
                    h_count += 1
            else:
                data[i][h_count] = data[i][j]
                if h_count != n:
                    data[i][j] = 0
    if count == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans,data[i][j])
        result.append(ans)

move_right(data,ans,count)
print(data)