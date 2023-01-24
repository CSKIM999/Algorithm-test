from collections import deque


alp, cop = 0, 0
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2],
            [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]

answer = 0
maxAl = max([i[0] for i in problems])
maxCo = max([i[1] for i in problems])
if maxAl <= alp:
    alp = maxAl
if maxCo <= cop:
    cop = maxCo
dic = {(alp, cop): [[1, 0, 1], [0, 1, 1]]}

for al in range(maxAl+1):
    for co in range(maxCo+1):
        dic[(al, co)] = []
        for a, c, b, d, e in problems:
            if a <= al and c <= co:
                dic[(al, co)].append((b, d, e))
dp = [[1e3 if i > cop or j > alp else 0 for i in range(
    maxCo+1)] for j in range(maxAl+1)]


# for i in range(maxAl+1):
#     for j in range(maxCo+1):
#         if dp[i][j] == 0:
#             continue
#         if i == 0 or j == 0:
#             if i == 0:
#                 if j == 0:
#                     continue
#                 dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
#             else:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
#         else:
#             for x, y, t in [[1, 0, 1], [0, 1, 1], *dic[(i, j)]]:
#                 dp[i][j] = min(dp[i][j], dp[i-x][j-y]+t)

q = deque()
q.append([0, alp, cop])
while q:
    cost, al, co = q.popleft()

    for x, y, c in [[1, 0, 1], [0, 1, 1], *dic[(al, co)]]:
        mCost, mAl, mCo = cost+c, al+x, co+y
        if mAl > maxAl:
            mAl = maxAl
        if mCo > maxCo:
            mCo = maxCo
        tCost = dp[mAl][mCo]
        if tCost != 1e3 and tCost < mCost:
            continue
        if tCost > mCost:
            dp[mAl][mCo] = mCost
            if mAl == maxAl and mCo == maxCo:
                continue
            q.append([mCost, mAl, mCo])


answer = dp[-1][-1]

[print(i) for i in dp]
print(answer)
