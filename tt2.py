# survey = ["TR", "RT", "TR"]
# choices = [7, 1, 3]


# n = len(survey)
# table = [[0,0] for _ in range(4)]
# name = [["R","T"],["C","F"],["J","M"],["A","N"]]
# key = {"R":[0,0],"T":[0,1],"C":[1,0],"F":[1,1],"J":[2,0],"M":[2,1],"A":[3,0],"N":[3,1],1:3,2:2,3:1,4:0,5:1,6:2,7:3}
# for i in range(n):
#     temp = list(survey[i])
#     # index 반환
#     dag,ag = key[temp[0]],key[temp[1]]
#     point = key[choices[i]]
#     if choices[i] < 4:
#         j,k = dag
#         table[j][k] += point
#     elif choices[i] > 4:
#         j,k = ag
#         table[j][k] += point
        
# print(table)
# answer = ""
# for i in range(4):
#     if table[i][0] >= table[i][1]:
#         answer += name[i][0]
#     else:
#         answer += name[i][1]
# print(answer)


#####################################
# # tc 1 에러???
# from collections import deque
# queue1,queue2 = [1,2,3],[4,5,7]
# q1,q2 = deque(queue1),deque(queue2)
# dic = {}
# n = len(queue1)
# sq1,sq2 = sum(queue1),sum(q2)
# print(sq1,sq2)
# total = sq1 + sq2
# # 가장 크게 2분이 안되는경우
# if total%2 != 0:
#     print(-1)
# answer = -1
# for i in range(n*3):
#     if sq1==sq2:
#         answer = i
#         break
#     if sq1>sq2:
#         a = q1.popleft()
#         q2.append(a)
#         sq1 -= a
#         sq2 += a
#     else:
#         a = q2.popleft()
#         q1.append(a)
#         sq1 += a
#         sq2 -= a
# print(answer)



#$####################################
#$####################################

### 효율성 제고
rc =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
print(rc+operations)
    # 정확성 통과, 효율성 실패
def solution(rc, operations):
    # 정확성 통과, 효율성 실패
    n = len(rc)
    def rotate():
        hand = None
        for i in range(len(rc)):
            if i == 0 or i == len(rc)-1:
                if i == 0:
                    hand = rc[i][-1]
                    rc[0] = [rc[1][0]] + rc[0][:-1]
                else:
                    rc[i] = rc[i][1:] + [hand]
            else:
                new = rc[i][-1]
                rc[i][0],rc[i][-1] = rc[i+1][0],hand
                hand = new
    def Nrotate(ss):
        g,s = len(rc[0]),len(rc)
        l,r = [],[]
        for i in range(len(rc)):
            l.append(rc[i][0])
            r.append(rc[i][-1])
        total = []
        b = rc[-1][:]
        b.reverse()
        l.reverse()
        total += rc[0][:]
        total += r[1:]
        total += b[1:-1]
        total += l[:-1]
        total[:] = total[-ss:] + total[:-ss]
        ind = 0
        t = total[0:g]
        ind += g-1
        r = total[ind:ind+s]
        ind +=s-1
        b = total[ind:ind+g]
        ind += g-1
        l = total[ind:]+[total[0]]
        rc[0] = t
        rc[-1] = b
        for i in range(n):
            
        
    Nrotate(2)
    def shiftRow(n):
        rc[:] = (rc[-n:] + rc[:-n])
    order = 0
    for i in operations:
        if i == "Rotate":
            if order:
                shiftRow(order)
                order = 0
            rotate()
        else:
            order += 1
            order %= n
    answer = rc
    return answer

print(solution(rc,operations))
#$####################################
#$####################################

## 4
# n = 7
# paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
# summits = [1,5]
# gates = [3,7]
# from collections import deque
# pathdata = {}
# nodelink = [[] for _ in range(n+1)]
# for f,t,c in paths:
#     try:
#         pathdata[c].append([f,t])
#     except KeyError:
#         pathdata[c] = [[f,t]]
# links = list(pathdata)
# links.sort()

# def bfs(node):
#     # q 가 비어있다면?
#     hist = []
#     ret = []
#     q = deque(nodelink[node])
#     while q:
#         now = q.popleft()
#         hist.append(now)
#         for i in nodelink[now]:
#             if i in summits:
#                 ret.append(i)
#             if i not in hist:
#                 q.append(i)
#     if ret:
#         return ret[0]
#     else:
#         return False

    
# for cost in links:
#     costlst = pathdata[cost]
#     for a,b in costlst:
#         nodelink[a].append(b)
#         nodelink[b].append(a)
#     for st in gates:
#         check = bfs(st)
#         if check == False:
#             continue
#         return ([check,cost])



#  [14,15,16 ][20,21,22 24]
# from collections import deque
# def solution(n, paths, gates, summits):
#     #일부 시간초과, 일부 틀림
#     pathdata = {}
#     nodelink = [[] for _ in range(n+1)]
#     for f,t,c in paths:
#         try:
#             pathdata[c].append([f,t])
#         except KeyError:
#             pathdata[c] = [[f,t]]
#     links = list(pathdata)
#     links.sort()
#     def bfs(node):
#         # q 가 비어있다면?
#         hist = []
#         ret = []
#         q = deque(nodelink[node])
#         while q:
#             now = q.popleft()
#             hist.append(now)
#             for i in nodelink[now]:
#                 if i in summits:
#                     return i
#                 if i not in hist:
#                     q.append(i)
#         if ret:
#             return ret[0]
#         else:
#             return False
            
#     answer = []
#     for cost in links:
#         costlst = pathdata[cost]
#         for a,b in costlst:
#             nodelink[a].append(b)
#             nodelink[b].append(a)
#         for st in gates:
#             check = bfs(st)
#             if check == False:
#                 continue
#             if answer:
#                 if answer[0] < check:
#                     continue
#                 else:
#                     answer = [check,cost]
#             else:
#                 answer = [check,cost]
#         if answer:
#             return answer



## 4
# n = 7
# paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
# summits = [1,5]
# gates = [3,7]
# from collections import deque
# pathdata = {}
# nodelink = [[] for _ in range(n+1)]
# for f,t,c in paths:
#     try:
#         pathdata[c].append([f,t])
#     except KeyError:
#         pathdata[c] = [[f,t]]
# links = list(pathdata)
# links.sort()
# def bfs(node):
#     # q 가 비어있다면?
#     hist = []
#     ret = []
#     q = deque(nodelink[node])
#     while q:
#         now = q.popleft()
#         hist.append(now)
#         for i in nodelink[now]:
#             if i in gates:
#                 return i
#             if i not in hist:
#                 q.append(i)
#     return False
        
# answer = []
# for cost in links:
#     costlst = pathdata[cost]
#     for a,b in costlst:
#         nodelink[a].append(b)
#         nodelink[b].append(a)
#     for summit in summits:
#         check = bfs(summit)
#         if check == False:
#             continue
#         if answer:
#             if answer[0] < check:
#                 continue
#             else:
#                 answer = [check,cost]
#         else:
#             answer = [check,cost]
#     if answer:
#         return answer