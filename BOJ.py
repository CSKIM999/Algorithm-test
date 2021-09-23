###############################################################################################################
##########################################     Q21608 _ 상어 초등학교     #####################################
###############################################################################################################
'''
Given ) 상어초등학교에 N*N 크기의 교실이 있고 학교에 다니는 학생 수는 N*N 명이다. 학생은 1번부터 N*N번까지 번호가
        매겨져있고, 교실의 가장 
'''
# import heapq

# # n = 3

# # data = [
# #     [4, (2,5,1,7)],
# #     [3, (1,9,4,5)],
# #     [9, (8,1,2,3)],
# #     [8, (1,9,3,4)],
# #     [7, (2,3,4,8)],
# #     [1, (9,2,5,7)],
# #     [6, (5,2,3,4)],
# #     [5, (1,9,2,8)],
# #     [2, (9,3,1,4)]
# # ]
# # data = [
# #     [7, (9, 3, 8, 2)], 
# #     [5, (7, 3, 8, 6)],
# #     [3, (5, 2, 4, 9)],
# #     [9, (6, 8, 3, 4)],
# #     [8, (5, 3, 1, 6)],
# #     [6, (3, 8, 5, 4)],
# #     [2, (6, 4, 8, 7)],
# #     [1, (8, 3, 4, 5)],
# #     [4, (7, 9, 3, 8)]

# # ]


# n = int(input())
# data = []
# for i in range(n*n):
#     delta = (list(map(int,input().split())))
#     data.append([delta[0],tuple(delta[1:5])])

# table = [[0]*n for _ in range(n)]

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# def seat(lst,table):
#     delta = [[0,0,0,0] for _ in range(n*n)]
#     num,like = lst
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if table[i][j] != 0:
#                 delta[count][0] += 1
#                 delta[count][1] += 1
#                 delta[count][2] = i
#                 delta[count][3] = j
#                 count +=1
#                 continue
#             delta[count][2] = i
#             delta[count][3] = j
#             for k in range(4):
#                 x,y = i,j
#                 nx,ny = x+dx[k],y+dy[k]
#                 if 0<=nx<n and 0<=ny<n:
#                     if table[nx][ny] in like:
#                         delta[count][0] -=1
#                     elif table[nx][ny] == 0:
#                         delta[count][1] -=1
                    
#             count +=1
#     return delta

# def satisfaction(table):
#     satis = 0
#     grade = [0,1,10,100,1000]
#     for i in range(n):
#         for j in range(n):
#             num = table[i][j]
#             count = 0
#             for k in range(4):
#                 x,y = i,j
#                 nx,ny = x+dx[k],y+dy[k]
#                 if 0<=nx<n and 0<=ny<n:
#                     if table[nx][ny] in data[num-1][1]:
#                         count += 1
#             satis += grade[count]
#     return satis

# for i in data:
#     a = seat(i,table)
#     heapq.heapify(a)
#     best = heapq.heappop(a)
#     x,y = best[2:4]
#     table[x][y] = i[0]

# data.sort()
# print(satisfaction(table))

'''
1회차 > [[ line 53 to 59 ]]
        if table[i][j] != 0:
                        #  delta[count][0] += 1
                        #  delta[count][1] += 1
                        delta[count][2] = i
                        delta[count][3] = j
                        #  count +=1
                        continue
        
        what ? 
        위 코드가 before & after 코드인데 count 또한 continue 전에 한번 더해주었어야했고 이미 사용된 칸이라면 최소힙 큐를
        사용중인 내 코드의 경우엔 delta 의 0,1 인덱스에 무조건 후순위로 밀릴 수 있는 1을 더해주었어야했음.
        앉을 자리를 탐색하는 함수에서 각 자리를 탐색할 때 인접 칸에 빈칸도 없고 좋아하는 친구도 없을때 를 고려하지 않았음

        why ?
        그렇다면 왜 위의 문제를 필터링하지 못했을까?
        힙큐를 이용해 [인접 좋아하는 학생수 , 인접 빈칸, 행번호, 열번호] 를 통해 seat() 함수가 빠르게 최적의 자리를 찾아주길 원했음
        하지만 힙큐는 최소힙큐에 기반하기때문에 인접칸에 대한 앞의 두 인덱스는 음수, 좌표 번호에 대한 뒤의 두 인덱스는 양수로 넣어서
        착오가 생겼었음. 본래 코드에서 위의 주석 세 줄로 정답판정을 받을 수 있었고 사용된 번호 처리가 조금 부족했던 것 같음  
'''


