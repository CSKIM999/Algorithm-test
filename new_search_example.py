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

1회차 ) 큐 없이 단순한 for 문 반복으로 풀어보고자 했음.
        바로 직전문제와 상당히 비슷해서 비슷한 구현방식을 채택
'''
# import sys
# input = sys.stdin.readline
# n,K = map(int,input().split())
# virus = [[] for _ in range(K)]
# data = [[] for _ in range(n)]
# for i in range(n):
#     data[i] = list(map(int,input().split()))
# s,X,Y = map(int,input().split())
# n = 3
# K=3
# s = 1


# data = [[1,0,2],[0,0,0],[3,0,0]]

# for i in range(n):
#     for j in range(n):
#         if data[i][j] != 0:
#             x = data[i][j]
#             virus[x-1] = [[i,j]]

# def expand(n,K,data,k):
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]
#     for i in range(K):
#         num = len(k[i])
#         for l in range(num):
#             x,y = k[i][l]
#             for j in range(4):
#                 nx = x+dx[j]
#                 ny = y+dy[j]
#                 if -1<nx<n and -1<ny<n:
#                     if data[nx][ny] ==0 and [nx,ny] not in k[i]:
#                         data[nx][ny] = i+1
#                         k[i].append([nx,ny])
    
#     return data,k

# for _ in range(s):
#     data, k =expand(n,K,data,virus)
# print(data[X-1][Y-1])

'''
1회차 > 큐 없이 구현한 결과, 답은 도출되나 채점결과 시간초과판정을 받음.
        흔히 이런 경우 시간 단축을 위해 큐를 쓰는데, 해답에서는 큐를 사용한 bfs 를 사용하라고 가이드해주고있음.
        내일 한번 짜봐야할듯
        
'''

# import sys
# from collections import deque
# input = sys.stdin.readline

# n,K = map(int,input().split())
# data = [[] for _ in range(n)]
# virus =[]
# for i in range(n):
#     data[i] = list(map(int,input().split()))
#     for j in range(n):
#         if data[i][j] !=0:
#             virus.append([data[i][j],0,i,j])
# s,X,Y = map(int,input().split())
# virus.sort()
# q = deque(virus)


# while q:
#     a,time,x,y = q.popleft()
#     if time == s:
#         break
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if -1<nx<len(data) and -1<ny<len(data):
#             if data[nx][ny] == 0:
#                 data[nx][ny] = a
#                 q.append([a,time+1,nx,ny])


# print(data[X-1][Y-1])

'''
1-1회차)다시 해답의 도움을 조금 받고 내 구현방법을 사용해서 풀어 본 결과, 정답판정을 받았다.
        line 835-837 까지 입력을 받자마자 그 내용을 분류해서 virus 리스트에 삽입 후
        입력이 끝나고 정렬해서 큐에 넣는 방식은 새로웠다.
'''



###############################################################################################################
#############################################   Q18 _ 괄호 변환   #############################################
###############################################################################################################

'''
Given ) "(,)" 로만 이루어진 문자열이 있을 경우 '(' 의 개수와 ')'의 개수가 같다면 이를 [[균형잡힌 괄호 문자열]] 로 칭함
        여기에 괄호의 짝도 모두 맞을 경우 [[올바른 괄호 문자열]] 로 칭함.
        "(()))(" << 균형잡힌 괄호 문자열 // "(())()" << 균형잡힌 괄호문자열 이자, 올바른 괄호문자열
        문자열 w 가 균형잡힌 괄호 문자열이라면, 다음 과정을 통해 올바른 문자열로 변환한다.

        1 ) 입력이 빈 문자열일 경우 빈 문자열 반환
        2 ) 문자열 w 를 두 균형잡힌 괄호문자열 u,v 로 분리한다. 단, u는 더이상 균형잡힌 문자열로 분리가 불가능해야하며,
            v 는 빈 문자열이 될 수 있다.
        3 ) 수행 결과를 문자열 u 에 이어 붙인 후 반환한다.
            3-1) u 가 "올바른 괄호 문자열" 이라면, 문자열 v 에 대해 1단계부터 다시 수행한다.
        4 ) u 가 "올바른 괄호 문자열"이 아니라면, 아래 과정을 수행한다.
            4-1) 빈 문자열에 첫 번째 문자로 ( 를 붙인다.
            4-2) 문자열 v 에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어붙인다.
            4-3) ) 를 다시 붙인다.
            4-4) u  의 첫번째, 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
            4-5) 생성 문자열을 반환한다.

