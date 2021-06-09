from collections import deque
from functools import partial, partialmethod
from os import error, spawnl
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


############################################  모험가 길드  ############################################
'''
Given ) 모험가의 수 : N //  최대 공포도 X == 해당 모험가의 그룹원 수 X // 1< N <100,000
Input ) 첫째 줄에 모험가의 수 N 입력 // 둘째 줄에 공포도를 입력
1회차 > 그리디 알고리즘 사용
'''

# # n = int(input())
# # data = list(map(int,input().split()))
# n=5
# data = [2,3,1,2,2]
# group = 0
# data.sort(reverse=True)

# def grouping(index):
#     global group
#     if index < len(data):
#         v = index + data[index]
#         group +=1
#         grouping(v)

# grouping(0)
# print(group)

############################################  곱하기 혹은 더하기  ############################################
'''
Given ) 정수로 이루어진 문자열 S 가 주어짐 // 1 <= S <= 20 
        문자열은 왼쪽으로부터 순서대로 * 혹은 + 로 계산됨 그 중에서 만들 수 있는 가장 큰 값을 출력하라
1회차 > 그리디 알고리즘
'''

# data = list(map(int,input()))
# final = 0

# def max_value(final,index):
#     if int(data[index+1]) is not int:
#         return
#     else:
#         S = data[index] + data[index+1]
#         M = data[index] * data[index+1]
#         value = max(S,M)
#         final += value
#         max_value(final,index)
#         index+=1
    
#     return value

# for i in range(len(data)-1):
#     data[i+1] = max_value(i)
#     final = data[i+1]

# max_value(final,0)
# print(final)

# print(final)

# data = input()
# print(int(data[0]))
# print(data)


############################################  문자열 뒤집기  ############################################
data = input()
if data[0] == '0':
    count_1 = 0
    count_0 = 1
elif data[0] == '1':
    count_1 = 1
    count_0 = 0

for i in range(len(data)-1):
    if data[i] == '0' and data[i+1] == '1':
        count_1 +=1
    elif data[i] == '1' and data[i+1] == '0':
        count_0 +=1
    
print(min(count_0,count_1))
    