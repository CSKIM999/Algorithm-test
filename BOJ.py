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
'''
1회차 > 톱니바퀴의 갯수가 4개뿐이므로 매 번 현재 톱니상태에서 움직여야하는 하나의 집합을 찾아내고 각각 회전방향을 부여하면 될 듯 하다.
'''
# # data = [[1,0,1,0,1,1,1,1],[0,1,1,1,1,1,0,1],[1,1,0,0,1,1,1,0],[0,0,0,0,0,0,1,0]]
# # moves = [[3,-1],[1,1]]

# data = []
# moves = []
# for i in range(4):
#     data.append(list(map(int,input())))
# n = int(input())
# for i in range(n):
#     moves.append(map(int,input().split()))

# def roll(rotate,data):
#     if rotate == 1:
#         data[0],data[1:] = data[-1],data[:-1]
#     elif rotate == -1:
#         data[-1],data[:-1] = data[0],data[1:]
#     return data

# group = [[i,0] for i in range(4)]
# reset = [i[:] for i in group]

# def check(g_node,rot):
#     global group
#     group[g_node][1] = rot
#     if g_node-1 >= 0 and group[g_node-1][1] == 0 and data[g_node-1][2] != data[g_node][6]:
#         group[g_node-1][1] = -rot
#         check(g_node-1,-rot)
#     if g_node+1 <= 3 and group[g_node+1][1] == 0 and data[g_node+1][6] != data[g_node][2]:
#         group[g_node+1][1] = -rot
#         check(g_node+1,-rot)

# for node,rotate in moves:
#     node = node-1
#     check(node,rotate)
#     for n_node,n_rot in group:
#         if n_rot != 0:
#             data[n_node] = roll(n_rot,data[n_node])
#     group = [i[:] for i in reset]
# result = 0
# for i in range(4):
#     if data[i][0] == 1:
#         result += 2**i
# print(result)

'''
1회차 > roll 함수와 현재 움직여야 할 group 을 생성해서 check 함수로 group 을 갱신해주고 각각 움직여주었다.
        인덱스값이 조금 헷갈리지만 쉽게 정답판정을 받았다.
'''





###############################################################################################################################################################################################
################################################################################     Q13460 _ 구슬 탈출 2    ##################################################################################
###############################################################################################################################################################################################
'''
Given ) N*M 크기의 보드가 1x1 칸으로 나누어져 가장 바깥 행과 열은 벽으로 막혀있다. 보드에는 구멍이 하나 있고 임의의 공간에 빨간 구슬과 파란 구슬이 각각 들어가있다.
        게임의 목표는 파란 구슬이 구멍으로 들어가기 전에 빨간 구슬을 꺼내는 것이다. 구슬은 중력을 이용하여 이리 저리 굴린다.
        각각의 동작에서 공은 동시에 움직이며 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 구슬은 각각 한칸을 차지하여 동시에 같은 칸에 있을 수없다.
        기울이는 동작을 그만하는것은 더이상 구슬이 움직이지 않을 때 까지이다. 최소 몇번 움직여서 구슬을 뺄 수 있는지 프로그램을 작성하라.
Input ) 첫째 줄에는 가로 세로 N과 M 이 주어진다.
        그 이후 N개의 줄에 걸쳐 M 개의 문자열이 주어진다. '.','#','O','R','B' 에서 . 은 빈칸을 의미하고, #은 벽, O 는 구멍, R 은 빨간 구슬 B 는 파란 구슬을 의미한다.
Output) 최소 몇번만에 빨간 구슬을 구멍을 통해 빼낼 수 있는 지 출력하라. 만약 10번을 초과한다면 -1 을 출력하라.
'''
'''
1회차 > 입력되는 값의 제한이 따로 주어지지 않았다. 우선 움직임 함수를 구현하고 dfs 를 통해 count 값이 10을 넘어가면 실행하지 않도록 해봐야겠다.
'''

# # n,m = 10,10
# # data = [
# #     '##########',
# #     '#R#...##B#',
# #     '#...#.##.#',
# #     '#####.##.#',
# #     '#......#.#',
# #     '#.######.#',
# #     '#.#....#.#',
# #     '#.#.##...#',
# #     '#O..#....#',
# #     '##########'
# # ]
# n,m = map(int,input().split())
# # table =[[] for _ in range(n)]
# # data = []
# dic = {'#':9,'.':0,'O':-1,'R':1,'B':2}
# table = [list(map(lambda x : dic[x],[i for i in input()])) for _ in range(n)]

# # for i in range(n):
# #     for j in range(m):
# #         table[i].append(dic[data[i][j]])
# result = 11
# count = 0
# def h_move_red(give,red,side,c):
#     global result
#     if side == -1:
#         for i in range(red[1],0,-1):
#             if give[red[0]][i-1] != 0:
#                 if give[red[0]][i-1] == -1:
#                     give[red[0]][red[1]] = 0
#                     red[1] = i
#                     result = min(result,c)
#                     return give
#                 give[red[0]][red[1]] = 0
#                 red[1] = i
#                 give[red[0]][red[1]] = 1
#                 break
#     else:
#         for i in range(red[1],m):
#             if give[red[0]][i+1] != 0:
#                 if give[red[0]][i+1] == -1:
#                     result = min(result,c)
#                     give[red[0]][red[1]] = 0
#                     red[1] = i
#                     return give
#                 give[red[0]][red[1]] = 0
#                 red[1] = i
#                 give[red[0]][red[1]] = 1
#                 break
#     return give