Input ) p 는 ( 와 )로만 이루어진 문자열이며, 길이는 2 이상 1,000 이하의 짝수
        p 를 이루는 ( 와 )의 개수는 항상 같다.

Output) 만약 p 가 이미 올바른 괄호 문자열이라면 그대로 return 하라.
'''

# p = '()))((()'

# def check_right(p):
#     count = 0
#     for i in p:
#         if i == '(':
#             count +=1
#         else:
#             count -=1
#         if count < 0:
#             return False

#     return True
# def bal(p):
#     count = 0
#     for i in range(len(p)):
#         if p[i] == "(":
#             count+=1
#         else:
#             count-=1
        
#         if count == 0:
#             return i


# def solution(p):
#     answer = ''
#     if len(p) == 0: # num_1
#         return answer
#     #  num_2
#     i = bal(p)
#     u = p[:i+1]
#     v = p[i+1:]

#     if check_right(u) == True:
#         answer = u + solution(v)
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#         u = list(u[1:-1])
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
#         answer += ''.join(u)

#     return answer

# answer = solution(p)
# print(answer)

'''
1회차 > 아우 존나게 복잡하다 뭐이렇게 복잡해
'''


###############################################################################################################
##########################################   Q19 _ 연산자 끼워넣기   ##########################################
###############################################################################################################
'''
Given ) N 개의 수와 N-1 개의 연산자가 주어질 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하라.

Input ) 첫째 줄에는 수의 개수 N ( 2<= N <= 11) 이 주어집니다.
        둘째 줄에는 A_1 ..... A_n 이 주어집니다. ( 1<= A_i < 100)
        셋째 줄에는 합이 N-1 인 정수 4개가 주어지는데, 차례대로 덧셈,뺄셈,곱셈,나눗셈 연산자의 개수이다.

Output) 첫째 줄에는 최댓값 출력
        둘째 줄에는 최솟값 출력
        모든 계산값은 항상 -1e9 <= X <= +1e9 이내의 범위에 있다.

1회차 > combination 을 사용하려 했으나, 시간이 초과되었다.
        해답의 알고리즘이 신기해서 이해하는데만 한참 걸렸다.
'''

# n = input()
# data =[0 for _ in range(n)]
# data = list(map(int,input().split()))
# add,sub,mul,div = list(map(int,input().split))

# min_val = 1e9
# max_val = -1e9

# def bfs(i,now):
#     global min_val,max_val,add,sub,mul,div

#     if i == n:
#         min_val = min(min_val,now)
#         max_val = max(max_val,now)
#     else:
#         if add >0:
#             add -=1
#             bfs(i+1,now+data[i])
#             add +=1
#         if sub >0:
#             sub -=1
#             bfs(i+1,now-data[i])
#             sub +=1
#         if mul >0:
#             mul -=1
#             bfs(i+1,now*data[i])
#             mul +=1
#         if div >0:
#             div -=1
#             bfs(i+1,int(now/data[i]))
#             div +=1
    
#     return max_val,min_val

# max_val,min_val = bfs(1,data[0])
# print(max_val)
# print(min_val)


###############################################################################################################
############################################   Q20 _ 감시 피하기   ############################################
###############################################################################################################
'''
Given ) N*N행렬 크기의 복도가 주어진다. 각 특정위치에는 선생,학생,장애물이 위치한다.
        복도에 나온 학생들이 선생의 감시에 들키지 않는것이 목표이다. 선생은 자신의 위치에서 상하좌우 4가지 방향으로 감시를 진행한다.
        그러나, 만약 장애물로 가로막혀있다면, 그 너머의 학생은 보지 못한다. 우리는 정확히 3개의 장애물을 설치해서
        선생님의 감시를 피할 수 있는지 출력하는 프로그램을 작성하라.

Input ) 첫째 줄에는 자연수 N (3<= N <= 6) 이 주어진다.
        둘째 줄에는 N 개의 줄에 걸쳐서 복도의 정보가 주어진다. 각 행에서는 N 개의 원소가 주어지며 각 공백으로 구분된다.
        해당위치에 학생이 있다면 S, 선생이 있다면 T, 아무것도 존재하지 않으면 X 가 주어진다. 단, 빈칸의 개수는 항상 3 이상이다
        
