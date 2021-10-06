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
from collections import deque
data = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = -1
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    queue = deque([[0,0,1]])
    rot = [[1,0],[-1,0],[0,1],[0,-1]]
    if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
        return -1
    while queue:
        x,y,count = queue.popleft()
        for a,b in rot:
            nx,ny = x+a,y+b
            if 0<=nx<m and 0<=ny<n:
                if maps[nx][ny] == 1 and visited[nx][ny] ==0:
                    queue.append([nx,ny,count+1])
                    visited[nx][ny] = 1
                if nx == n-1 and ny==m-1:
                    answer = count+1
                    break


    return answer

print(solution(data))

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