# def h_move_blue(give,blue,side,flag):
#     global result
#     if side == -1:
#         for i in range(blue[1],0,-1):
#             if give[blue[0]][i-1] != 0:
#                 if give[blue[0]][i-1] == -1:
#                     flag = False
#                     return give,flag
#                 give[blue[0]][blue[1]] = 0
#                 blue[1] = i
#                 give[blue[0]][blue[1]] = 2
#                 break
#     else:
#         for i in range(blue[1],m):
#             if give[blue[0]][i+1] != 0:
#                 if give[blue[0]][i+1] == -1:
#                     flag = False
#                     return give,flag
#                 give[blue[0]][blue[1]] = 0
#                 blue[1] = i
#                 give[blue[0]][blue[1]] = 2
#                 break
#     return give,flag


# def roll_h(give,side,c):
#     global result

#     rnb = [[],[],[]]
#     for i in range(n):
#         for j in range(m):
#             if 1<= give[i][j] <= 2:
#                 rnb[give[i][j]] = [i,j]
#     red,blue = rnb[1],rnb[2]
    
#     flag = True
#     if side == -1:
#         if red[0] == blue[0]:
#             if red[1]<blue[1]:
#                 temp = h_move_red(give,red,side,c)
#                 temp,flag = h_move_blue(temp,blue,side,flag)
#                 if flag:
#                     give = temp
#                     return give
#                 else:
#                     result = 11
#                     return give
#         temp,flag = h_move_blue(give,blue,side,flag)
#         temp = h_move_red(temp,red,side,c)
#         # for i in range(blue[1],0,-1):
#         #     if give[blue[0]][i-1] != 0:
#         #         if give[blue[0]][i-1] == -1:
#         #             return give
#         #         give[blue[0]][blue[1]] = 0
#         #         blue[1] = i
#         #         give[blue[0]][blue[1]] = 2
#         #         break
#         # for i in range(red[1],0,-1):
#         #     if give[red[0]][i-1] != 0:
#         #         if give[red[0]][i-1] == -1:
#         #             result = min(result,c)
#         #             return give
#         #         give[red[0]][red[1]] = 0
#         #         red[1] = i
#         #         give[red[0]][red[1]] = 1
#         #         break
#     else:
#         if red[0] == blue[0]:
#             if red[1]>blue[1]:
#                 temp = h_move_red(give,red,side,c)
#                 temp,flag = h_move_blue(temp,blue,side,flag)
#                 if flag:
#                     give = temp
#                 else:
#                     result = 11
#                     return give

#         temp,flag = h_move_blue(give,blue,side,flag)
#         temp = h_move_red(temp,red,side,c)
#         # for i in range(blue[1],m):
#         #     if give[blue[0]][i+1] != 0:
#         #         if give[blue[0]][i+1] == -1:
#         #             return give
#         #         give[blue[0]][blue[1]] = 0
#         #         blue[1] = i
#         #         give[blue[0]][blue[1]] = 2
#         #         break
#         # for i in range(red[1],m):
#         #     if give[red[0]][i+1] != 0:
#         #         if give[red[0]][i+1] == -1:
#         #             result = min(result,c)
#         #             return give
#         #         give[red[0]][red[1]] = 0
#         #         red[1] = i
#         #         give[red[0]][red[1]] = 1
#         #         break
#     if flag:
#         give = temp
#         return give
#     else:
#         result = 11
#         return give

# def roll_v(give,side,c):
#     global result

#     rnb = [[],[],[]]
#     for i in range(n):
#         for j in range(m):
#             if 1<= give[i][j] <= 2:
#                 rnb[give[i][j]] = [i,j]
#     red,blue = rnb[1],rnb[2]
#     flag = [False,False]
#     if side == -1:
#         for i in range(blue[0],0,-1):
#             if give[i-1][blue[1]] != 0:
#                 if give[i-1][blue[1]] == -1:
#                     flag[1] = True
#                     break
#                 give[blue[0]][blue[1]] = 0
#                 blue[0] = i
#                 give[blue[0]][blue[1]] = 2
#                 break
#         for i in range(red[0],0,-1):
#             if give[i-1][red[1]] != 0:
#                 if give[i-1][red[1]] == -1:
#                     result = min(result,c)
#                     return give
#                 give[red[0]][red[1]] = 0
#                 red[0] = i
#                 give[red[0]][red[1]] = 1
#                 break
#     else:
#         for i in range(blue[0],m):
#             if give[i+1][blue[1]] != 0:
#                 if give[i+1][blue[1]] == -1:
#                     return give
#                 give[blue[0]][blue[1]] = 0
#                 blue[0] = i
#                 give[blue[0]][blue[1]] = 2
#                 break
#         for i in range(red[0],m):
#             if give[i+1][red[1]] != 0:
#                 if give[i+1][red[1]] == -1:
#                     result = min(result,c)
#                     return give
#                 give[red[0]][red[1]] = 0
#                 red[0] = i
#                 give[red[0]][red[1]] = 1
#                 break

#     return give



# # for i in table:
# #     print(i)
# # print()
# # table = roll_v(table,1,count+1)
# # for i in table:
# #     print(i)

# def roll(g,count):
#     global result
#     if count >= result:
#         return
#     if g != roll_h([i[:] for i in g],1,count+1):
#         roll(roll_h([i[:] for i in g],1,count+1),count+1)
#     if g != roll_h([i[:] for i in g],-1,count+1):
#         roll(roll_h([i[:] for i in g],-1,count+1),count+1)
#     if g != roll_v([i[:] for i in g],1,count+1):
#         roll(roll_v([i[:] for i in g],1,count+1),count+1)
#     if g != roll_v([i[:] for i in g],-1,count+1):
#         roll(roll_v([i[:] for i in g],-1,count+1),count+1)