Output) 장애물을 3개만 배치하여 모든 학생을 감시에서 피할 수 있는지 여부를 출력한다.

1회차 > 선생과 학생 사이의 좌표값을 얻고 그 좌표값들로 만든 조합을 순회하며 놓았을때 매번 체크를 하는 방식을 채택함
        하지만 오답판정을 받음. 조금 더 찬찬히 뜯어봐야할거같음

'''

# from itertools import combinations


# available = []
# n= int(input())
# data = [[] for _ in range(n)]
# s,t = [],[]
# for i in range(n):
#     data[i] = list(map(str,input().split(' ')))
#     for j in range(n):
#         if data[i][j] == 'S':
#             data[i][j] = 1
#             s.append([i,j])
#         elif data[i][j] == 'T':
#             data[i][j] = 2
#             t.append([i,j])
#         else:
#             data[i][j] = 0

# for i in range(n):
#     x_true = False
#     temp = []
#     for j in range(n):
#         if data[i][j] != 0 and x_true == False:
#             x_true = True
#         elif data[i][j] == 0 and x_true == True:
#             if [i,j] not in available:
#                 temp.append([i,j])
#         elif data[i][j] != 0 and x_true == True:
#             if len(temp) == 0:
#                 x_true = False
#                 continue
#             available = available +temp
#             temp = []
#             x_true = False
#     true = False
#     temp = []
#     for j in range(n):
#         if data[j][i] != 0 and true == False:
#             true = True
#         elif data[j][i] == 0 and true == True:
#             if [j,i] not in available:
#                 temp.append([j,i])
#         elif data[j][i] != 0 and true == True:
#             if len(temp) == 0:
#                 true = False
#                 continue
#             available = available +temp
#             temp = []
#             true = False      

# pos = list(combinations(available,3))

# def check(data,t):
#     for i in t:
#         up,down,left,right = True,True,True,True
#         for j in range(1,n):
#             x,y = i[0],i[1]
#             # 상
#             if -1<x+j<n and up == True:
#                 if data[x+j][y] == 3:
#                     up = False
#                 elif data[x+j][y] == 1:
#                     return False
#             # 하
#             if -1<x-j<n and down == True:
#                 if data[x-j][y] == 3:
#                     down = False
#                 elif data[x-j][y] == 1:
#                     return False
#             # 좌
#             if -1<y-j<n and left == True:
#                 if data[x][y-j] == 3:
#                     left = False
#                 elif data[x][y-j] == 1:
#                     return False
#             # 우
#             if -1<y+j<n and right == True:
#                 if data[x][y+j] == 3:
#                     right = False
#                 elif data[x][y+j] == 1:
#                     return False

#     return True

# def sol(pos,data,t):
#     state = False
#     for a,b,c in pos:
#         data[a[0]][a[1]],data[b[0]][b[1]],data[c[0]][c[1]] = 3,3,3
#         if check(data,t) == True:
#             state = True
#             print('YES')
#             break
#         data[a[0]][a[1]],data[b[0]][b[1]],data[c[0]][c[1]] = 0,0,0
#     if state == False:
#         print('NO')

# sol(pos,data,t)

# # # for i in s:
# # #     x = i[0]
# # #     y = i[1]
# # #     for j in range(n):
# # #         if data[x][j] == 0 and [x,j] not in available:
# # #             available.append([x,j])
# # #         if data[j][y] == 0 and [j,y] not in available:
# # #             available.append([j,y])
# # # available.sort()
# # # n_a = list(combinations(available,3))
# # # print(len(n_a))



'''
2회차 > 1회차의 코드에서 해답의 코드 소스를 조금만 빌려와서 다시 작성해보았다. 시간단축을 위해 s 와 t 사이의 빈칸만 받으려했으나,
        다 받아봐야 1,000 개 언저리이길래 그냥 다 받아서 모든 경우의수를 순회했다.
        우선 정답판정을 받고 시간도 96ms 밖에 소요하지 않았다. 지금 짜놓고 봐도 왜 어제건 안되고 오늘건 되는지 모르겠다
        
