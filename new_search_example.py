from collections import deque
from functools import partial
import typing_extensions

############################################  Q7 _ 럭키 스트레이트  ############################################
'''
Given ) 럭키 스트레이트는 특정 조건 만족할 경우만 발동한다
        특정 조건이란 현재 캐릭터의 점수 : N 에서 자릿수를 기준으로 점수 N 을 반으로 나누어 
        왼쪽부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합이 같을때를 의미한다.
        ex ) N = 123,402 일 경우 왼쪽의 합 6 오른쪽의 합 6 이므로 럭키스트레이트 발동 조건을 만족한다
Input ) 첫째 줄에 점수 N 이 정수로 주어진다.( 10<= N <= 99,999,999 ) 단, 점수 N 의 자릿수는 항상 짝수로 주어진다
Output) 첫째 줄에 럭키스트레이트 발동 가능할 경우 "LUCKY" 를 불가능할경우 "READY" 를 출력한다
'''

# # data = '123402'
# data = input()

# def LS(data):
#     half = len(data)/2
#     s = 0
#     for i in range(len(data)):
#         if i < half:
#             s -= int(data[i])
#         else:
#             s += int(data[i])
#     if s == 0:
#         print('LUCKY')
#     else:
#         print('READY')
# LS(data)
'''
1회차 > 상당히 쉬운 문제같다. BOJ 에서는 효율성테스트가 없어서 간단히 패스했으나 해답을 봐야 확실할 듯
'''

############################################  Q8 _ 문자열 재정렬  ############################################
'''
Given ) 알파벳 대문자와 숫자로 이루어진 문자열이 주어진다. 여기서 알파벳은 오름차순 정렬, 숫자는 모두 더해서 알파벳 뒤에 출력하라
Input ) 하나의 문자열 S 가 주어진다. (( 1 <= S <= 10,000 ))
Output) 요구 정답 출력
'''
# count = 0
# lst = []
# data = 'K1KA5CB7'
# for i in range(len(data)):
#     if data[i].isdigit() == True:
#         count+=int(data[i])
#     else:
#        lst.append(data[i]) 
# lst.sort()
# lst.append(str(count))
# print(''.join(lst))

'''
1회차>> isdigit // isalpha 를 들어는 봤는데 사용은 처음해본다. 그리고 join메서드도 처음 사용해본다.
추가로 join 메서드는 list 안에 모든 값이 같은 타입이어야 join 이 되는듯 하다.
'''


############################################  Q9 _ 문자열 압축  ############################################
'''
Given ) 임의의 문자열 S 가 주어진다 해당 문자열을 압축하고자 한다
        'aabbaccc' 의 경우 '2a2ba3c' 와 같이 압축하고 해당 패턴은 맨 앞부터 n 개 자리의 문자열을 선택하기로 한다
        따라서 문자열 'abcabcabcdedede' 3개 자리로 압축할 경우 '3abcdedede' 가 되는것.
Output) 주어진 문자열에서 가장 짧게 압축한 문자열의 길이를 반환하라
'''


# data = 'abcabcabcabcdededededede'

# min_len = len(data)
# half_num = int(len(data)/2)
# for i in range(1,half_num+1): 
#     compare = ''
#     count = 1
#     code = data[0:i]
#     for now in range(i,len(data),i): 
#         now_code = data[now:now+i]
#         if code == now_code: 
#             count +=1
#             if now+i >= len(data):
#                 compare += '{}{}'.format(count,code)
#                 code = now_code
#                 count = 1
#                 continue
#         elif code !=now_code and count == 1:
#             compare += '{}'.format(code)
#             code = now_code
#         else: 
#             compare += '{}{}'.format(count,code)
#             code = now_code
#             count = 1
#         if now+i >= len(data):
#             compare += (data[now:len(data)])
#     min_len = min(min_len,len(compare))

# print(min_len)