###############################################################################################################
############################################     Q12100 _ 2048     ############################################
###############################################################################################################
'''
Given ) 2048 게임을 하려고 한다. n*n 의 보드에서 주어진 데이터로 5번 움직일 때 얻을 수 있는 최댓값 블록을 출력하라
        1<= N <= 20
'''
'''
1회차 > 각 방향으로의 이동함수를 작성하고 해당 함수들을 dfs 로 순회시켜서 max 값을 가져오고자 함.
'''

# # n = 3
# # give = [
# #     [2,2,2],
# #     [4,4,4],
# #     [8,8,8]
# # ]
# n = int(input())
# give = []
# for i in range(n):
#     give.append(list(map(int,input().split(' '))))
# count = 0

# def move_right(data):
#     lst = []
#     ck = False
#     for i in range(n):
#         h_count = 1
#         lst = [j for j in data[i] if j >0]
#         m = len(lst)
#         for j in range(1,m+1): #[2,2,2]
#             if j != m:
#                 if ck:
#                     ck = False
#                     continue
#                 if lst[-j] != lst[-j-1]:
#                     data[i][-h_count] = lst[-j]
#                     h_count+=1
#                     continue
#                 elif lst[-j] == lst[-j-1]:
#                     data[i][-h_count] = lst[-j]*2
#                     ck = True
#                     h_count+=1
#             else:
#                 if ck:
#                     ck=False
#                     data[i][-h_count] = 0
#                     continue
#                 else:
#                     data[i][-h_count] = lst[-j]
#         if n!=h_count:
#             while True:
#                 h_count+=1
#                 data[i][-h_count] = 0
#                 if n == h_count:
#                     break
#         lst = []
#     return data


# def move_left(data):
#     lst = []
#     ck = False
#     for i in range(n):
#         h_count = 0
#         lst = [j for j in data[i] if j >0]
#         m = len(lst)
#         for j in range(m): #[2,2,2]
#             if j != m-1:
#                 if ck:
#                     ck = False
#                     continue
#                 if lst[j] != lst[j+1]:
#                     data[i][h_count] = lst[j]
#                     h_count+=1
#                     continue
#                 elif lst[j] == lst[j+1]:
#                     data[i][h_count] = lst[j]*2
#                     ck = True
#                     h_count+=1
#             else:
#                 if ck:
#                     ck=False
#                     data[i][h_count] = 0
#                     continue
#                 else:
#                     data[i][h_count] = lst[j]
#         if n-1!=h_count:
#             while True:
#                 h_count+=1
#                 data[i][h_count] = 0
#                 if n-1 == h_count:
#                     break
#         lst = []
#     return data


# def move_down(data):
#     lst = []
#     ck = False
#     for i in range(n):
#         v_count = 1
#         lst = [ j[i] for j in data[0:n] if j[i] > 0]
#         m = len(lst)
#         for j in range(1,m+1):
#             if j != m:
#                 if ck:
#                     ck = False
#                     continue
#                 if lst[-j] != lst[-j-1]:
#                     data[-v_count][i] = lst[-j]
#                     v_count+=1
#                     continue
#                 elif lst[-j] == lst[-j-1]:
#                     data[-v_count][i] = lst[-j]*2
#                     ck = True
#                     v_count+=1
#             else:
#                 if ck:
#                     ck=False
#                     data[-v_count][i] = 0
#                     continue
#                 else:
#                     data[-v_count][i] = lst[-j]
#         if n!=v_count:
#             while True:
#                 v_count+=1
#                 data[-v_count][i] = 0
#                 if n == v_count:
#                     break
#         lst = []
#     return data

# def move_up(data):
#     lst = []
#     ck = False
#     for i in range(n):
#         v_count = 0
#         lst = [ j[i] for j in data[0:n] if j[i] > 0]
#         m = len(lst)
#         for j in range(m):
#             if j != m-1:
#                 if ck:
#                     ck = False
#                     continue
#                 if lst[j] != lst[j+1]:
#                     data[v_count][i] = lst[j]
#                     v_count+=1
#                     continue
#                 elif lst[j] == lst[j+1]:
#                     data[v_count][i] = lst[j]*2
#                     ck = True
#                     v_count+=1
#             else:
#                 if ck:
#                     ck=False
#                     data[v_count][i] = 0
#                     continue
#                 else:
#                     data[v_count][i] = lst[j]
#         if n-1!=v_count:
#             while True:
#                 v_count+=1
#                 data[v_count][i] = 0
#                 if n-1 == v_count:
#                     break
#         lst = []
#     return data