'''

# from itertools import combinations


# n= int(input())
# data = [[] for _ in range(n)]
# s,t,el = [],[],[]
# for i in range(n):
#     data[i] = list(map(str,input().split(' ')))
#     for j in range(n):
#         if data[i][j] == 'S':
#             s.append([i,j])
#         elif data[i][j] == 'T':
#             t.append([i,j])
#         else:
#             el.append([i,j])
#             data[i][j] = 'X'
# temp = list(combinations(el,3))
# # n = 3
# # data = [['S','X','X'],['O','X','X'],['T','X','X']]
# # for i in range(n):
# #     for j in range(n):
# #         if data[i][j] == 'S':
# #             s.append([i,j])
# #         elif data[i][j] == 'T':
# #             t.append([i,j])
# #         else:
# #             data[i][j] = 'X'

# def detect(data,t):
#     for x,y in t:
#         u,d,l,r = 0,0,0,0
#         while x-u >=0 :
#             if data[x-u][y] == 'S':
#                 return False
#             elif data[x-u][y] == 'O':
#                 break
#             else:
#                 u += 1
        
#         while x + d < n:
#             if data[x+d][y] == 'S':
#                 return False
#             elif data[x+d][y] == 'O':
#                 break
#             else:
#                 d += 1
        
#         while y - l >=0:
#             if data[x][y-l] == 'S':
#                 return False
#             elif data[x][y-l] == 'O':
#                 break
#             else:
#                 l += 1

#         while y + r < n:
#             if data[x][y+r] == 'S':
#                 return False
#             elif data[x][y+r] == 'O':
#                 break
#             else:
#                 r += 1
        
#     return True
# ck = False
# for i in temp:
#     for j in range(3):
#         data[i[j][0]][i[j][1]] = 'O'
#     if detect(data,t) == True and ck == False:
#         print('Yes')
#         ck = True
#     for j in range(3):
#         data[i[j][0]][i[j][1]] = 'X'
# if ck == False:
#     print('No')


###############################################################################################################
#############################################   Q21 _ 인구 이동   #############################################
###############################################################################################################
'''
Given ) 국경선을 공유하는 두 나라의 인구차이가 L 명이상, R 명 이하라면, 해당 국경선을 하루동안 열어준다
        해당 조건에 의해 열려야 할 국경선이 모두 열린다면, 인구이동이 시작된다
        국경선이 열려있어, 인접칸만을 이용해 이동이 가능하다면, 그 나라를 하루동안은 연합이라 칭한다.
        연합을 이룬 각 칸의 인구수는 (연합 인구수) / (연합을 이루는 칸의 개수) 가 된다. 편의상 소수점은 버린다
        연합을 해체하고, 모든 국경선을 닫는다.

Input ) 첫째 줄에는 N,L,R 이 주어진다. (1 <= N <= 50 , 1 <= (L <= R) <= 100)
        둘째 줄부터 N 개의 줄에 각 나라의 인구수가 주어진다. r행 c 열에 주어지는 정수는 A[r][C] 의 값입니다.( 0<= A[r][c] <= 100)
        인구이동이 발생하는 횟수가 2,000보다 작거나 같은 입력만 주어진다.

Output) 인구이동이 몇번 발생하는지 첫째줄에 출력하라
'''

# from collections import deque
# # n,l,r = 2,20,50
# # data = [[50,30],[30,40]]
# n,l,r = map(int,input().split())
# data = [[] for _ in range(n)]
# for i in range(n):
#     data[i] = list(map(int,input().split()))
# union = [[] for _ in range(n*n)]
# cs = []
# union_count = 0
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# def bfs(data,node,cs):
#     temp = []
#     dx = [0,1,0,-1]
#     dy = [1,0,-1,0]
#     y,x = node[0],node[1]
#     q = deque([[y,x]])
#     while q:
#         [y,x] = q.popleft()
#         temp.append([y,x])
#         for i in range(4):
#             ny,nx = y+dy[i],x+dx[i]
#             if [ny,nx] not in cs:
#                 if 0<=ny<len(data) and 0 <= nx <len(data):
#                     if l <= abs(data[y][x]-data[ny][nx]) <= r:
#                         if [ny,nx] not in temp:
#                             q.append([ny,nx])

#     return temp

# # print(len(bfs(data,[0,0])))

# # data 를 순회
# def openNmove(data,union,union_count):
#     for i in range(n):
#         for j in range(n):
#             if [i,j] not in cs:
#                 if len(bfs(data,[i,j],cs)) > 1 :
#                     union[union_count] = bfs(data,[i,j],cs)
#                     for k in union[union_count]:
#                         cs.append(k)
#                     union_count +=1
    
#     for i in union:
#         if len(i) >1:
#             add = 0
#             for j in i:
#                 add += data[j[0]][j[1]]
#             add = int(add/(len(i)))
#             for j in i:
#                 data[j[0]][j[1]] = add
#     union = []
#     return data,union,union_count

# data,union,union_count = openNmove(data,union,union_count)
# data,union,union_count = openNmove(data,union,union_count)
# # data,union,union_count = openNmove(data,union,union_count)
# # data,union,union_count = openNmove(data,union,union_count)
        
# print(data)

'''
1회차 > 내가 생각해도 좆같이 공부 안했다 제대로좀 하자
        근데 해답 확인해보니 내 구현방향이 아주 틀리진 않았다?