# roll(table,count)
# print(result)

'''
1회차 > 간단한 구현은 끝냈으나, 한개의 반례가 걸려서 모두 뒤엎게 됨. 다음에 다시풀어봐야할 것 같음
'''

###############################################################################################################################################################################################
#################################################################################     Q14500 _ 테트로미노    ##################################################################################
###############################################################################################################################################################################################
'''
Given ) 정사각형을 4 개 이어붙인 테트로미노 5가지 모양을 이용하여 종이 위에 테트로미노를 놓았을 때 각 칸의 합의 최대를 구하는 프로그램을 작성하라
Input ) 첫째 줄에 세로크기 N 과 가로크기 M 이 주어진다 ( 4<= M,N <= 500 )
        둘째 줄부터 N 개의 줄에 종이 데이터가 주어진다.
Output) 칸이 가리는 최댓값을 출력하라
'''
# c,r = map(int,input().split())
# result = -1
# # data = [[i+(c*j) for i in range(1,1+c)] for j in range(r)]
# data = [list(map(int,input().split())) for _ in range(c)]
# # for i in data:
# #     print(i)
# def tet_1(vh,x,y,give): # 1자
#     global result
#     if vh == 0:
#         if x+3>=len(give) or y >= len(give[0]):
#             return False
#         try:
#             i = [give[i][y] for i in range(x,x+4)]
#             # tmp = 0
#             # for j in i:
#             #     tmp +=j
#             result = max(result,sum(i))
#         except IndexError:
#             return False
            

#     else:
#         if x>=len(give) or y+3 >= len(give[0]):
#             return False
#         try:
#             i = give[x][y:y+4]
#             # tmp = 0
#             # for j in i:
#             #     tmp +=j
#             result = max(result,sum(i))
#         except IndexError:
#             return False

# def tet_2(x,y,give):
#     global result
#     if x+1>=len(give) or y+1 >= len(give[0]):
#             return False
#     try:
#         i = [give[x][y],give[x+1][y],give[x][y+1],give[x+1][y+1]]
#         # tmp = 0
#         # for j in i:
#         #     tmp +=j
#         result = max(result,sum(i))
#     except IndexError:
#         return False


# def tet_3(vh,x,y,give):
#     global result
#     dic = [
#         [
#             [[1,1],[0,1],[0,1]],
#             [[1,1],[1,0],[1,0]]
#         ],
#         [
#             [[1,0],[1,1],[1,0]],
#             [[1,0],[1,1],[0,1]],
#             [[0,1],[1,1],[1,0]],
#             [[0,1],[1,1],[0,1]]
#         ],
#         [
#             [[1,0],[1,0],[1,1]],
#             [[0,1],[0,1],[1,1]]
#         ]
#     ]
#     if vh == 0: #세로
#         if x+2>=len(give) or y+1 >= len(give[0]):
#             return False

#         try:
#             tb = [[] for _ in range(3)]
#             for i in range(3):
#                 for j in range(len(dic[i])):
#                     tmp = 0
#                     #dic[j][0] = [1,1]
#                     tt = []
#                     for k in range(3):
#                         for n in range(2):
#                             if dic[i][j][k][n] == 1:
#                                 tt.append(give[x+k][y+n])
#                     if len(tt) != 0:
#                         # tb[i].append(tt)
#                         # for num in tt:
#                         #     tmp += num
#                         # result = max(result,tmp)
#                         result = max(result,sum(tt))


#         except IndexError:
#             print('error')
#     else: #가로
#         if x+1>=len(give) or y+2 >= len(give[0]):
#             return False
#         try:
#             tb = [[] for _ in range(3)]
#             for i in range(3):
#                 tmp = 0
#                 for j in range(len(dic[i])):
#                     #dic[j][0] = [1,1]
#                     tt = []
#                     for k in range(3):
#                         for n in range(2):
#                             if dic[i][j][k][n] == 1:
#                                 tt.append(give[x+n][y+k])
#                     if len(tt) != 0:
#                         # tb[i].append(tt)
#                         # for num in tt:
#                         #     tmp += num
#                         result = max(result,sum(tt))
#                 # print(tb)
#         except IndexError:
#             print('error')

# for i in range(c):
#     for j in range(r):
#         for k in range(2):
#             tet_1(k,i,j,data)
#             tet_3(k,i,j,data)
#         tet_2(i,j,data)
# print(result)

# # tet_3(1,3,2,data)
'''
1회차 > python3 로 채점하니 시간초과, pypy3 로 채점하니 정답판정을 받았다.
        다른사람들은 dfs 로 풀었던데, 나중에 다시 풀게되면 dfs 를 사용하는 방법도 찾아보자
'''


###############################################################################################################################################################################################
#################################################################################     Q14503 _ 로봇청소기    ##################################################################################
###############################################################################################################################################################################################