# ans = 0
# def dfs(data,count):
#     global ans
#     if count >= 5:
#         for i in range(n):
#             for j in range(n):
#                 ans = max(ans,data[i][j])
#         return
#     dfs(move_right([i[:] for i in data]),count +1)
#     dfs(move_left([i[:] for i in data]),count +1)
#     dfs(move_down([i[:] for i in data]),count +1)
#     dfs(move_up([i[:] for i in data]),count +1)

# #########################################################


# # time = 5
# # def test(data,count):
# #     for i in range(4):
# #         data,count = data,count
# #         if i ==0:
# #             if count >= time:
# #                 break
# #             count +=1
# #             move_right(data,count)
# #             print(data)
# #             test(data,count)
# #         elif i == 1:
# #             if count >= time:
# #                 break
# #             count += 1
# #             move_left(data,count)
# #             print(data)
# #             test(data,count)
# #         elif i == 2:
# #             if count >= time:
# #                 break
# #             count += 1
# #             move_up(data,count)
# #             print(data)
# #             test(data,count)
# #         elif i == 3:
# #             if count >= time:
# #                 break
# #             count += 1
# #             move_down(data,count)
# #             print(data)
# #             test(data,count)
# # test(give,count)

# dfs(give,count)
# print(ans)


'''
1회차 > 5번째 카운트일때만 해당 데이터를 순회하여 최댓값을 탐색하는 방향으로 선회했다.
        그것보다도 dfs알고리즘에서 재귀함수를 사용하고싶은데 어떻게 해야하나 많이 고민했다. 하지만 나는 이미 
        move 함수를 만들어놓아서 이것을 사용하는 재귀함수로서 for 문을 이용하여 각 i 값마다 상하좌우 움직임 함수를
        호출하고자 했으나, 이와같은 방법은 전역변수 data 에 영향을 주므로 문제가 생겼던 것 같다. <<< 이부분은 아직 제대로 이해하지 못함
        아무튼 다시 지금 확인해보니 
        line 315 ) move_right(data,count)
        line 316 ) print(data)
        line 317 ) test(data,count)
        위의 내용을
        test(move_right(data,count),count+1) 이런식으로 구성했으면 아마도 성공하지않았을까 싶다.
        물론 지금 완성시킨 dfs 안에 4개의 dfs 안에 지역변수 move함수데이터를 주는 방법이 더욱 깔끔할 듯 하다.
'''


###############################################################################################################
#########################################     Q13458 _ 시험 감독     ##########################################
###############################################################################################################


# result = 0

# n = int(input())
# give = list(map(int,input().split()))
# b,c = map(int,input().split())

# for i in give:
#     if i<=b:
#         result +=1
#         continue
#     if (i-b)%c != 0:
#         result += ((i-b)//c )+2
#     else:
#         result += ((i-b)//c )+1

# print(result)

'''
1회차 > 상당히 쉬워보이길래 그자리에서 가볍게 코딩해보았다. 하지만 i<=b 의 경우를 생각하지 않아 오답판정을 받았다. 
        이와같이 정확한 필터링을 해내는 연습을 해봐야겠다.
'''


###############################################################################################################
#######################################     Q14499 _ 주사위 굴리기     ########################################
###############################################################################################################

'''
Given ) N*M 크기의 지도 위에 주사위가 놓여진다. 가장 처음 주사위는 모든 면이 0 이 적혀있다.
        만약 지도와 맞닿는 주사위의 면이 0 이라면 지도에 적혀있는 숫자가 주사위로 복사되며 지도에는 0이 적힌다.
        반대로 주사위와 맞닿은 지도의 숫자가 0 이라면 주사위의 숫자가 지도에 복사되며 주사위의 해당 면의 숫자가 0이 된다.
        주사위를 굴리는 이동명령이 주어질 때 주사위 상단에 쓰여있는 값을 출력하는 프로그램을 작성하라.
        만약 주사위를 지도 밖으로 이동시키려는 명령은 무시하고 출력도 하지 않아야한다.
Input ) 첫째 줄에 N과 M 이 주어지고 ( 1<= N,M <=20 ) 주사위를 놓는 좌표 x,y 그리고 명령의 개수 K 가 주어진다(1<= K <= 1,000)
        둘째 줄부터 N 개의 줄에 지도 데이터가 주어지며 각 칸은 10 미만의 자연수 혹은 0 이 주어진다.
        마지막 줄에는 이동명령이 순서대로 주어진다. 동쪽은 1 서쪽은 2 북쪽은 3 남쪽은 4 로 주어진다.
Output) 매 이동마다 주사위의 윗면에 쓰인 수를 출력한다. 만약 지도밖으로 나가려한다면 해당 명령을 무시하며 출력또한 하지 않는다.
'''

