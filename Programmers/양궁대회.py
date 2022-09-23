from itertools import combinations_with_replacement

board = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
n = 10
dic = {}
cid = {}
for i in range(11):
    dic[10-i] = i
    cid[i] = 10-i
seq = list(combinations_with_replacement(range(11), n))
res = [0, 0]
result = []
for s in seq:
    lst = [0 for _ in range(11)]
    c = 0
    for n in s:
        lst[dic[n]] += 1
    for i in range(11):
        if board[i] < lst[i]:
            c += cid[i]
        elif board[i] >= lst[i]:
            if board[i] == 0:
                continue
            else:
                c -= cid[i]
    if res[0] <= c and c:
        nc = 0
        for i in range(11):
            if lst[i]:
                nc += lst[i]*i
        if res[0] == c:
            if res[1] < nc:
                res = [c, nc]
                result = lst[:]
        else:
            res = [c, nc]
            result = lst[:]

print(result)