'''
Given ) 로봇청소기가 N*M 의 영역을 청소하기 시작한다. 각가의 칸은 벽 또는 빈칸이다. 청소기는 동/서/남/북 중 하나로 바라보는 방향이 정해져있으며, 지도의 각 칸(r,c) 는 북쪽으로부터 r칸, 서쪽으로부터
        c 칸 멀어진것을 뜻한다.
        로봇청소기는 다음의 알고리즘을 따른다.
        1. 현재 위치를 청소한다.
        2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 인접한 칸을 탐색한다.
            2.a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전 후 한칸을 전진하고 1번으로 돌아간다.
            2.b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
            2.c. 2.b 의 반복을 통해 네 방향 모두 확인결과 모두 청소가 되어있거나 벽인 경우 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            2.d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 벽으로 막혀 후진을 할 수 없는 경우 작동을 멈춘다.
        로봇 청소기는 이미 청소된 칸을 청소하지 않으며, 벽을 통과하지 못한다
Input ) 첫째 줄에 세로크기 N 과 가로크기 M 이 주어진다. (3<=N,M<=50)
        둘째 줄에 로봇 청소기가 있는 칸의 좌표(r,c) 와 바라보는방향 d 가 주어진다. d가 0,1,2,3 순서로 북,동,남,서 방향을 가리킨다.
        셋째 줄부터 N 개의 줄에 맵 데이터가 주어진다. 0은 빈칸 1 은 벽을 나타낸다. 맵의 테두리는 벽으로 주어진다.

Output) 로봇청소기가 청소하는 칸의 개수를 구하라
'''

'''
Approach ) dxdy 테이블로 현재 로봇의 방향을 처리, 맵데이터에 0을 2 로 바꾸어서 방문처리
           만들어야할 모듈 // 0.회전탐색 1. 전진 2. 회전탐색 3. 후진
'''

# # r,c = 11,10
# # robot = [7,4,0]


# # data = [
# #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# #     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
# #     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
# #     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
# #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# #     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
# #     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],#
# #     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
# #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # ]

# dd = [[-1,0],[0,1],[1,0],[0,-1]]
# r,c = map(int,input().split())
# robot = list(map(int,input().split()))
# data = []
# for i in range(r):
#     data.append(list(map(int,input().split())))


# def turn(x): #방향 전환 0이 아니라면 -1 씩 해줘서 왼쪽으로 회전 0이라면 3으로
#     if x != 0:
#         a = x-1
#         return a
#     else:
#         a = 3
#         return a
# result = 0
# flag = True
# while flag:
#     check = True
#     x,y,d = robot[0],robot[1],robot[2]
#     if data[x][y] == 0:
#         data[x][y] = 2 #현재 위치 청소
#         result += 1
#     count = 0
#     for i in range(4): # 0. 회전탐색
#         d = turn(d)
#         nx,ny = x+dd[d][0],y+dd[d][1]
#         if data[nx][ny] == 0: #nxny 가 빈칸이라면 
#             robot = [nx,ny,d] #지금 방향 그대로 이동
#             break
#         count +=1
#         if count == 4: #4방향 모두 체크한결과 후진해야함
#             check = False

#     if not check: # 후진
#         nx,ny = x-dd[d][0],y-dd[d][1]
#         if data[nx][ny] != 1:
#             robot = [nx,ny,d]
#         else:
#             flag = False

#     # if result == 100:
#     #     break


# print(result)

'''
1회차 > 무조건 맞는데 왜 자꾸 틀렸다고 하나 하고 찬찬히 코드를 뜯어보던 중 마지막 line 1112 에 코드 확인용으로 적어두었던 break
        문을 지우지 않고 업로드했었다. 이걸 지우니 바로 정답을 받았다. 조금 어이없다 꼼꼼하게좀 보자
'''

###############################################################################################################################################################################################
####################################################################################     Q14503 _ 경사로    ###################################################################################
###############################################################################################################################################################################################
'''
Given ) N*N 크기의 지도가 있고, 각 칸에는 그 칸의 높이가 주어진다. 높이가 다른 칸을 지나기 위해선 L칸짜리 경사로가 필요하다. 오로지 높이가 1, 밑변이 L 인 삼각형의 빗변이 위로 가는 방향으로만
        놓을 수 있다.
Input ) 첫째 줄에 N (2<=N<=100) 과 L(1<=L<=N) 이 주어진다.
        둘째 줄부터 N 개의 줄에 지도가 주어지며, 각 칸의 높이는 10보다 작거나 같은 자연수이다.
Output) 지나갈 수 있는 길의 개수를 출력하라
'''

'''
Approach >> 각 행, 각 열마다 슬라이싱해온 후 경사로를 놓되, 경사로를 놓은 자리를 방문처리 리스트를 관리한다.
            매 칸을 순회하여 방문 후 다음칸의 높이가 2 이상 차이나면 해당 행렬은 바로 불가능판정.
            1만큼 높다면 현재칸을 포함하여 경사로를 놓을 L 칸이 방문처리되지 않고 같은 높이인지, 지도를 벗어나지 않는지 판별 후 조건 만족시 방문처리.
            1만큼 낮다면 다음칸을 포함하여 L 칸이 지도를 벗어나지 않고, 지도를 벗어나지 않는다면 방문처리.
            모든 행과 열이 위 처리를 만족한다면 count 를 return 해주면 됨.
'''

# count = 0
# # n,l = 6,1
# # data =[
# #     [3, 3, 3, 3, 3, 3],
# #     [2, 3, 3, 3, 3, 3],
# #     [2, 2, 2, 3, 2, 3],
# #     [1, 1, 1, 2, 2, 2],
# #     [1, 1, 1, 3, 3, 1],
# #     [1, 1, 2, 3, 3, 2]
# # ]
# # data = [
# #     [3, 2, 1, 1, 2, 3],
# #     [3, 2, 2, 1, 2, 3],
# #     [3, 2, 2, 2, 3, 3],
# #     [3, 3, 3, 3, 3, 3],
# #     [3, 3, 3, 3, 2, 2],
# #     [3, 3, 3, 3, 2, 2]
# # ]
# n,l = map(int,input().split())
# data = [list(map(int,input().split())) for _ in range(n)]