# tb = [1,6]
# side = [3,4,2,5]
'''
1회차 > 주사위를 구현하는것이 어려웠다. 문제를 풀기 전에 주사위 구현방법을 먼저 생각했는데 현재 생각한 방법은 위 아래면과 옆면을 나누는
        방식이다. 이 외에는 지도를 이동하는것은 어렵지 않으니 구현해보려 한다.
'''
# # x,y = 0,0
# # n,m = 4,2
# # data = [
# #     [0,2],
# #     [3,4],
# #     [5,6],
# #     [7,8]
# # ]
# # order = [4,4,4,1,3,3,3,2] #동 북 서 서 남 남 동 동 북

# n,m,x,y,i = map(int,input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int,input().split())))
# order = list(map(int,input().split()))

# dx = [0,0,0,-1,1]
# dy = [0,1,-1,0,0]
# dice_tb = [0,0]
# dice_side=[0,0,0,0]

# def roll(orde,x,y):
#     if orde == 2: #서
#         t,b,r,l = dice_tb[0],dice_tb[1],dice_side[0],dice_side[1]
#         dice_tb[0],dice_tb[1] = r,l
#         dice_side[0],dice_side[1] = b,t
#     elif orde == 1: #동
#         t,b,r,l = dice_tb[0],dice_tb[1],dice_side[0],dice_side[1]
#         dice_tb[0],dice_tb[1] = l,r
#         dice_side[0],dice_side[1] = t,b
#     elif orde == 3: #북
#         t,b,s,n = dice_tb[0],dice_tb[1],dice_side[3],dice_side[2]
#         dice_tb[0],dice_tb[1] = s,n
#         dice_side[3],dice_side[2] = b,t
#     else: #남
#         t,b,s,n = dice_tb[0],dice_tb[1],dice_side[3],dice_side[2]
#         dice_tb[0],dice_tb[1] = n,s
#         dice_side[3],dice_side[2] = t,b


#     if data[x][y] != 0:
#         dice_tb[1],data[x][y] = data[x][y],0
#     elif data[x][y] == 0:
#         data[x][y]= dice_tb[1]
#     print(dice_tb[0])

# for i in order:
#     nx,ny = x+dx[i],y+dy[i]
#     if 0<=nx<n and 0<=ny<m:
#         x,y = nx,ny
#         roll(i,x,y)
    
    
'''
1회차 > 참 지저분했던 문제. 출력부도 상당히 지저분하고 입력도 상당히 지저분함
        주사위 모델링이 계속 헷갈리고 제일 먼저 문제를 잘못읽어서 시간이 너무너무 많이 걸림 여러모로 징그러운 문제
        주사위모델링과 움직이는방법 자체에 대한 추론은 맞았다. 하지만 간결하지 않아 제대로 구현하지못한 듯
'''



###############################################################################################################
#######################################     Q14889 _ 스타트와 링크     ########################################
###############################################################################################################
'''
Given ) 축구를 하기 위해 N 명의 사람을 나누어 팀을 짜려한다. 사람들에게 번호를 매겨 1부터 N 까지 배정하고 각 사람마다 능력치를 조사했다.
        S_ij 는 i번사람과 j번 사람이 같은 팀에 속할 때 팀에 더해지는 능력치로 S_ij 와 S_ji 는 다를 수 있다.
        만약 같은 팀에 속한다면 더해지는 능력치는 S_ij와 S_ji 이다. ( 둘 다 )
        모든 경우의 수를 따져 두 팀의 능력치차이가 최소가 되는 값을 출력하라.
Input ) 첫째 줄에 N( 4<= N <= 20 __항상짝수__ ) 가 주어지고 둘째 줄부터 N개의 줄에 S 가 주어진다. 각 줄은 N 개의 수로 이루어져있고,
        i번 줄의 j 번째 수가 S_ij 가 된다. S_ii 는 항상 0 이고 나머지 S_ij 는 1 이상 100 이하의 정수이다.
Output) 두 팀의 능력치 차이 최솟값을 출력하라
'''

