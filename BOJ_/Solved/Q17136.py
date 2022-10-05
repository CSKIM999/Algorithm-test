from itertools import combinations
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q17136
#######  TODAY  #######
##### 2022. 09. 28 #####
GIVEN ) 10*10 크기의 테이블에 빈칸이 랜덤으로 주어진다.
        1~5 의 정사각 크기의 색종이가 각 크기별로 5장씩 주어지며
        가지고 있는 색종이만으로 모든 빈칸을 덮고자 한다.
        

INPUT ) 

OUTPUT) 

Approach )  
'''


input = sys.stdin.readline


def func(x, y, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return
    if x >= 10:
        func(0, y+1, cnt)
        return

    if a[x][y] == 1:
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if a[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 0

                paper[k] += 1
                func(x + k + 1, y, cnt + 1)
                paper[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 1
    else:
        func(x + 1, y, cnt)


a = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = sys.maxsize
func(0, 0, 0)
if ans != sys.maxsize:
    print(ans)
else:
    print(-1)


# res = 0

# table = [list(map(int, input().split())) for _ in range(10)]
# blnk = 0
# dic = {i: set() for i in range(1, 6)}
# hashmap = set()


# def check(node):
#     x, y = node
#     s = [1]
#     for i in range(1, 5):
#         nx, ny = x+i+1, y+i+1
#         if 0 <= nx < 11 and 0 <= ny < 11:
#             temp = sum([sum(j[y:y+i+1]) for j in table[x:x+i+1]])
#             if temp == (i+1)**2:
#                 s.append(i+1)
#     return s


# for i in range(10):
#     for j in range(10):
#         if table[i][j] == 1:
#             blnk += 1
#             s = check([i, j])
#             for x in s:
#                 dic[x].add((i, j))
# blocks = []
# for i in range(1, 6):
#     if len(dic[i]) < 5:
#         blocks.extend([i]*len(dic[i]))
#     else:
#         if i == 5:
#             blocks.extend([i]*4)
#         else:
#             blocks.extend([i]*5)
# flag = 0

# for a in range(5):
#     hflag = True
#     temp = []
#     ta = 0
#     if blnk < 25*a:
#         break
#     temp.extend([5]*a)
#     ta += 25*a
#     if ta == blnk:
#         hashmap.add(tuple(temp))
#         continue
#     for b in range(6):
#         if blnk < (ta + 16*b if b != 0 else ta):
#             break
#         tempb = temp[:]
#         tempb.extend([4]*b)
#         tb = ta + 16*b
#         if tb == blnk:
#             tempb.sort()
#             hashmap.add(tuple(tempb))
#             break
#         for c in range(6):
#             if blnk < (tb + 9*c if c != 0 else tb):
#                 break
#             tempc = tempb[:]
#             tempc.extend([3]*c)
#             tc = tb + 9*c
#             if tc == blnk:
#                 tempc.sort()
#                 hashmap.add(tuple(tempc))
#                 break
#             for d in range(6):
#                 if blnk < (tc + 4*d if d != 0 else tc):
#                     break
#                 tempd = tempc[:]
#                 tempd.extend([2]*d)
#                 td = tc + 4*d
#                 if td == blnk:
#                     tempd.sort()
#                     hashmap.add(tuple(tempd))
#                     break

#                 for e in range(6):
#                     if blnk < (td + e if e != 0 else td):
#                         break
#                     tempe = tempd[:]
#                     tempe.extend([1]*e)
#                     te = td + e
#                     if te == blnk:
#                         tempe.sort()
#                         hashmap.add(tuple(tempe))
#                         break


# def dfs(filled, lst, depth):
#     global flag
#     now = lst[depth]
#     opt = dic[now] - filled
#     for i in opt:
#         oflag = True
#         x, y = i
#         optlst = []
#         for j in range(now):
#             optlst.extend([(x+j, y+q) for q in range(now)])
#         for j in optlst:
#             if j in filled:
#                 oflag = False
#                 break
#         if oflag:
#             if depth == len(lst)-1:
#                 flag = len(lst)
#                 return
#             filled.update(optlst)
#             dfs(filled, lst, depth+1)
#             for j in optlst:
#                 filled.remove(j)
#         if flag:
#             return


# if blnk == 0:
#     print(0)
# else:
#     for i in range(25):
#         comb = set(combinations(blocks, i))
#         for j in comb:
#             if j not in hashmap:
#                 continue
#             j = list(j)
#             j.sort(reverse=True)
#             dfs(set(), j, 0)
#             if flag:
#                 break
#         if flag:
#             break

#     if flag == 0:
#         print(-1)
#     else:
#         print(flag)


# blocks = [0, 0, 0, 0, 0, 0]
# res = 0
# v = set()
# table = [list(map(int, input().split())) for _ in range(10)]
# blnk = 0
# dic = {i: {} for i in range(10)}


# def check(node):
#     x, y = node
#     s = [1]
#     for i in range(1, 5):
#         nx, ny = x+i+1, y+i+1
#         if 0 <= nx < 11 and 0 <= ny < 11:
#             temp = sum([sum(j[y:y+i+1]) for j in table[x:x+i+1]])
#             if temp == (i+1)**2:
#                 s.append(i+1)
#     s.sort(reverse=True)
#     return s


# for i in range(10):
#     for j in range(10):
#         if table[i][j] == 1:
#             blnk += 1
#             s = check([i, j])
#             for x in s:
#                 try:
#                     dic[i][j].append(x)
#                 except KeyError:
#                     dic[i][j] = [x]

# flag = False
# result = [0, 5, 5, 5, 5, 5]


# def ds(visit, start):
#     global flag, result
#     if flag and sum(blocks) > sum(result):
#         return
#     x, y = start
#     for i in range(x, 10):
#         for j in range(10):
#             if (i, j) in visit:
#                 continue
#             if table[i][j] == 0:
#                 continue
#             if flag and sum(blocks) > sum(result)-2:
#                 return
#             lst = dic[i][j]
#             for l in lst:
#                 lflag = False
#                 if blocks[l] == 5:
#                     continue
#                 temp = []
#                 for li in range(l):
#                     temp.extend([(i+li, j+k) for k in range(l)])
#                 for t in temp:
#                     if t in visit:
#                         lflag = True
#                 if lflag:
#                     continue
#                 visit.update(temp)
#                 blocks[l] += 1
#                 ds(visit, [i, j])
#                 for t in temp:
#                     visit.remove(t)
#                 blocks[l] -= 1
#     visit = list(visit)
#     visit.sort()
#     if len(visit) == blnk:
#         flag = True
#         result = blocks[:]


# ds(v, [0, 0])
# if result == 1e9:
#     result = -1
# print(result)
