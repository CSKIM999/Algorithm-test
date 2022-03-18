# from collections import deque
# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# visit = [ -1 for _ in range(n)]
# count = 0
# def bfs(C,ind):
#     visit[ind] = C

#     q = deque([ind])
#     while q:
#         now = q.popleft()
#         for i in range(n):
#             if visit[i] == -1 and computers[now][i]:
#                 q.append(i)
#                 visit[i] = C


# for node in range(n):
#     if visit[node] == -1:
#         bfs(count,node)
#         count +=1


# print(count)

'''
1트 솔브
'''

