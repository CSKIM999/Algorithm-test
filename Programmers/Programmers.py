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
# from collections import deque
# data = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     answer = -1
#     visited = [[0]*m for _ in range(n)]
#     visited[0][0] = 1
#     queue = deque([[0,0,1]])
#     rot = [[1,0],[-1,0],[0,1],[0,-1]]
#     if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
#         return -1
#     while queue:
#         x,y,count = queue.popleft()
#         for a,b in rot:
#             nx,ny = x+a,y+b
#             if 0<=nx<n and 0<=ny<m:
#                 if maps[nx][ny] == 1 and visited[nx][ny] ==0:
#                     queue.append([nx,ny,count+1])
#                     visited[nx][ny] = 1
#                 if nx == n-1 and ny==m-1:
#                     answer = count+1
#                     break


#     return answer

# print(solution(data))

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



################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'>>> 오픈채팅방 <<<'
'''
Approach >> 회원의 데이터는 유저아이디로 처리되며, 만약 아이디가 바뀔경우 전에 입력된 데이터들도 모두 바뀐다
            따라서 딕셔너리와 큐를 사용하여 큐에 사용자별 입/퇴장 데이터를, 딕셔너리에 사용자 이름데이터를 이용하여
            마지막에 하나의 스트링으로 묶어보고자 한다.
'''

# from collections import deque

# dic = {}
# result = []
# queue = deque()
# state_input = {'Enter':0,'Leave':1,'Change':2}
# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# for i in record:
#     data = i.split()
#     try:
#         if state_input[data[0]] == 0:
#             dic[data[1]] = data[2]
#             queue.append([0,data[1]])
#         elif state_input[data[0]] == 1:
#             queue.append([1,data[1]])
#         elif state_input[data[0]] == 2:
#             dic[data[1]] = data[2]
#     except KeyError:
#         print('error')
    
# print(queue)
# print(dic)
# while queue:
#     s,u = queue.popleft()
#     if s == 0:
#         result.append(f"{dic[u]}님이 들어왔습니다.")
#     elif s == 1:
#         result.append(f"{dic[u]}님이 나갔습니다.")

# print(result)


'''
1회차 >> 바로정답 존나게 쉽다
'''

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
' >>> 멀쩡한 사각형 <<< '
# a=[8,12]
# total = a[0]*a[1]
# a,b = min(a),max(a)
# # a = 77783/77797


# # print(a)
# from math import ceil,floor
# c = 1/(a/b)
# # print((c*7))
# i=0
# result = 0
# while True:
#     i+=1
#     up = ceil(c*i)
#     low = floor((up)-c)
#     result += up-low
#     if (c*i)%1 == 0:
#         alp = a/i
#         result = result*alp

#         break
# print(result)

# def gcd(a,b):
#     return b if a%b == 0 else gcd(b,a%b)

# print(gcd(7,11))

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
# ' >>> 기능 개발 <<< '
# from math  import ceil
# data = [93, 30, 55]
# sp = [1, 30, 5]
# result = []
# ans = []
# for i in range(len(data)):
#     result.append(ceil((100 - data[i])/sp[i]))
# temp = result[0]
# j = 1
# print(result)
# for i in range(1,len(result)):
#     if temp<result[i]: #i 보다 i+1 이 더 오래걸릴 때
#         ans.append(j)
#         temp = result[i]
#         j = 0
#     j+=1
# ans.append(j)
# print(ans)



################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'''
>>> LV 3 거스름돈 <<< 
>>> DP 를 통해서 n 을 구하는 요소를 찾아보고자 한다
    DP 의 사용 플로우는 다음과 같을 예정이다
        >>> A ) DP생성 1부터 n-money[0] 까지
            현재 구성중인 DP now
            >>> B ) money 를 역순으로 순회한다. i
                i == now 라면 DP[now].append((i)) #set구조임을 주의
                    continue
                i < now 라면 now = now - i
                    for i in DP[now]:
                        if len(DP[i]) == 0:
                            continue     