# def disc(lst,L,count): #정제된 list 입력
#     given = lst[:]
#     used_index = []
#     for i in range(len(given)-1):
#         if given[i+1] - given[i] == 1:#i가 i+1 보다 작을때 // 오름 경사
#             try:
#                 tmp = [i for i in range(i-L+1,i+1)]
#                 if i-L+1 < 0:
#                     return count
#                 if max([given[i] for i in tmp]) != min([given[i] for i in tmp]): # L 범위 내의 수가 모두 같은 수가 아닐때
#                     return count
#                 for i in tmp:
#                     if i in used_index: #방문처리가 이미 된 칸일때
#                         return count


#                 used_index += tmp

#             except IndexError: #지도를 벗어날 때
#                 return count
#         elif given[i+1] - given[i] == -1: #i+1 이 i 보다 작을때 // 내림 경사
#             try:
#                 tmp = [i for i in range(i+1,i+L+1)] 
#                 if max([given[i] for i in tmp]) != min([given[i] for i in tmp]): # 다음 L 범위의 숫자가 모두 같은가?
#                     return count
                
#                 used_index += tmp
                
#             except IndexError: #인덱스에러가 일어나는가?
#                 return count
#         elif given[i+1] - given[i] == 0:  #i 와 i+1 이 같을 때 // 평지
#             continue
#         else: #높이가 2 이상 차이나는 경우
#             return count

#     return count+1

# for i in range(n):
#     #행
#     v = data[i][:]
#     count = disc(v,l,count)
#     #열
#     h = [data[j][i] for j in range(n)]
#     count = disc(h,l,count)

# print(count)

'''
1회차 > 첫 런타임 에러를 제외한다면 line 1173 조건문을 추가하지 않아 오답판정을 받았다.
        모든 인덱스 에러를 제외문으로 처리하고자 하였으나, tmp 리스트에 음수 인덱스가 담기고 음수데이터를 리스트컴프리헨션을 통해
        리스트화 시켰을 때 올바른 데이터가 입력되어 생긴 문제였다. 인덱스에러 예외처리가 만능은 아니라는 점을 기억하자.
    
'''



###############################################################################################################################################################################################
#####################################################################################     Q14503 _ 감시    ####################################################################################
###############################################################################################################################################################################################
'''
Given ) CCTV 를 통해 N*M 크기의 직사각형 모양 사무실을 감시하고자 한다 CCTV 는 총 5가지가 있으며 모두 회전이 가능하다
        1. 한쪽방향 2.양쪽방향 3.ㄱ자 방향 4. ㅗ자 방향 5. 十자방향
        사무실에는 벽이 설치되어있으며 벽으로 가려서 CCTV 로 감시하지 못하는 범위를 사각지대라고 칭한다.
Input ) 첫째 줄에 사무실의 크기 N,M 이 주어진다 (1<=N,M<=8)
        둘째 줄부터 N 개의 줄에 사무실 각 칸의 정보가 주어진다. 0 은 빈칸, 6은 벽, 1~5는 CCTV 의 종류를 의미한다.
        CCTV 의 개수는 최대 8개를 넘지 않는다.
Output) 사각지대의 최소 크기를 출력하라.
'''

'''
Approach >> 현재 바라보는 방향을 사각지대에서 제외하는 함수(방문처리를 통해)와 dfs를 통해 문제를 풀어보고자 한다.
            사무실의 최대크기가 8*8 이므로 index 가 최대일 때 체크해도 무방할듯 함.
'''

#오답코드

    # # 북 동 남 서 >> 0,1,2,3
    # result = 1e9
    # cctv = []
    # walls = []
    # for i in range(N):
    #     for j in range(M):
    #         if 0<data[i][j]<6:
    #             cctv.append([data[i][j],i,j])
    #         elif data[i][j] == 6:
    #             walls.append([i,j])

    # print(cctv)
    # print(walls)
    # # dfs 내에서 4 방향 for문을 작성하되, count 를 관리하여 마지막의 경우  min(0) 값을 탐색하게 만들기
    # def rd(data,t,node,dir):
    #     pass

    # def ctd(data,t,node,dir):
    #     x,y = node
    #     if t == 1:
    #         index = 1
    #         d = [[-1,0],[0,1],[1,0],[0,-1]]
    #         while True:
    #             try:
    #                 if data[x+(d[dir][0])*index][y+(d[dir][1])*index] == 6:
    #                     return data
    #                 elif x+(d[dir][0])*index < 0 or y+(d[dir][1])*index < 0:
    #                     return data
    #             except IndexError:
    #                 return data

    #             if data[x+(d[dir][0])*index][y+(d[dir][1])*index] == 0:
    #                 data[x+(d[dir][0])*index][y+(d[dir][1])*index] = 9
    #             index += 1
    #     elif t == 2:
    #         l,r = False,False
    #         if dir == 1:
    #             index = 1
    #             while True:
    #                 try:
    #                     if data[x][y+index] == 6:
    #                         break
    #                 except IndexError:
    #                     break
    #                 if data[x][y+index] == 0:
    #                     data[x][y+index] = 9
    #                 index += 1
    #             index = 1
    #             while True:
    #                 try:
    #                     if data[x][y-index] == 6:
    #                         break
    #                     elif y-index < 0:
    #                         break
    #                 except IndexError:
    #                     break
    #                 if data[x][y-index] == 0:
    #                     data[x][y-index] = 9
    #                 index += 1


    # data = ctd(data,1,[2,2],3)
    # for i in data:
    #     print(i)

    # # def dfs(data,cctv,count):
    # #     global result
    # #     end = len(cctv)
    # #     if count == end:
    # #         print('check')
    # #         return
    # #     t,x,y =cctv[count]
    # #     temp = [i[:] for i in data]
    # #     # h_data = data[x][:]
    # #     # v_data = [ i[y] for i in data]
    # #     # print(h_data)
    # #     # print(v_data)
    # #     for i in range(4):
    # #         pass
            

    # # dfs(data,cctv,0)


    # N,M = 4,6
    # data = [
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 6, 0],
    #     [0, 0, 0, 0, 0, 0]
    # ]