'''
1회차 > 다른 사람의 해답을 보았을 때 나보다 더욱 간결했다. 2개의 함수를 만들어서 사용했다.
        하지만 나는 함수 없이 2중 for문을 사용했기때문에, 아마 그 코드보다는 더욱 복잡한 코드일 것이다.
        또한 시간도 30분의 제한시간을 갖는 문제이지만, 나는 약 80분에 걸쳐서 풀어냈다. 아직 갈 길이 멀다.

'''

###############################################################################################################
############################################  Q10 _ 자물쇠와 열쇠  ############################################
###############################################################################################################
'''
Given ) 자물쇠의 크기는 n*n 크기의 정사각 격자형태이고 특이한 모양의 열쇠는 m*m 크기의 정사각 격자이다.
        자물쇠의 영역을 벗어나더라도 영역 내의 홈이 정확히 일치하면 자물쇠를 열 수 있다.
        열쇠를 나타내는 2차원 배열 key 와 lock이 매개변수로 주어질 때 해당 열쇠로 열 수 있다면 True를
        불가능하다면 False 를 return 하도록 함수를 작성하라.
        Key 는 M*M (3<= M <= 20 , M 은 자연수) 크기의 2차원 배열
        lock 는 N*N (3<= M <= 20 , M 은 자연수) 크기의 2차원 배열
        언제나 M < N 이며, key 와 lock의 원소는 0 또는 1 로 이루어져 있고, 0은 홈부분 1은 돌기를 나타낸다
'''

# m,n = 3,3


# key = list([0]*m for _ in range(m))
# new = [[0]*(n*3) for _ in range(n*3)]
# key = [[0,0,0],[1,0,0],[0,1,1]]
# lck = [[1,1,1],[1,1,0],[1,0,1]]
# # print(lck[1]+key[1])
# def rotate(data):
#     n = len(data)
#     m = len(data[0])
#     data_prime = [[0]*n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             data_prime[j][n-i-1] = data[i][j]
#     return data_prime

# def check(data):
#     a = len(data)//3
#     for i in range(a,a*2):
#         for j in range(a,a*2):
#             if data[i][j] !=1:
#                 return False
#     return True

# def solution(key,lock):
#     n = len(lock)
#     m = len(key)

#     for i in range(n):
#         for j in range(n):
#             new[i+n][j+n] = lock[i][j]

#     for _ in range(4):
#         key = rotate(key)
#         for x in range(n*2):
#             for y in range(n*2):

#                 for i in range(m):
#                     for j in range(m):
#                         new[x+i][y+j] += key[i][i]
#                 if check(new) == True:
#                     return True
                
#                 for i in range(m):
#                     for j in range(m):
#                         new[x+i][y+j] -= key[i][i]
#     return False

# print(solution(key,lck))

'''
1회차 > 160 line 의 들여쓰기 실수로 인해 틀렸다. for 문을 모두 순회하고서도 답이 안나온다면, false 를 반환해야 했지만, 들여쓰기 오류로 인해 line 146 의 첫 순환이 끝날 때 false
        를 반환해서 계속해서 오답처리되었음. 혹시나 하고 rotate 함수와 check 함수를 조금 만졌지만, 역시나 그 둘의 문제가 아니었음.
        흔히들 파이썬은 들여쓰기가 아주 중요하다고 하는데 이번 문제야말로 내가 그 오류를 범한 문제였음.
        물론 그것 말고도 for문이 많이 반복되어서 내 머리로 시뮬레이션 하기에 상당히 어려운 문제였음.
'''

###############################################################################################################
##################################################  Q11 _ 뱀  #################################################
###############################################################################################################