'''

# n = 5
# money = [2,1,5]
# money.sort()

# dp = [set() for _ in range(n-money[0]+1)]

# #타겟넘버까지 dp 테이블을 만들고 해당 테이블을 통해 타겟넘버를 만들자
# # 
# print(dp)
# for now in range(1,n-money[0]+1): # DP 순환
#     for j in range(1,len(money)+1):
#         tmp = now
#         now_money = money[-j]
#         if now_money == now:
#             dp[now].add(now_money)
#             continue
#         if tmp > now_money:
#             tmp -= now_money
#             # for k in list(dp[tmp]):
#             for k in dp[tmp]:
#                 if type(k) == int:
#                     t = [k]
#                 else:
#                     t = list(k)
#                 t.append(now_money)
#                 dp[now].add(tuple(sorted(t,key=lambda x:x)))


# # t = (2,3,2)
# # a.add(tuple(sorted(t,key=lambda x:x)))

# # b = (2,3)
# # tmp = list(b)
# # tmp.append(2)
# # tmp.sort(reverse=True)
# # print(tuple(tmp))
# # print(a)
# print(dp)
# print()
# result = set()
# for i in reversed(money):
#     temp = n
#     if i == temp:
#         result.add(i)
#         continue
#     if temp > i:
#         temp -= i
#         for j in dp[temp]:
#             if type(j) == int:
#                 t = [j]
#             else:
#                 t = list(j)
#             t.append(i)
#             result.add(tuple(sorted(t,key=lambda x:x)))
            

# answer = len(result)%1000000007
# print(answer)

# def solution(n, money):
#     money.sort()
#     dp = [set() for _ in range(n-money[0]+1)]
#     for now in range(1,n-money[0]+1): # DP 순환
#         for j in range(1,len(money)+1):
#             tmp = now
#             now_money = money[-j]
#             if now_money == now:
#                 dp[now].add(now_money)
#                 continue
#             if tmp > now_money:
#                 tmp -= now_money
#                 # for k in list(dp[tmp]):
#                 for k in dp[tmp]:
#                     if type(k) == int:
#                         t = [k]
#                     else:
#                         t = list(k)
#                     t.append(now_money)
#                     dp[now].add(tuple(sorted(t,key=lambda x:x)))
#     result = set()
#     for i in reversed(money):
#         temp = n
#         if i == temp:
#             result.add(i)
#             continue
#         if temp > i:
#             temp -= i
#             for j in dp[temp]:
#                 if type(j) == int:
#                     t = [j]
#                 else:
#                     t = list(j)
#                 t.append(i)
#                 result.add(tuple(sorted(t,key=lambda x:x)))


#     answer = len(result)%1000000007
#     return answer



# '''
# 1회차 > 정확도 테스트는 모두 통과했다. 하지만 효율성테스트는 모두 시간초과로 실패했다.
# '''




################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'''
>>> LV 2 더 맵게 <<< 

가장 낮은 스코빌 지수음식 2개를 찾아야하므로 최소힙을 사용하면 좋을듯

'''

# import heapq
# K = 11
# lst = [1,2,3]
# result = 0
# while True:
#     if len(lst) <2:
#         if lst[0] > K:
#             break
#         result = -1
#         break
#     alpha = heapq.heappop(lst)
#     if alpha<K:
#         beta = heapq.heappop(lst)
#         gamma = alpha+(beta*2)
#         heapq.heappush(lst,gamma)
#         result+=1
#     else:
#         break

# print(result)

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'''
>>> LV 2 짝지어 제거하기 <<< 

디큐 사용하면 빠를거같은디
'''

# from collections import deque

# s = 'abbbaa'
# s = list(s)
# s = deque(s)
# before = s.popleft() #큐 빼기 A
# temp = deque()
# while True:
#     flag = True
#     while True:
#         try:
#             now = s.popleft() #큐 빼기 B
#         except:
#             flag = True
#             break
#         if before == now: # AB 비교 같다면?
#             flag = False
#             if (len(s)>0 and len(temp)>0) and temp[-1] == s[0]: #만약 
#                 while True:
#                     if (len(s)>0 and len(temp)>0) and temp[-1] == s[0]:
#                         temp.pop()
#                         s.popleft()
#                     else:
#                         break
#             if len(s)==0:
#                 try:
#                     s.append(temp.pop())
#                 except:
#                     break
#                 break
#             before = s.popleft() #새로운 before 값이 필요하므로 큐빼놓기
            
#         else:
#             if len(s)==0:
#                 s.append(now)
#                 break
#             temp.append(before)
#             before = now
#     if flag:
#         result = 0
#         break
#     elif len(s) == 0:
#         result = 1
#         break

# print(result)

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'''
>>> LV 3 가장 먼 노드 <<< 