'''
위에 길게 작성했는데 아무래도 아닌거같음 다르게 풀어봐야겠음
'''

# N,M = map(int,input().split())
# data = []
# for i in range(N):
#     data.append(list(map(int,input().split())))

# def change(data,node,dir):
#     x,y = node
#     if dir ==3:
#         for i in range(y-1,-1,-1):
#             if data[x][i] == 6:
#                 return data
#             if data[x][i] == 0:
#                 data[x][i] = 9
#         return data
#     elif dir == 1:
#         for i in range(y,len(data[0])):
#             if data[x][i] == 6:
#                 return data
#             if data[x][i] == 0:
#                 data[x][i] = 9
#         return data
#     elif dir == 0:
#         for i in range(x,-1,-1):
#             if data[i][y] == 6:
#                 return data
#             if data[i][y] == 0:
#                 data[i][y] = 9
#         return data
#     else:
#         for i in range(x,len(data)):
#             if data[i][y] == 6:
#                 return data
#             if data[i][y] == 0:
#                 data[i][y] = 9
#         return data

# # for i in data:
# #     print(i)
# node =[]
# for i in range(N):
#     for j in range(M):
#         if 0<data[i][j]<6:
#             node.append([data[i][j],i,j])


# end = len(node)
# result = 1e9
# def dfs(data,node,count):
#     global end,result
#     if count == end:
#         tmp = 0
#         for i in range(N):
#             for j in range(M):
#                 if data[i][j] == 0:
#                     tmp += 1
#         result = min(result,tmp)
#         return
#     t,x,y = node[count]
#     if t == 1:
#         for i in range(4):
#             dfs(change([i[:] for i in data],[x,y],i),node,count+1)
#     elif t == 2:
#         for i in range(2):
#             temp = change([i[:] for i in data],[x,y],i+2)
#             dfs(change([i[:] for i in temp],[x,y],i),node,count+1)
#     elif t == 3:
#         for i in range(4):
#             if i == 3:
#                 temp = change([i[:] for i in data],[x,y],0)
#             else:
#                 temp = change([i[:] for i in data],[x,y],i+1)
#             dfs(change([i[:] for i in temp],[x,y],i),node,count+1)
#     elif t == 4:
#         for i in range(2):
#             for j in range(2):
#                 if i == 0:
#                     temp = change([i[:] for i in data],[x,y],1)
#                     temp = change([i[:] for i in temp],[x,y],3)
#                     dfs(change([i[:] for i in temp],[x,y],j*2),node,count+1)
#                 else:
#                     temp = change([i[:] for i in data],[x,y],0)
#                     temp = change([i[:] for i in temp],[x,y],2)
#                     if j == 0:
#                         dfs(change([i[:] for i in temp],[x,y],1),node,count+1)
#                     else:
#                         dfs(change([i[:] for i in temp],[x,y],3),node,count+1)
#     else:
#         temp = change([i[:] for i in data],[x,y],0)
#         temp = change([i[:] for i in temp],[x,y],1)
#         temp = change([i[:] for i in temp],[x,y],2)
#         dfs(change([i[:] for i in temp],[x,y],3),node,count+1)


# dfs([i[:] for i in data],node,0)
# print(result)
# '''
# 1회차 > 오답목록 // 1. 어렵게 각 타입마다 다른 mapping 방법을 사용하려했음. 너무 복잡하고 코드도 길어짐
#                     >> 따라서 단순하게 상하좌우 확산하는 change 함수만으로 관리
#                     2. 다 맞춘거같은데 오답이 나옴
#                     >> type 4 의 line 1410 에서 change 함수의 i 입력관리를 제대로 하지 않아 오류가 발생
#                     >> dfs 내에 들어가는 data 부 change i 에 마지막 값을 제대로 넣어주어 정답판정
#         리뷰 // 오히려 아주 간단한 코드를 반복사용하는것이 간결하고 정확한 출력을 낼 수도 있다.
# '''



###############################################################################################################################################################################################
#################################################################################     Q14503 _ 사다리 조작    #################################################################################
###############################################################################################################################################################################################

'''
Given ) N 개의 세로선과 H 개의 가로선이 주어질 때, M 개의 가로선이 이미 배치되어있다.
        주어진 상황에서 i 번의 세로선이 출발하여 i 번으로 도착하기 위해 추가해야하는 가로선의 최솟값을 출력하라.
Input ) 첫째 줄에 세로선의 개수 N 과 그어진 가로선의 개수 M , 가로줄의 개수 H 가 주어진다  (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
        둘째 줄부터 M 개의 줄에 가로선(M) 의 정보가 한줄에 하나씩 주어진다. (a,b) b번 세로선과 b+1 번 세로선을 a번 가로줄 에서 연결했다는 의미
        가장 위의 가로줄이 1번이고 가장 왼쪽 세로줄의 번호가 1번이다.
Output) i번 세로선이 i번 으로 도착하도록 하는 추가 가로줄의 최소 개수를 출력하라. 만약 3 이상, 혹은 불가능이라면 -1 을 출력하라.
'''