'''
Given ) 뱀은 돌아다니다 사과를 먹으면 길이가 늘어난다. 또한 뱀은 돌아다니다 벽 또는 자신의 몸과 부딫히면 게임이 끝난다.
        게임은 N*N 크기 정사각 보드위에서 시작되어 몇몇칸에는 사과가 놓여진다. 뱀은 왼쪽위에 오른쪽을 보며 위치하여 시작한다.
        1. 뱀은 움직일 때 몸을 늘려 머리를 다음칸에 위치시킨다.
        2. 이동칸에 사과가 있다면, 그 칸에 있는 사과는 없어지고 꼬리는 움직이지 않음
        3. 없다면 몸 길이를 줄여 꼬리가 위치한 칸을 비워준다.

input ) 첫째 줄에는 보드의 크기 N 이 주어짐  (2 <= N <= 100), 그리고 그 다음줄에는 사과의 개수 K 가 주어짐 (0<= K <= 100)
        다음 K개 줄에는 사과의 위치가 (행,열) 로 주어짐, (1행,1열)에는 사과가 없음
        그 다음줄에는 뱀의 방향변환횟수 L 이 주어짐 (1 <= L <= 100)
        다음 L개 줄에는 뱀의 방향변환 정보가 (정수 X , 문자 C) 로 주어짐. 게임 시작 후 X 초가 지나고 C(왼쪽 L 혹은 오른쪽 R) 방향으로 움직인다는 뜻
        여기서 X 는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X 가 증가하는 순으로 주어짐.

Output) 게임이 몇초 뒤에 끝나는지 출력하라.

1회차 > 처음엔 단순히 2차원 행렬에 더하는 방식으로 풀어볼까했으나, 오히려 우선순위 큐를 이용하는것이 꼬리를 밟는것도 구현 가능하여 좋겠다 생각함.
'''

# n = int(input())

# k = int(input())

# k_map = []
# for i in range(k):
#     a,b = map(int, input().split(' '))
#     k_map.append((a,b))

# L = int(input())

# L_Time = []

# for i in range(L):
#     time,dis = input().split(' ')
#     L_Time.append((int(time),dis))

# time_count = 0
# snake = [0,0]
# queue = deque()
# queue.appendleft([0,0])
# time_queue = deque()

# for i in L_Time:
#     time_queue.append(i)

# D = 1
# direction_y =  [-1,0,1,0]
# direction_x =  [0,1,0,-1]

# table = [[0]*(n) for _ in range(n)]

# for i in k_map:
#     table[i[0]-1][i[1]-1] = 1

# while True:

#     time_count +=1


#     snake[0] += direction_y[D]
#     snake[1] += direction_x[D]
#     new = [snake[0],snake[1]]
#     if (snake[0] == n or snake[0] < 0 or snake[1] == n or snake[1] < 0) or (snake in queue):
#         break
#     queue.appendleft(new)


#     if table[snake[0]][snake[1]] == 1:
#         table[snake[0]][snake[1]] = 0
#     else:
#         queue.pop()

#     if len(time_queue) > 0:
#         if time_queue[0][0] == time_count:
#             if time_queue[0][1] == 'D':
#                 D += 1
#                 if D == 4:
#                     D = 0
#             else:
#                 D -= 1
#                 if D == -1:
#                     D = 3
#             time_queue.popleft()

# print(time_count)

'''
1회차 >> 우선순위 큐를 이용하여 정답판정을 받았다. line 240 의 break 처리 위치를 잘 생각하고 위치시켰으면 더 빨리 풀었을 것.
'''



###############################################################################################################
############################################  Q12 _ 기둥과 보 설치  ###########################################
###############################################################################################################

'''
Given ) 2차원 가상 벽면에 기둥과보를 이용한 구조물을 설치하고자 하며 기둥과 보는 길이가 1 인 선분으로 표현되며 다음과 같은 규칙을 따른다.
        1. 기둥은 바닥 위에 있거나, 보의 한쪽끝, 혹은 다른 기둥 위에 있어야한다.
        2. 보는 한쪽 끝이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어야 한다.
        여기서 벽면은 N*N 의 정사각 격자형태이며 맨 처음에는 비어있는 상태이다.

Input ) N 은 5<= N <= 100 의 자연수 buildFrame 의 세로길이(주어지는 데이터 갯수) 는 1이상 1,000 이하이며 buildFrame 의 가로길이는 4 로
        (x,y,a,b) 로 주어진다. 여기서 x,y 는 구조물을 설치할 좌표이며, a는 구조물의 종류( 0: 기둥, 1: 보 )이며, b는 설치(1) 혹은 삭제(1) 여부이다.
        여기서 구조물은 무조건 보의 경우 기준점으로부터 오른쪽으로 기둥은 기준점으로부터 위로 설치 혹은 삭제한다.

Output) Ourput 은 아래 규칙에 따른다.
        return되는 배열은 다음과 같이 데이터를 담는다 (x,y,a) x,y좌표와 a: 기둥(0) 인지, 보(1) 인지
        또한 Input과 같이 x,y 는 교차점의 위치이며, 기둥과 보는 교차점을 기준으로 위로 혹은 오른쪽으로 뻗는다.

'''