'''
1회차 > 팀원이 절반으로 나누어져야한다. 즉 depth 가 절반이 되었을 때의 현재 home 팀 능력치를 계산하고 home 팀에 들어가지 못한 나머지 수의
        능력치를 계산하면 away 팀의 능력치가 계산된다. 능력치 테이블에서 값을 가져오는것이므로 away 팀의 능력치 계산은 그닥 오래걸리지 않을것
'''
# # n = 6
# # data = [
# #     [0,1,2,3,4,5],
# #     [1,0,2,3,4,5],
# #     [1,2,0,3,4,5],
# #     [1,2,3,0,4,5],
# #     [1,2,3,4,0,5],
# #     [1,2,3,4,5,0]
# # ]

# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))

# half = int(n/2)
# lst = []
# ans = 1e9

# def dfs(curr,last=-1):
#     global ans
#     if len(curr) >= half:
#         home = 0
#         away = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 elif i in curr and j in curr:
#                     home += data[i][j]
#                 elif i not in curr and j not in curr:
#                     away += data[i][j]
#         temp = abs(home-away)
#         if ans>temp:
#             ans = min(ans,temp)
#         return

#     for i in range(last+1,n):
#         if i not in curr and len(curr)<half:
#             last = i
#             curr.append(i)
#             dfs(curr[:],last)
#             curr.pop()
#             if len(curr) == 0:
#                 last = -1
#             else:
#                 last = curr[(len(curr)-1)]

# dfs(lst)
# print(ans)
'''
1회차 > Pyhton 3 로는 시간초과판정을 받아서 Pypy 로 정답판정을 받았다.
        나는 combination 을 사용하지 않고 그냥 모든 경우의수를 모두 순회했다. [0,1,2,3] 과 [3,2,1,0] 이 다르단것을 알고있어서
        last 값을 넣어주고 현재 가장 마지막에 들어간 수 보다 무조건 큰 수가 다음에 들어가도록 코딩했다.그정도라면 아마 충분히 통과할 줄 알았으나
        결과는 그렇지 않았던 듯 하다. 다른사람들의 제출결과를 확인해보니 대다수가 combination 라이브러리를 사용했다.
        기본으로 제공되는 라이브러리를 잘 사용하는것도 실력이다. dfs 는 잘 사용했지만 지금 돌아보면 combination 을 사용하기에 아주 적합한 문제였음에도
        생각해내지 못한 점이 문제라고 할 수 있지 싶다.
'''
'''
import sys
from itertools import combinations

N = int(sys.stdin.readline())
list_N = list(range(N))
data_list = [list(map(int, sys.stdin.readline().split())) for __ in range(N)]

sum_list = [sum(i) + sum(j) for i, j in zip(data_list, zip(*data_list))]
answer = min([abs(sum(sum_list) // 2 - sum(team)) for team in combinations(sum_list, N // 2)])

print(answer)

204 ms 가 걸린 다른사람의 코드. line 555 의 zip(*data) 까지는 이해했으나 그 이후로는 이해 못함. 나중에 내공이 쌓이면 다시 이 코드를 이해해보자
'''




###############################################################################################################
#########################################     Q14891 _ 톱니바퀴     ###########################################
###############################################################################################################
'''
Given ) 특수한 룰에 의해서 톱니바퀴는 회전할 때 9시와 3시에 맞닿은 톱니바퀴를 회전시킨다.
        특수한 룰은 다음과 같다. 만약 회전시키려는 톱니바퀴와 맞닿은 톱니바퀴의 극이 서로 다르다면 맞닿은 톱니바퀴는
        반대방향으로 회전한다. 이 룰은 9시와 3시 양쪽에 모두 적용되며, 또한 전파된다.
        즉, 같은 극으로 맞닿아있는 톱니바퀴를 만날 때 까지 톱니바퀴의 회전영역이 된다.
        초기 톱니바퀴상태와 톱니바퀴를 회전시키는 순서가 주어질 때 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하라
Input ) 첫째 ~ 넷째 줄에 걸쳐 1 ~ 4 번 톱니바퀴의 상태가 주어진다.
        상태는 8개의 정수로 이루어져있고, 12시 방향부터 시계방향 순서로 주어진다. N 극은 0, S 극은 1로 나타낸다.
        다섯째 줄에는 회전 횟수 K (1 <= K <= 100 )이 주어지고 다음 K개의 줄에는 회전 방법이 순서대로 주어진다.
        각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시키는 톱니바퀴의 번호,
        두 번째 정수는 회전시키는 방향으로 1은 시계방향, -1 은 반시계방향을 나타낸다.
Output) 총 K 번 회전시킨 후, 네 톱니바퀴의 점수의 합을 출력하라. 점수 계산방법은 다음과 같다.
        12시 방향의 극으로 점수를 계산하며 N 극이라면 0 점 S 극이라면 1,2,4,8 점을 부여한다.
'''