'''
Approach >> 보니 세로선과 세로선 사이에 놓인 가로선의 갯수가 짝수여야 출발과 도착이 같을 수 있다. 또한 A-out 가로선과 A-in 가로선 사이에 B-out 가로선이 위치한다면 그 사이에 B-in 가로선이 위치해야만한다
            따라서 각 세로선을 따라 in&out 을 체크하여 주어진 데이터에서 가로선이 들어갈 수 있는 자리를 모두 받아오도록 해보자
'''

# # for i in give:
# #     data[i[0]-1][i[1]-1] = 1
# # ino =[[] for _ in range(N-1)]
# # point = [[] for _ in range(N-1)]

# # for i in range(len(data[0])):
# #     temp = [j[i] for j in data]
# #     for k in range(H):
# #         if temp[k] != 0:
# #             ino[i].append(k)

# # for i in range(len(ino)):
# #     if len(ino[i])%2 == 0:
# #         continue
# #     tmp = []
# #     if i == 0: #1번줄의 경우
# #         last = ino[i][-1]
# #         a,b = 0,H
# #         if ino
# #         pass

# # print(ino)


# # for i in data:
# #     print(i)

# N,M,H = 5,5,6

# data = [[0]*(N-1) for _ in range(H)]
# give = [
#     [5, 1],
#     [1, 1],
#     [3, 2],
#     [2, 3],
#     [5, 4]
# ]

# lines = [[] for _ in range(N-1)]
# for i,j in give:
#     lines[j-1].append(i)
# for i in lines:
#     i.sort()
# #3개 이상 그어야하는가?
# count = 0
# for i in lines:
#     if len(i)%2 !=0:
#         count +=1

# #각 줄마다 ino 체크
# print(lines)

'''

아 몰라!!!!!!!!!!!!!!!!!!!!!!!

'''


# RETRY #
'''
Given ) N 개의 세로선과 H 개의 가로선이 주어질 때, M 개의 가로선이 이미 배치되어있다.
        주어진 상황에서 i 번의 세로선이 출발하여 i 번으로 도착하기 위해 추가해야하는 가로선의 최솟값을 출력하라.
Input ) 첫째 줄에 세로선의 개수 N 과 그어진 가로선의 개수 M , 가로줄의 개수 H 가 주어진다  (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
        둘째 줄부터 M 개의 줄에 가로선(M) 의 정보가 한줄에 하나씩 주어진다. (a,b) b번 세로선과 b+1 번 세로선을 a번 가로줄 에서 연결했다는 의미
        가장 위의 가로줄이 1번이고 가장 왼쪽 세로줄의 번호가 1번이다.
Output) i번 세로선이 i번 으로 도착하도록 하는 추가 가로줄의 최소 개수를 출력하라. 만약 3 이상, 혹은 불가능이라면 -1 을 출력하라.
'''

'''
Approach >> 보니 세로선과 세로선 사이에 놓인 가로선의 갯수가 짝수여야 출발과 도착이 같을 수 있다. 또한 A-out 가로선과 A-in 가로선 사이에 B-out 가로선이 위치한다면 그 사이에 B-in 가로선이 위치해야만한다
            따라서 각 세로선을 따라 in&out 을 체크하여 주어진 데이터에서 가로선이 들어갈 수 있는 자리를 모두 받아오도록 해보자
'''
# def xprint(a):
#     for i in a:
#         print(i)


# # n,m,h = 5,5,6

# # #[a,b] b번 세로의 a번째 가로줄
# # give = [ 
# #     [1, 1],
# #     [3, 2],
# #     [2, 3],
# #     [5, 1],
# #     [5, 4]
# # ]
# give = []
# n,m,h = map(int,input().split())
# for i in range(m):
#     give.append(map(int,input().split()))
# def check(x): #x 는 boolean-list 형태
#     global n,h
#     back = []
#     for i in range(n):
#         stack = []
#         for j in range(h):
#             if 0<i<n-1:
#                 if x[j][i]:
#                     if len(stack) != 0 and stack[-1]==i+1:
#                         stack.pop()
#                         i += 1
#                         continue
#                     stack.append(i)
#                     i+=1
#                     continue
#                 elif x[j][i-1]:
#                     if len(stack) != 0 and stack[-1] == i-1:
#                         stack.pop()
#                         i-=1
#                         continue
#                     stack.append(i)
#                     i-=1
#                     continue
#             elif i == 0:
#                 if x[j][0]:
#                     if len(stack) !=0:
#                         stack.pop()
#                         i+=1
#                         continue
#                     else:
#                         stack.append(i)
#                         i+=1
#                         continue
#             elif i == n-1:
#                 if x[j][i-1]:
#                     if len(stack) !=0:
#                         stack.pop()
#                         i-=1
#                         continue
#                     else:
#                         stack.append(i)
#                         i-=1
#                         continue
#         if len(stack) !=0:
#             return False
#     return True