# # Given = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# Given = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# Output = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
# n = 5
# N = n+1
# table = [[0]*N for _ in range(N)]

# def check(table,x,y,a):
#     beam = 0

#     if a == 0: 
#         if table[y+1][x]%2 == 1: 
#             if table[y+1][x-1] >= 2 and table[y+1][x+1] >= 2 :
#                 return True
#             return False
#         elif table[y+1][x] == 2:
#             if table[y+1][x-1] >= 2 and table[y+1][x+1] >= 2:
#                 return True
#             return False

#     elif a == 1:
#         left,right = table[y][x-1],table[y][x+1]
#         if left >= 2:
#             if table[y-1][x-1]%2 == 1 and table[y-1][x]%2 == 1:
#                 beam +=1
#             return False
#         elif right == 1:
#             if table[y-1][x+1] ==1:
#                 beam +=1
#             return False
        
#         if beam == 2:
#             return True
#         else:
#             return False

#     return ValueError


# for i in Given:
#     x,y = i[0],i[1]
#     if i[2] == 1 and i[3] == 1:
#         if i[2] == 1: #보 조건
#             if (table[y-1][x]%2 == 1 or table[y-1][x+1]%2 == 1) or (table[y][x-1] ==2 and table[y][x+1] == 2):
#                 table[y][x] += 2
#             else:
#                 continue
#     elif i[2] == 0 and i[3] == 1: #기둥 조건
#             if table[y-1][x]%2 == 1 or y == 0 or table[y][x-1] ==2:
#                 table[y][x] +=1
#             else:
#                 continue
#     elif i[3] == 0:
#         x,y,a = i[0],i[1],i[2]
#         if check(table,x,y,a) ==True:
#             table[y][x] -= a+1
#         else:
#             continue

# result = [] 
# for i in range(N):
#     for j in range(N):
#         if 0 < table[i][j] < 3:
#             x,y,a = j,i,(table[i][j]-1)
#             result.append([x,y,a])
#         elif table[i][j] == 3:
#             x,y,a,b = j,i,(table[i][j]-2),(table[i][j]-1)
#             result.append([x,y,a])
#             result.append([x,y,b])

# result.sort()

# print(result)
'''
1st )   나의 코드는 너무 조건문이 많이 붙었다. 그리고 단순히 매 입력마다 삭제의 경우 상하좌우만 살폈는데,
        그렇게 하니 예시 코드는 맞더라도 채점 코드에서는 틀렸다. 아무래도 잘 못 하고있는 것 같아 정답을 보고 다시 코드를 짜보려한다.
'''

# def check(result):
#     for x,y,a in result:
#         if a == 0:
#             if y == 0 or [x,y-1,0] in result or [x,y,1] in result or [x-1,y,1] in result:
#                 continue
#             return False
        
#         elif a == 1:
#             if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x+1,y,1] in result and [x-1,y,1] in result):
#                 continue
#             return False


#     return True

# Given = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
# result = []

# for i in Given:
#     x,y,a,b = i
#     if b == 1:
#         result.append([x,y,a])
#         if not check(result):
#             result.remove([x,y,a])
#     if b == 0:
#         result.remove([x,y,a])
#         if not check(result):
#             result.append([x,y,a])
            
# result.sort()

# print(result)


'''
2회차 ) 위의 방법대로 부분검사가 아닌 전체검사를 시행하니 간단하게 정답처리를 받을 수 있었다.
        내가 처음 짠 코드보다 거의 1/3수준으로 짧은 코드지만 정답처리를 받았다. 다음에 다시풀 땐 더 간결하게 짜보자
'''