'''

# from collections import deque
# import sys
# input = sys.stdin.readline
# n,l,r = map(int,input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# result = 0

# def process(x,y,index):
#     united = []
#     united.append([x,y])
#     q = deque()
#     q.append((x,y))
#     union[x][y] = index
#     add = graph[x][y]
#     union_count = 1

#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<= nx <n and 0 <= ny < n and union[nx][ny] == -1:
#                 if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
#                     q.append((nx,ny))
#                     union[nx][ny] = index
#                     add += graph[nx][ny]
#                     union_count +=1
#                     united.append((nx,ny))

#     for i,j in united:
#         graph[i][j] = add//union_count
    
#     return union_count

# total = 0

# while True:
#     union = [[-1]*n for _ in range(n)]
#     index = 0
#     for i in range(n):
#         for j in range(n):
#             if union[i][j] == -1:
#                 process(i,j,index)
#                 index +=1
    
#     if index == n*n:
#         break
#     total +=1

# print(total)

###############################################################################################################
###########################################   Q22 _ 블록 이동하기  ############################################
###############################################################################################################

'''
카카오 공채 LV 3의 문제. 조금 더 경험치를 쌓고 다시풀기로 했다.
'''

###############################################################################################################
###############################################   Q23 _ 국영수  ###############################################
###############################################################################################################
'''
Given ) N명의 이름/국어/영어/수학 점수가 주어진다. 주어지는 조건에 따라 성적을 정렬하는 프로그램을 작성하라
        1. 국어점수가 감소하는 순서로
        2. 국어점수가 같으면 영어점수가 증가하는 순서로
        3. 국어와 영어점수가 같으면 수학점수가 감소하는 순서로
        4. 모든 점수가 같다면, 이름이 사전순으로 증가사는 순서로( 단, 아스키코드에서 대문자는 소문자보다 작으므로 
            소문자보다 앞으로 옵니다.)
Input ) 첫째 줄에는 도현이네 반의 학생 수 N(1<= N <= 100,000) 이 주어집니다.
        둘째 줄부터는 한줄에 하나씩 각 학생의 이름,국어/영어/수학 점수가 공백으로 구분해 주어진다.
        점수는 1보다 크거나 같고 100보다 작거나 같은 자연수
        이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.
Output) 문제에 나와있는 정렬기준으로 정렬한 후, 첫째 줄부터 N개의 줄에 걸쳐 학생의 이름 출력
'''
# n = 12
# data = [['Junkyu',50,60,100],['Sangkeun', 80, 60, 50],['Sunyoung',80,70,100],['Soong',50,60,90],['Haebin',50,60,100],['Kangsoo',60,80,100],
# ['Donghyuk',80,60,100],['Sei',70,70,70],['Wonseob',70,70,90],['Sanghyun',70,70,80],['nsj',80,80,80],['Taewhan',50,60,90]]
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = [[] for _ in range(n)]
# for i in range(n):
#     data[i] = list(input().split())
# data.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
# print(data)
# for i in range(n):
#     print(data[i][0])

'''
1회차 > 이전에 한번 sort 의 lambda 함수 사용하는 방법을 봤었으나, 기억 못하고있었음.
        x: (A,B,C,D) 에서 A의 조건을 만족하면 B조건으로 넘어가는 필터링에 대해서 다시한번 기억하게 됨
        그리고 혹시나해서 sorted 와 sort의 시간차이를 확인해본결과 시간은 오히려 sort 가 4ms 만큼 미약하게나마 더 오래걸렸다. 하지만 800kb 가량 메모리를 적게 사용했다.
        뭐 거의 사실상 비슷한 수준이라고 봐도 무방할 듯하다.