# def i_is_i(ladder):
#     for i in range(n):  # i가 i로 가는지 확인한다
#         col = i
#         for row in range(h):  # 마지막 가로줄(H) 가기 전까지 확인
#             if col < n-1 and ladder[row][col]:  # col번 세로선과 col+1번 세로선이 row번 가로선에 의해 연결되는가?
#                 col += 1  # 다음 세로줄로 이동
#             elif 0 < col and ladder[row][col-1]:  # col-1 세로선과 col 세로선이 row 가로선에 의해 연결되는가?
#                 col -= 1
#         if col != i:
#             return False
#     return True


# data = [[False]*(n-1) for _ in range(h)]
# for a,b in give:
#     data[a-1][b-1] = True #사다리 데이터 받아오기
# # empty = [[i[j] for i in data] for j in range(len(data[0]))]
# # print(check(data))
# # target = []
# # for i in range(len(empty)):
# #     if empty[i].count(True)%2 !=0:
# #         target.append(i)
# # print(target)
# # print(empty)
# result = 4
# def dfs(x,count,limit,a):
#     global result
#     l,h = len(x[0]),len(x)
#     if count == limit:
#         if i_is_i(x):
#             result = min(result,count)
#             return
#         return
#     for i in range(a,h):
#         for j in range(l):
#             # if count == limit:
#             #     if x[i][j] or x[i][j-1] or x[i][j+1]:
#             #         continue
#             #     x[i][j] = True
#             #     if check(x):
#             #         return count
#             #     x[i][j] = False
#             # else:
#             #     if x[i][j] or x[i][j-1] or x[i][j+1]:
#             #         continue
#             #     x[i][j] = True
#             #     dfs([i[:] for i in x],count+1,limit)
#             #     x[i][j] = False
            
#             if 0<j<l-1:
#                 if x[i][j] or x[i][j-1] or x[i][j+1]:
#                     continue
#             elif j == l-1:
#                 if x[i][j] or x[i][j-1]:
#                     continue
#             else:
#                 if x[i][j] or x[i][j+1]:
#                     continue
#             x[i][j] = True
#             dfs([q[:] for q in x],count+1,limit,i)
#             if result != 4:
#                 return
#             x[i][j] = False
#     return

# for i in range(4):
#     dfs(data,0,i,0)
# if result == 4:
#     result = -1
# print(result)



###############################################################################################################################################################################################
#################################################################################     Q14503 _ 드래곤 커브    #################################################################################
###############################################################################################################################################################################################
'''
Given ) 드래곤 커브는 3가지 속성으로 이루어진다. 1. 시작점 / 2. 시작방향 / 3. 세대
        i+1 세대는 i세대 끝점을 기준으로 i세대 드래곤 커브를 시계방향으로 90도 회전시킨 후 i세대의 끝점에 붙인 점이며, 여기서 끝점이란 시작점에서 선분을 타고 이동하여 이동했을 때 가장 먼 점이다.
        100*100인 격자 위에 드래곤커브가 N 개 있다. 이때, 크기가 1*1 인 정사각형의 네 꼭지점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램을 작성하라.
Input ) 첫째 줄에는 커브의 개수 N (1<= N <= 20)이 주어진다. 둘째 줄부터 N 개의 줄에는 드래곤커브의 정보가 주어진다. 드래곤커브의 정보는 x,y,d,g 로 이루어져 있으며,
        x,y 는 커브의 시작점, d 는 시작방향, g 는  세대이다.
Output) 1*1 정사각형의 개수를 출력하라
'''

'''
1회차 > 1세대 올라갈 때 마다 원소의 역순을 시계 반대방향으로 회전시켜 넣으면된다는 규칙을 확인했다. 구현해보자.
        마지막에 data 를 완전탐색하여 4칸이 모두 True 인 사각형을 찾으면 될 듯하다.
'''

# 방향 0 -> 3 (동 북 서 남)


def xprint(a):
    for i in a:
        print(i)

# n = 3
# give = [
#     [3, 3, 0, 1],
#     [4, 2, 1, 3],
#     [4, 2, 2, 1]
# ]
n = int(input())
give = []
for i in range(n):
    give.append(list(map(int,input().split())))

data = [[[] for _ in range(100)] for _ in range(100)]


def d_curve(x,y,d,g):
    dx,dy = [0,-1,0,1],[1,0,-1,0]
    data[x][y].append(d)
    temp = []
    temp.append(d)
    nx,ny = x+dx[d],y+dy[d]
    def turn(a):
        if a==3:
            a=0
        else:
            a += 1
        return a
    def rc(xx,yy,gg):
        nonlocal g,temp
        l = len(temp)
        tt=[]
        for i in range(l):
            i = -(1+i)
            d = turn(temp[i])
            tt.append(d)
            nx,ny = xx+dx[d],yy+dy[d]
            data[xx][yy].append(d)
            xx,yy = nx,ny
        temp += tt
        if g != gg:
            rc(xx,yy,gg+1)
            return
    if g != 0:
        rc(nx,ny,1)

    return

# def check_sq(x,y):
#     square = [False,False,False,False]
#     if 0 in data[x][y] or 2 in data[x][y+1]:
#         square[0] = True
#     if 3 in data[x][y] or 1 in data[x+1][y]:
#         square[1] = True
#     if 0 in data[x+1][y] or 2 in data[x+1][y+1]:
#         square[2] = True
#     if 3 in data[x][y+1] or 1 in data[x+1][y+1]:
#         square[3] = True
#     for i in square:
#         if not i:
#             return False
#     return True

for q,w,e,r in give:
    d_curve(w,q,e,r)

count = 0
for i in range(99):
    for j in range(99):
        if data[i][j]:
            if data[i][j+1]:
                if data[i+1][j]:
                    if data[i+1][j+1]:
                        count+=1

print(count)