###############################################################################################################
##############################################  Q13 _ 치킨 배달  ##############################################
###############################################################################################################
'''
Given ) 도시의 크기 N*N 에서 각 1*1 크기의 칸으로 나누어져있다. 각 칸은 빈칸, 집 혹은 치킨집이다.
        좌표는 (r,c) 로 주어지며 위에서 r번째 칸, 왼쪽에서 c 번째 칸을 의미한다.
        ** 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리.
        각각의 집은 치킨거리를 가지며, 도시의 치킨거리는 모든 집의 치킨거리의 합이다.
        도시의 치킨거리값이 최소가 되는 도시 내의 치킨집 중 최대 M 개를 고르고 나머지는 폐업시키고자 한다. 

Input ) 첫째 줄에 N(2<= N <=50) 과 M(1<= M <= 13) 이 주어진다
        둘째 줄 부터는 도시의 정보가 주어진다.
        도시의 정보는 0,1,2 로 주어지고 0 은 빈칸 1 은 집 2 는 치킨집이다. 집의 개수는 2N 을 넘지 않고 최소 1개 이상 존재한다

Output) 치킨집을 최대 M 개 골랐을 때 도시의 치킨거리 최솟값 출력

'''

# from itertools import combinations


# N,M = map(int,input().split(' '))
# Input = []
# kfc,house = [],[]

# for i in range(N):
#     Input = list(map(int,input().split()))

#     for j in range(N):
#         if Input[j] == 1:
#         # if Input[i][j] == 1:
#             house.append([i,j])
#         elif Input[j] == 2:
#         # elif Input[i][j] == 2:
#             kfc.append([i,j])
# kfc = list(combinations(kfc,M))

# def get_sum(chicken):
#     result = 0
#     for hx,hy in house:
#         temp = 1e9
#         for x,y in chicken:
#             temp = min(temp,abs(hx-x)+abs(hy-y))
#         result += temp
#     return result
# result = 1e9
# dif = 0

# for chicken in kfc:
#     result = min(result,get_sum(chicken))

# print(result)

# for branch in kfc:        # 경우의 수 분배
#     dif = 0
#     check = []
#     index = 1

#     while len(check) != len(house):
#         index +=1
#         for x,y in branch:        #분배 된 경우의 수 내의 치킨집 좌표
#             check_list = [] 

#             for i in range(index): #x
#                 for j in range(-index+1,i): #y
#                     if i == 0 and j == 0:
#                         continue
#                     elif i == index-1:
#                         pass
#                     elif i == 0:
#                         check_list.append([index-1,x,y+j])
#                         check_list.append([index-1,x,y-j])
#                     elif j == 0:



                        
#             # for i in range(index):        #인덱스(치킨거리) 를 늘려가며 해당 경우의 수에서의 최소 치킨거리 반환
#             #     for j in range(-index+2,1):
#             #         if i == 0 and j == 0:
#             #             continue
#             #         elif i == 0:
#             #             check_list.append([index-1,x,y-j])
#             #             check_list.append([index-1,x,y+j])
#             #         elif j == 0:
#             #             check_list.append([index-1,x+i,y])
#             #             check_list.append([index-1,x-i,y])
#             #         else:
#             #             check_list.append([index-1,x-i,y-j])
#             #             check_list.append([index-1,x-i,y+j])
#             #             check_list.append([index-1,x+i,y-j])
#             #             check_list.append([index-1,x+i,y+j])

#             for i,x,y in check_list:
#                 if [x,y] in house and [x,y] not in check:
#                     check.append([x,y])
#                     dif += i
        
#     result = min(result,dif)

# print(result)
'''
1회차 ) 실패. 이유는 좌표에 대한 이해부족. 두 좌표의 xy값을 뺀 뒤 더하면 거리가 나오는것인데 모든 좌표를 확인하려했음.
'''


###############################################################################################################
##############################################  Q14 _ 외벽 점검  ##############################################
###############################################################################################################

