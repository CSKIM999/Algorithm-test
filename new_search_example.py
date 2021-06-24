from collections import deque

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

n = 10
k = 4
k_map = [(1,2),(1,3),(1,4),(1,5)]
L = 4
L_Time = [(8,'D'),(10,'D'),(11,'D'),(13,'L')]
#  OUTPUT = 21
time_count = 0
snake = [0,0]
queue = deque()
queue.appendleft(snake)
snake = [1,0]
queue.appendleft(snake)

direction = 0
direction_option = 1
table = [[0]*(n) for _ in range(n)]
for i in k_map:
    table[i[0]-1][i[1]-1] = 1

# while snake[0]== n or snake[0] <0 or snake[1] == n or snake[1] < 0:
#     time_count +=1
#     # if table[snake[0]][snake[1]] ==2:
#     snake[direction] += direction_option
#     queue.appendleft(snake)
#     table[snake[0]][snake[1]] += 1

#     pass


    
    


print(queue)
print([1,0] in queue)