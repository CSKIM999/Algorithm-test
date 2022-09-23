from itertools import combinations
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

dic = {}
for x in course:
    dic[x] = {}
orders = [[ord(j) for j in i] for i in orders]
for x in orders:
    x.sort()
L = len(orders)
result = []
hist = []
for i in range(L):
    now = orders[i]
    for q in course:  # 2 , 3 , 4
        seq = list(combinations(now, q))
        for s in seq:  # AB , BC
            if s in hist:
                continue

            c = 0
            for j in range(L):

                if i == j:
                    continue

                if len(set(s) & set(orders[j])) == len(s):
                    c += 1
                    continue
            if c:
                try:
                    dic[q][c].append(s)
                except KeyError:
                    dic[q][c] = [s]
                hist.append(s)

for q in course:
    if dic[q]:
        now = dic[q][max(dic[q])]
        for x in now:
            x = list(x)
            x.sort()
            result.append("".join([chr(i) for i in x]))
result.sort()
print(result)


# for j in range(L):
#     if i == j:
#         continue
#     nxt = orders[j]
#     itsn = list(set(now) & set(nxt))
#     l = len(itsn)
#     if l in course and itsn not in hist:
#         c = 0
#         for k in range(L):
#             if (list(set(orders[k]) & set(itsn))) == itsn:
#                 c += 1
#         try:
#             dic[l][c].append(itsn)
#         except KeyError:
#             dic[l][c] = [itsn]
#         hist.append(itsn)
# for i in course:
#     if dic[i]:
#         now = dic[i]
#         for j in now[max(now)]:
#             res.append(j)
# result = []
# for i in range(len(res)):
#     res[i].sort()
#     result.append("".join([chr(x) for x in res[i]]))
# result.sort()
# print(result)


# res.sort(key=lambda x: x)

# for x in range(len(res)):
#     res[x] = "".join([chr(i) for i in res[x]])
# print(res)

'''
카카오가 특히 좀 순열이나 조합을 사용하면 쉬운편이 많은듯?
'''


print(len(list(combinations(range(20), 4))))