'''
Given ) 레스토랑의 취약 외벽을 점검하고자 한다. 점검 시간은 1시간으로 제한되며, 최소한의 친구를 보내 외벽을 점검하고
        나머지는 공사를 돕는다. 레스토랑의 정북방향을 0 으로 두고 취약지점은 시계방향으로 떨어진 거리로 나타낸다
        친구들은 외벽을 따라 시계, 또는 반시계 방향으로 외벽을 따라 움직인다.

Input ) 외벽의 길이 n (1 <= n <= 200 의 자연수)
        1<= len(weak) <=15
        -> 취약점의 위치는 중복되지 않는다
        -> 취약점의 위치는 오름차순으로 주어진다
        -> weak 의 원소는 0 이상  n-1 이하의 정수다
        
        1<= len(dist) <= 8
        ->dist의 원소는 1이상 100이하의 자연수이다.
        
        친구들을 모두 투입해도 점검할 수 없을 땐 -1 을 return 하라

Output) 외벽점검을 위한 최소인원 return
'''

'''
이 문제는 주어진 조건에서 weak, dist 리스트가 확실히 짧다는것을 알 수 있다. 이는 완전탐색으로 접근하기에 매우 유리하다
문제에서 구하고자 하는 답은 '투입해야하는 친구의 수' 이다. 따라서 모든 친구를 무작위로 나열하는 모든 순열을 구하고(Permutations)
각 리스트별로 비교하여 최소 몇명 배치 시 모두 확인할 수 있는지 구하면 된다.

또한 이와같은 원형 배열문제는 해당 배열을 2배로 늘려 직선으로 만들면 더욱 쉽게 접근할 수 있다.
'''

# from itertools import permutations

# n = 12
# weak = [1,5,6,10]
# dist = [1,2,3,4]

# def solution(n,weak,dist):
#     length = len(weak)

#     for i in range(length):
#         weak.append(weak[i] + n)  

#     answer = len(dist) + 1

#     for start in range(length): 
#         for friends in list(permutations(dist, len(dist))): 
#             count = 1 
#             position = weak[start] + friends[count - 1] 

#             for index in range(start, start + length):

#                 if position < weak[index]:
#                     count += 1
#                     if count > len(dist):
#                         break
#                     position = weak[index] + friends[count-1]

#             answer = min(answer,count)

#     if answer > len(dist):
#         return -1
#     return answer

# print(solution(n,weak,dist))


'''
1회차 > 아예 손도못댔다 구현 구상부터 구현까지 하다못해 있는 코드마저도 제대로 못써서 틀렸다.
'''



###############################################################################################################
########################################  Q15 _ 특정 거리의 도시 찾기  ########################################
###############################################################################################################
'''
Given ) 어느 나라에는 1~N 번까지의 도시와 M 개의 단방향 도로가 존재하며 각 도로의 거리는 1이다.
        여기서 특정 도시 X 를 출발하여 도달할 수 있는 모든 도시중에서, 최단거리가 정확히 K인 모든 도시의 번호를
        출력하는 프로그램을 작성하시오. 또한 출발도시 X 에서 다시 출발도시 X 로 가는 최단거리는 0 으로 가정한다.

Input ) 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발도시의 번호 X 가 주어진다.
        둘째 줄 부터는 M 개의 줄에 걸쳐 두 개의 자연수 A,B 가 주어지며 A 도시에서 B 도시로 가는 단방향 도로가 존재한다는 의미
        단 A 와 B 는 항상 다른 자연수이다.

Output) X 로 부터 출발하여 도달할 수 있는 도시 중에서, 최단거리가 K 인 모든 도시의 번호를 한줄에 하나씩 오름차순으로 출력
        만약 최단거리가 K 인 도시가 존재하지 않는다면 -1 반환출력


1회차 ) 모든 노드에서 모든 노드까지의 거리를 구하는 플로이드 워셜 알고리즘은 O(N^3) 인데 N 의개수가 최대 300,000 이므로
        900조에 가까운 데이터가 나올 수 있으므로 제외한다.
        우선순위 큐를 이용한 경로탐색을 해보고자 한다.
'''