'''

###############################################################################################################
###############################################   Q24 _ 안테나  ###############################################
###############################################################################################################
'''
Given ) N 개의 집이 있는 마을에 안테나를 설치하고자 한다. 이 때, 효율성을 위해 안테나에서 모든 집까지의 거리를
        최소로 하는 최적의 위치를 찾고자 한다. 여기서 안테나는 오로지 집에만 설치가 가능하다.
        집들의 위치가 주어질 때, 최적의 위치를 선택하는 프로그램을 작성하라
Input ) 첫째 줄에는 집의 수 N 이 주어진다 (1<= N <= 200,000)
        둘째 줄에는 집의 위치가 공백으로 구분되어 1 이상 100,000 이하의 자연수로 주어진다.
Output) 첫째 줄에 최적의 위치를 출력한다. 만약 여러개의값이 도출된다면 그 중 가장 작은 값을 출력한다.
'''
# import sys
# input = sys.stdin.readline
# n = int(input())
# data = map(int,input().split())
# data.sort()
# print(data[(n-1)//2])



###############################################################################################################
###############################################   Q25 _ 실패율  ###############################################
###############################################################################################################
'''
Given ) 게임에서 스테이지별 실패율을 구하고자 한다.
        스테이지에 도달했으나 아직 클리어하지 못한 플레이어수 / 스테이지에 도달한 플레이어 수
        전체 스테이지 개수 N , 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stage 가 매개변수로
        주어질 때, 실패율이 높은  스테이지부터 내림차순으로 스테이지의 번호가 담긴 배열을 return 하도록 프로그램을 작성하라
Input ) 1<= N <= 500 , 1<= len(stage) <= 200,000 , stage 에는 1 이상 N+1 이하의 자연수가 담겨있다.
        (( 각 자연수는 사용자가 현재 도전중인 스테이지의 번호 // 단 N+1 은 마지막 스테이지(N번째 스테이지)까지 클리어한 사용자))
        실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
        스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 이다.

'''
# n=4
# stage = [1,1,1,1,1,1,1,1,1,1,1]
# stage.sort(reverse=True)
# count = 0
# stage_state = [[0,0,i+1] for i in range(n+1)]
# complete = [[0,i+1] for i in range(n)]

# for i in stage:
#     stage_state[i-1][1] += 1

# for i in range(n,0,-1):
#     count += stage_state[i][1]
#     if i > 0:
#         stage_state[i-1][0] = count
# for i in range(n):
#     if stage_state[i][1] == 0 or (stage_state[i][0]+stage_state[i][1]) == 0:
#         complete[i][0] = 0
#         continue
#     complete[i][0] = (stage_state[i][1]/(stage_state[i][0]+stage_state[i][1]))

# complete.sort(key= lambda x: (-float(x[0]),int(x[1])))

# print(complete)

'''
1회차 > 상당히 쉬운 문제였으나, 내가 0/0 을 고려하지 않아서 오답판정을 받았었다.
'''





###############################################################################################################
############################################   Q26 _ 카드 정렬하기  ###########################################
###############################################################################################################
'''
Given ) 카드 묶음 A 와 B 를 비교후 합치는데에는 len(A) + len(B) 번의 비교가 필요하다.
        10,20,40 의 묶음을 묶고자 할 때 만약 10,20 을 먼저 하고 30,40 을 합칠경우 30+70 이지만,
        10,40 을 묶은 후 50,20 을 하면 120 이 되는, 비효율적인 방법인 것이다. 따라서 N 개의 카드묶음 크기가 각각 주어질 때
        최적의 비교횟수를 구하는 프로그램을 작성하라.
Input ) 첫째 줄에 N 이 주어진다. ( 1<= N <= 100,000 ) 이어서 N 개의 줄에 걸쳐 숫자카드 묶음의 각각의 크기가 주어진다.
Output) 첫째 줄에 최소 비교 횟수를 출력한다.

