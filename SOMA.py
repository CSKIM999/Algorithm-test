# 4
from itertools import *
from collections import deque
test = ["AD", "BD", "CA", "BA", "DD", "AC"]
dic = {ord(i): -1 for i in ["A", "B", "C", "D"]}
arr = [[ord(j) for j in list(i)] for i in test]

al = len(arr)

q = deque()
q.append([arr[:], 0])
result = 1e9


def play(array, count):
    global result
    m = 0
    lst = []
    td = {ord(i): 0 for i in ["A", "B", "C", "D"]}
    for i in range(al):
        for j in range(2):
            nowj = array[i][j]
            if dic[nowj] == -1:
                dic[nowj] = [i, j]
            elif dic[nowj][0] == i:
                dic[nowj] = -1
            else:
                bi, bj = dic[nowj]
                v = i-bi
                td[nowj] = max(td[nowj], v)
                if v > m:
                    lst = [[(bi, bj), (i, j), nowj]]
                    m = v
                elif v == m:
                    lst.append([(bi, bj), (i, j), nowj])
                else:
                    continue
    if len(lst) == 0:
        if result == 1e9:
            result = count
        else:
            result = min(count, result)
        return

    for a, b, v in lst:
        i1, j1 = a
        i2, j2 = b
        temp = array[:]

        for k in range(2):
            temp[i1+1][k], temp[i1][j1] = temp[i1][j1], temp[i1+1][k]
            q.append([[t[:] for t in temp[:]], count+1])
            temp[i1+1][k], temp[i1][j1] = temp[i1][j1], temp[i1+1][k]
        for h in range(2):
            temp[i2-1][h], temp[i2][j2] = temp[i2][j2], temp[i2-1][h]
            q.append([[t[:] for t in temp[:]], count+1])
            temp[i2-1][h], temp[i2][j2] = temp[i2][j2], temp[i2-1][h]


# while q:
#     ar, c = q.popleft()
#     if result != 1e9 and result < c:
#         continue===
#     dic = {ord(i): -1 for i in ["A", "B", "C", "D"]}
#     play(ar, c)

# print(result)

'''
되긴 되는데 아닌거같은디

'''
print(len(list(combinations(range(12), 2))))