# from collections import deque
# import sys
# input = sys.stdin.readline

# N,M,K,X = map(int, input().split())
# data = [[] for _ in range(N+1)]
# dist = [-1]*(N+1)
# dist[X] = 0
# queue = deque([X])
# for i in range(M):
#     a,b = list(map(int,input().split()))
#     data[a].append(b)
# check = False
# while queue:
#     X = queue.popleft()
#     for i in data[X]:
#         if dist[i] == -1:
#             dist[i] = dist[X]+1
#             queue.append(i)
            
# for i in range(1,N+1):
#     if dist[i] == K:
#         print(i)
#         check = True

# if check == False:
#     print(-1)


'''
1회차 ) 풀어본 결과 답은 도출 되나, 시간초과 판정을 받았다. 아무래도 큰 N,M,K 에 맞춰서 코드를 짜지 않아서인 것 같다.
        그리고 해답 확인결과, 우선순위큐를 사용하는것도 맞았고 나의 계획이 상당히 많이 맞았다.


        07/08 ) 다시 해답을 확인해 본 결과 해답과는 큰 차이를 보이지 않았다. 그럼에도 시간초과가 나오고 하다하다 답답해서
        해답을 그대로 작성했음에도 오답처리를 받았다. 따라서 그 이유를 찾아본 결과, Input의 사용때문이었다.

        반복 입력이 굉장히 많기때문에 단순한 input 으로는 시간초과를 받을 수 밖에 없다. 그 이유는 input() 함수는 input 되는 string을
        받고 \n 의 개행문자를 제거 한 뒤 return 해주기 때문에 input값이 많은 문제를 풀 땐 입력만으로 그만큼 많은 시간을 소모한다.
        따라서 이와같이 아주 많은 input 을 가지는 문제는 sys 를 import 해 준 뒤,  input() 함수 대신 sys.stdin.readline() <<s.s.r 이라 칭하겠음>>
        을 사용해주자 여기서 s.s.r 은 문자열을 개행문자까지 return 해주지만, 어차피 map(int,**)함수를 사용하므로 split() 을 통해
        map 에 들어온 개행함수는 int 변환 시 사라지고 단순한 정수값만 return 되는 것.

        이런 발견이 나로써는 기쁘다. 아주 작은 발견이지만 나로선 조금이라도 성장한 기분이 든다. 아무튼간에 내 코드는 맞았고 s.s.r의 사용법만
        제대로 익히자
'''




###############################################################################################################
###############################################  Q16 _ 연구소  ################################################
###############################################################################################################
'''
Given ) 연구소의 크기 N*M 이 주어진다 행렬의 각 칸은 빈칸,바이러스 혹은 벽으로 이루어진다
        바이러스는 상하좌우 인접 행렬로 퍼져나가며, 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개롤 세워야한다.
        0은 빈칸, 1은 벽, 2는 바이러스를 의미한다.
        먼저 벽이 세워진 뒤 바이러스는 벽으로 격리되지 않은 모든 영역으로 퍼진다. 이후에 빈칸으로 격리되어 남아있는 영역을
        안전구역으로 지칭하고 안전구역의 최댓값을 구하는 프로그램을 작성하라

Input ) 첫째 줄에는 지도의 세로 크기 N 과 가로 크기 M 이 주어진다. (3<= N,M <= 8)
        둘째 줄부터는 N 개줄에 지도의 모양이 주어짐. 2<= (2) <= 10
        빈칸의 개수는 3개 이상

Output) 첫째 줄에 얻을 수 있는 안전구역의 최댓값 출력

1회차 > 주어지는 지도의 크기가 크지 않고, 바이러스의 개수 또한 10개 이하이므로, 처음에는 모든 경우의 수에 벽을 하나씩 세워본 뒤
        빈칸을 bfs 로 구하다가 2를 만나면 모두 2로 바꾸려고 했다.
        하지만 다시 생각해보니, 같은 방식으로 2를 bfs 탐색으로 만나는 0 마다 모두 2로 바꿔주고 마지막에 테이블을 검사하여
        0 의 개수를 세어주면 되는 것 아닌가? 싶어서 해당 방식을 사용해보고자 한다.

'''
# from itertools import combinations
# from collections import deque
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# data = [[] for _ in range(n)]

