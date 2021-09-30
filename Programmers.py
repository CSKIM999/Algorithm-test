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
'''
전체 스테이지 개수 N
현재 사용자의 스테이지 번호가 담긴 배열 stages
실패율 = 해당 스테이지번호 수/ 스테이지번호 이상의 수
'''
N = 4
stages = [4,4,4,4,4]
length = len(stages)
stages.sort()
count = length
P = [[i,0,0] for i in range(N+2)]
print(P)
for i in stages:
    P[i][1] += 1
for i in range(N+1):
    count -= P[i][1]
    P[i][2] = count
result = [[i,1] for i in range(N+1)]
for i in range(N+1):
    if P[i][2] == 0:
        result[i][1] = 1
    else:
        result[i][1] = P[i][1]/P[i][2]
result = sorted(result[1:],key= lambda x: -x[1])
answer = []
for i in result:
    answer.append(i[0])
print(answer)