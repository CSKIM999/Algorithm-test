from collections import deque
from functools import partial
from itertools import combinations
# array = [5,7,9,0,3,1,6,2,4,8]
# end = len(array)-1
# right = end
# print(array[end])
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

# data ='abcabcabcabcdedededededee'
# code = ''
# code = data[0]+data[1]
# print(type(code))
# min_len = len(data)
# print(int(len(data)/2))
# half_num = int(len(data)/2)
# for i in range(2,half_num):
#     for j in range(i):
#         lst = 


# n = input()
# k = input()
# for i in range(k):
#     k_map = 

# L = input()
# L_Time = [(8,'D'),(10,'D'),(11,'D'),(13,'L')]
# k_map = []
# k=2
# for i in range(k):
#     a,b = map(int, input().split(' '))
#     k_map.append((a,b))
# print(k_map)

# N,m = 5,3
# kfc,house = [],[]
# Input = [[0,0,1,0,0],[0,0,2,0,1],[0,1,2,0,0],[0,0,1,0,0],[0,0,0,0,2]]
# for i in range(N):
#     for j in range(N):
#         if Input[i][j] == 1:
#             house.append([i,j])
#         elif Input[i][j] == 2:
#             kfc.append([i,j])

# print(kfc)

# c = list(combinations(kfc,1))

# print(1e9)
# # for i,j in enumerate(range(3,-1,-1)):
#     print(i,j)
index = 2
for i in range(index):
    for j in range(-index+1,0):
        print(i,j)