# for i in range(n):
#     a= list(map(int,input().split()))
#     data[i].append(a)
# virus = []
# empty = []
# count = 0
# for i in range(n):
#     for j in range(m):
#         if data[i][j] == 2:
#             virus.append([i,j])
#         elif data[i][j] == 0:
#             empty.append([i,j])

# def bfs(data,b,h):
#     x = [-1,0,1,0]
#     y = [0,1,0,-1]
#     q = deque()
#     q.append([b,h])
#     while q:
#         check = False
#         b,h = q.pop()
#         for i in range(4):
#             X,Y = x[i],y[i]
#             if -1<b+Y<n and -1<h+X<m and (data[b+Y][h+X] !=1 and data[b+Y][h+X] != 2):
#                 if check == False:
#                     q.append([b,h])
#                     check = True
#                 q.append([b+Y,h+X])
#                 data[b+Y][h+X] = 2
#     return data

# options = list(combinations(empty,3))
# option = [[0,1],[1,0],[3,5]]

# def test(data,option):
#     count = 0
#     for i in range(3):
#         data[option[i][0]][option[i][1]] = 1
    
#     for i in virus:
#         x,y = i[0],i[1]
#         data = bfs(data,x,y)
    
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 count+=1

#     return count

# for i in options:
#     data_prime = [i[:] for i in data]
#     count = max(count,test(data_prime,i))

# print(count)

'''
1회차 ) 거의 순수하게 내 구상만으로 문제를 풀어냈다. 해답에서도 비슷한 방향으로 진행되었고
        무엇보다도, bfs 를 사용한 점과 combination 을 이용한 점이 특별했다.
        새롭게 배운것은 앞서 배운 sys.stdin.readline 을 이용해서 input 의 시간을 단축시키고
        검색해서 알게 된 행렬의 전치 deepcopy 메서드를 사용하는것이며, 해당 메서드 사용시
        약 7.6초가 걸려서 python 시간보정으로 인해 시간제한 8초에 거의 가깝게 해답이 나왔지만,
        또 새롭게 알게 된 리스트 슬라이싱으로 행렬을 전치하는 방법으로 6초대까지 단축시켰다.
'''


###############################################################################################################
#############################################  Q16 _ 경쟁적 전염  #############################################
###############################################################################################################
'''
Given ) N*N 크기의 시험관 행렬이 주어진다. 또한 특정 위치에는 바이러스가 존재하며 그 종류는 1~K번 까지 K종류가 있으며
        모든 바이러스는 이 중 하나에 속한다. 모든 바이러스는 1초마다 상/하/좌/우 방향으로 증식하며 매 초 번호가
        낮은 바이러스가 우선증식한다. 또한 빈칸에 다른 바이러스가 우선적으로 증식한다면 그 칸에는 증식할 수 없다.
        시험관의 크기가 주어질 때 S 초가 지난 후 (X,Y) 에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하라
        S초 이후에 해당 위치에 바이러스가 없다면 0 을 출력하라.
        이 때 X,Y 는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)로 지정한다.

Input ) 첫째 줄에는 자연수 N,K 가 주어지며, 공백으로 구분한다. (1<= N <=200)  /// (1<= K <=1,000)
        둘째 줄 부터는 N 개의 줄에 걸쳐 시험관의 정보가 주어진다. 빈칸은 0 그리고 1~K 번까지의 바이러스 번호가 배치된다.
        마지막줄에는 S,X,Y 가 주어지며, S 초 뒤에 (X,Y) 자리에 무엇이 위치하는지를 알아보는 입력이다.

Output) S초 뒤에 (X,Y) 에 존재하는 바이러스의 종류를 출력하고 만약 없다면 0 을 출력하라.
'''
n = 3
k=3
K = [i for i in range(1,k+1) ]
data = [[1,0,2],[0,0,0],[3,0,0]]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