1회차 > 단순 리스트로 계산하고자 했으나, 시간초과판정을 받았다.
        따라서 전에 배웠던 우선순위 큐 heapq 를 사용하여서 정답판정을 받았음.
        우선순위큐는 가장 높은 우선순위(파이썬에서는 최소값) 이 가장 앞에 정렬되는 큐다.
'''
# import heapq
# import sys
# input = sys.stdin.readline
# n = int(input())
# heap = []
# for i in range(n):
#     data = int(input())
#     heapq.heappush(heap, data)
# result = 0
# while len(heap) != 1:
#     a,b = heapq.heappop(heap),heapq.heappop(heap)
#     add = a+b
#     result += add
#     heapq.heappush(heap, add)

# print(result)



###############################################################################################################
##################################   Q27 _ 정렬 배열에서 특정수의 개수 구하기  ################################
###############################################################################################################
'''
Given ) N 개의 원소를 포한하는 오름차순 정렬 수열이 있다. 여기서 x 가 등장하는 횟수를 구하라
        여기서 시간복잡도는 O(logN) 으로 설계하지 않는다면, 시간초과 판정을 받습니다.
Input ) 첫째 줄에 N 과 x 가 정수형태로 공백으로 구분되어 입력 (1 <= N <= 1,000,000)
        둘째 줄에는 N 개의 원소가 정수형태로 공백으로 구분되어 입력됨.
Output) 수열에서 값이 x 인 원소의 개수 출력 하나도 없다면, -1 출력
'''

# data = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
# n,x = len(data),3
# def bisec_MtoE(data,x,start,end):
#     if  data[end-1] == x:
#         return end
#     half =(start+end)// 2
#     if data[half] == x and data[half+1] > x :
#         return half
#     elif data[half] == x and data[half+1] == x :
#         return bisec_MtoE(data,x,half,end)
#     elif data[half] > x and data[half+1] > x :
#         return bisec_MtoE(data,x,start,half)

# def bisec_StoM(data,x,start,end):
#     if data[start] == x:
#         return start
#     half =(start+end)// 2
#     if data[half] == x and data[half-1] < x :
#         return half
#     elif data[half] == x and data[half-1] == x :
#         return bisec_StoM(data,x,start,half)
#     elif data[half] < x and data[half-1] < x :
#         return bisec_StoM(data,x,half,end)

# def main_bisec(data,x,start,end):
#     half =( start+end )// 2
#     if data[half] < x:
#         return main_bisec(data,x,half,end)
#     elif data[half] > x:
#         return main_bisec(data,x,start,half)
#     elif data[half] == x:
#         return half

# mid = main_bisec(data,x,0,n)
# MtoE = bisec_MtoE(data,x,mid,n)
# StoM = bisec_StoM(data,x,0,mid)
# print(MtoE)
# print(StoM)
# print(data[StoM-1:MtoE+2])


'''
1회차 > 직접 이분탐색 함수를 짜보려했으나, 귀찮아서 그냥 bisect라이브러리를 가져옴.
        bisect 라이브러리 또한 O(logN)의 시간복잡도를 가지므로, 문제가 제시하는 제한사항을 만족하며
        문제를 풀어낼 수있다.
'''


# import bisect
# data = [1,1,2,2,2,2,3]
# n,x = len(data),2
# left,right = bisect.bisect_left(data,x),bisect.bisect_right(data,x)
# if data[left] != x:
#     print(-1)
# else:
#     print(right-left)



###############################################################################################################
#############################################   Q28 _ 고정점 찾기  ############################################
###############################################################################################################
'''
Given ) 고정점이란 수열의 원소 중 그 값이 인덱스값과 같은 원소를 지칭한다.
        하나의 수열이 N 개의 원소를 포함하며, 모든 원소가 오름차순으로 정렬되어있다. 이 때 수열에서 고정점이 있다면
        고정점을, 없다면 -1 일 출력하는 프로그램을 작성하라. 시간복잡도가 O(logN) 으로 설계하지 않으면 시간 초과판정
        을 받는다.

Input ) 첫째 줄에 N 이 입력된다.(1 <= N <= 1,000,000)
        둘째 줄에 N 개의 원소가 정수 형태로 공백으로 구분되어 입력된다. (-1e9 <= X <= 1e9)

