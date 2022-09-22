# from collections import deque

# n = 10
# info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
# a = []
# point = [i for i in range(10, -1, -1)]
# pts = [-1 if _ > 0 else 0 for _ in info]
# compete = [i+1 for i in info]
# result = [0 for _ in range(11)]
# competePoint = []
# for i in range(11):
#     cp = point[i]
#     if pts[i] == -1:
#         cp *= 2
#         a.append(point[i])
#     cp /= compete[i]
#     competePoint.append([cp, compete[i], i])

# competePoint.sort(reverse=True)
# q = deque()
# sol = [0, 0]
# for item in competePoint:
#     exp, rsc, index = item
#     lst = [0 for _ in range(11)]
#     lst[index] = rsc
#     target = point[index]
#     diff = -sum(a) + target
#     if target in a:
#         diff += target
#     q.append([n-rsc, diff, lst[:]])
# while q:
#     rsc, diff, lst = q.popleft()
#     if rsc == 0:
#         if diff >= sol[0]:
#             s = 0
#             if lst == result:
#                 continue
#             for i in range(11):
#                 s += i*lst[i]
#             # if diff >= sol[0]:
#             #     if sum(lst) > sol[1]:
#             #         result = lst
#             if s > sol[1]:
#                 sol = [diff, s]
#                 result = lst
#             continue
#     for item in competePoint:
#         e, r, i = item
#         earn = point[i]

#         # 남은 횟수보다 비싼가
#         if rsc < r:
#             continue
#         # 이미 담은 적있는 표적
#         tlst = lst[:]
#         if lst[i] != 0:
#             tlst[i] += 1
#             q.append([rsc-1, diff, tlst[:]])
#             continue
#         # 뺏는 표적인가
#         if pts[i] == -1:
#             earn *= 2
#         tlst[i] += r
#         q.append([rsc-r, diff+earn, tlst[:]])

# print(result)

# # for item in competePoint:
# #     exp, rsc, index = item
# #     if rsc <= n:
# #         n -= rsc
# #         pts[index] = 1
# #         result[index] = rsc
# #         if n == 0:
# #             break
# # a, r = 0, 0
# # for i in pts:
# #     if i == 1:
# #         r += 1
# #     elif i == -1:
# #         a += 1

# # if a < r:
# #     print(result)
# # else:
# #     print(-1)


from itertools import combinations_with_replacement
dic = {}
for i in range(11):
    dic[10-i] = i
n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
comb = list(combinations_with_replacement(range(11), n))
result = [0, 0]
for i in comb:
    t, ti = 0, 0
    lst = info[:]
    for j in i:
        aim = dic[j]
        lst[aim] -= 1

    for j in range(10):
        if lst[j] > 0:
            # a
            t -= dic[i]
            pass
        elif lst[j] < 0:
            # p
            t += dic[i]
            pass