방문처리하고 bfs 쓰면 충분할듯?
'''

# n = 6
# from collections import deque
# data = [[] for _ in range(n+1)]
# hist = [1e9 for _ in range(n+1)] 
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
# for a,b in edge:
#     data[a].append(b)
#     data[b].append(a)
# q = deque([1])
# hist[0],hist[1] = 0,0
# count = 0
# while True:
#     now = q.popleft()
#     dist = hist[now]
#     for i in data[now]:
#         if hist[i] > dist+1:
#             hist[i] = dist+1
#             q.append(i)
#     count+=1
#     # print(q)
#     if not q:
#         break
#     elif count == 100:
#         break
# print(hist.count(max(hist)))
# print(hist)


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################'''
'''
>>> LV 3 추석 트래픽 <<< 

각 배열원소에서 날짜를 뺀 시간단위를 초로 바꾸자
이미 정렬되어있는 데이터이므로, 따로 정렬의 필요는 없다.
s 로 바꾼 데이터에서 각 원소를 순회하며 최소단위인 0.001s 를 뺀 값부터 1초 뒤 까지 순회하며 카운트를 해보는것 아무리 많아봐야 1초사이에는 아무리 많아봐야 1000개이므로
시간이 오래걸릴일은 없을것. 2초 사이에 1999개의 배열이 위치하더라도 최대 연산횟수는 1,999,000회로 아주 미미한수준
각 원소의 시작과 끝이 1초 안에 들어간다면 최대처리량 카운트에 추가
'''

# lines =  [
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# # "2016-09-15 01:00:04.002 2.0s",
# # "2016-09-15 01:00:07.000 2s"
# ]
# Id = len(lines)
# data = []
# for i in lines: #주어진 값 sec 로 환산
#     d,t,st = i.split()
#     h,m,s = map(float,t.split(':'))
#     t = h*3600+m*60+s
#     st = float(st[:-1])-0.001
#     data.append([round(t-st,3),t])
# data.sort()
# result = 0
# for i in range(Id):
#     temp = set()
#     start = data[i][1]
#     end = round(data[i][1] + 0.999,3)
#     for j in range(Id):
#         if data[j][0]>end:
#             break
#         if data[j][1]<start:
#             continue
#         temp.add(j)
#     result = max(result,len(temp))

# print(result)

'''
line 507 의 sort 를 빼고 하니 두가지 케이스에서 오답을 받았다.
이유는 검사하고자 하는 start-end 범위를 모두 감싸는 경우가 line514 로 인해 break 된 이후, 다시 조건에 부합하는 데이터가 위치하는듯했다.
sort 를 이용한 이유는 line 의 크기가 2000을 넘지 않아 sort 를 사용하더라도 무시 가능한 수준일것이고, 처리의 순서는 중요하지 않았기에 sort를 통해
순서를 바꾸어도 초당 최대처리량을 구하는데는 문제가 없었기 때문이다.
'''


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
'''
>>> LV 3 입국심사<<< 
-- 구분 : 이분탐색 --

대부분의 문제는 사실상 하나의 방정식이다. 이 문제의 경우 입국자수가 상수이고 소요시간이 우리가 구하고자 하는 계산값이다.
입국자 수가 정해져있고, 바뀌는것은 각 심사관이 시간내에 심사하는 인원수이다.
총 소요시간 / 심사관의 속도 = 해당 심사관이 받을 수 있는 최대 입국자수 이다. 따라서 시간을 1부터 최악의 경우의수 까지 배열한 후
중간값(1+최악의시간 / 2) 에서 각 심사관의 최대처리수를 모두 더한 값이 중간값에서의 입국자 수가 되는것이다.
그 중간값 입국자수로 또다시 최대, 최소값을 구하면 된다.

'''


times = [5,7,13]
n = 8
mt = 0
result = 1e18
start, end = 1,max(times)*n
while start!=end:
    mt = 0
    mid = (start+end)//2

    for i in times:
        mt += mid//i
    
    if mt > n:
        end = mid-1
    elif mt < n:
        start = mid+1
    else:
        result = min(result,mid)
        end-=1

print(result)