Output) 고정점이 있다면 고정점, 없다면 -1 출력
'''

'''
1회차 > 고정점은 단 1개 존재한다. 또한 O(logN)의 시간복잡도와 이미 정렬되어있는 수열은 이분탐색을 의미한다고 생각한다.
        절반지점이 인덱스값보다 큰 원소값을 가진다면 왼쪽으로 이분탐색 작다면 오른쪽으로 이분탐색 하는 알고리즘을 짜보자
'''
# n = 5
# data = [-15,-6,1,3,7]

# def binary_search(array,start,end):
#     if start == end and array[start] != start:
#         return -1
#     half = (end+start)//2
#     if array[half] == half:
#         return half
#     elif array[half] > half:
#         return binary_search(array,start,half-1)
#     elif array[half] < half:
#         return binary_search(array,half+1,end)

# print(binary_search(data,0,n-1))

'''
1회차 > 생각대로 잘 풀렸다. 하지만 이러문제는 채점해주는 사이트가 없어서 살짝 아쉽다.
'''



###############################################################################################################
#############################################   Q29 _ 공유기 설치  ############################################
###############################################################################################################
'''
Given ) 수직선 위에 N 개의 집이 있다. C 개의 공유기를 공유기간 거리를 최대로 하여 설치하고자 한다.
        C개의 공유기를 설치하는 공유기간거리 최댓값은 얼마인가 구하는 프로그램을 작성하라
Input ) 첫째 줄에 집의 개수 N(2<= N <= 200,000)과 공유기의 개수 C(2<= C <=N)가 하나의 빈칸으로 구분되어 주어짐
        둘째 줄 부터는 N 개의 줄에 집의 촤표를 나타내는 Xi ( 1<= Xi <= 1e9) 가 한줄에 하나씩 주어짐
Output) 가장 인접한 두 공유기 사이의 최대거리를 출력하라        

'''

'''
1회차 > 보통 1 부터 순회하며, 해당 거리를 찾겠지만 해답에서는 우선 1/2거리부터 시작하여 이진탐색으로 최대거리를 찾고자한다
        만약 작은 크기의 거리라면 내 처음생각대로 1부터 순회하는것이 맞겠지만, 이 문제에선 집의 좌표가 최대 1e9 이므로
        이진탐색의 속도가 더 빠르기에 해당 방법을 사용한것이 아닌가 싶다.
'''
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# data = [0 for _ in range(n)]
# for i in range(n):
#     data[i] = int(input())
# data.sort()

# start = 1
# end = data[-1]- data[0] 
# result = 0

# while start <= end:
#     mid = (start+end) // 2
#     value = data[0]
#     count = 1
#     for i in range(1,n):
#         if data[i] >= value + mid:
#             value = data[i]
#             count +=1
    
#     if count >= m:
#         start = mid+1
#         result = mid
#     else:
#         end = mid -1
    
# print(result)
# print(data)


###############################################################################################################
##############################################   Q30 _ 가사 검색   ############################################
###############################################################################################################
'''
Given ) data 에 '?' 가 포함된 패턴형태의 문자열이 몇개  있는가 찾는 프로그램을 작성하라
        '?'는 글자 하나를 의미하며 어떤 문자에도 매치된다. 예를들어 'fro??'는 'frodo','front' 에는 매치되나,
        'frozen','frame'에는 매치되지 않는다.
        키워드가 담긴 배열 queries 가 주어질 때 각 키워드별로 매치되는 단어의 수를 순서대로 배열에 답아 반환하는
        함수를 작성하라
Input ) words 의 길이는 2 이상 100,000 이하이다.
        각 가사단어의 길이는 1 이상 10,000 이하로 빈 문자열은 없다.
        전체 가사단어 길이의 합은 2 이상 1,000,000 이하입니다.
        가사에 동일한 단어가 중복될경우 중복을 제거하거, words 에는 하나로만 제공됨
        각 가사단어는 오직 알파벳 소문자로만 구성되며, 특수문자나 숫자는 포함하지 않음
        검색키워드는 중복될 수 있음

'''

data = ['frodo','front','frost','frozen','frame','kakao','froco']
n = 2
data.sort(key= lambda x : (x[-i] for i in range(n)))
print(data)