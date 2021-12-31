from collections import deque
from functools import partial, partialmethod
from os import error, spawnl
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


############################################  Q1 _ 모험가 길드  ############################################
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

############################################  Q2 _ 곱하기 혹은 더하기  ############################################
'''
Given ) 정수로 이루어진 문자열 S 가 주어짐 // 1 <= S <= 20 
        문자열은 왼쪽으로부터 순서대로 * 혹은 + 로 계산됨 그 중에서 만들 수 있는 가장 큰 값을 출력하라
1회차 > 그리디 알고리즘
'''

# # data = input()
# data = '02984'
# final = 0

# for i in range(len(data)-1):
#     if i == 0:
#         s = int(data[i]) + int(data[i+1])
#         m = int(data[i]) * int(data[i+1])
#         value = max(s,m)
#         final+=value
#     else:
#         s = final + int(data[i+1])
#         m = final * int(data[i+1])
#         value = max(s,m)
#         final = value

# print(final)



############################################  Q3 _ 문자열 뒤집기  ############################################
# data = input()
# if data[0] == '0':
#     count_1 = 0
#     count_0 = 1
# elif data[0] == '1':
#     count_1 = 1
#     count_0 = 0

# for i in range(len(data)-1):
#     if data[i] == '0' and data[i+1] == '1':
#         count_1 +=1
#     elif data[i] == '1' and data[i+1] == '0':
#         count_0 +=1
    
# print(min(count_0,count_1))
    

############################################  Q4 _ 만들 수 없는 금액  ############################################
'''
Given ) 동전의 수 : N // 1 <= N <= 1,000
Input ) 동전의 개수 N 입력 후 동전의 단위 N개 입력
Output) 해당 동전들로 만들 수 없는 최솟값

1회차 > 그리디
'''
# n = 5
# data = [1,2,3,3]
# data.sort(reverse=True)
# index = max(data)
# target = 0

# while True:
#     target +=1
#     v = target
#     for i in range(len(data)):
#         if v >= data[i]:
#             v -= data[i]
#     if v !=0:
#         print(target)
#         break

'''
1회차 > 분명 이 코드가 아닌데 잘 된다. 조금 더 공부하고 다시 돌아보자
'''


############################################  Q5 _ 볼링공 고르기 ############################################
'''
Given ) A 와 B 두 사람이 볼링을 치고있다. 두 사람은 각자 다른 무게의 볼링공을 고르고자 한다
        볼링공은 총 N 개 있으며 그 무게는 1~M 사이의 자연수이다. 이 두 사람이 고를 수 있는 볼링공 번호의 조합은?
Input ) 첫째 줄에 볼링공 개수 N , 최대무게 M 이 공백으로 구분되어 자연수 형태로 주어짐 ( 1 <= N <= 1,000 // 1 <= M <= 10)
        둘째 줄에는 각 볼링공의 무게 K 가 공백으로 구분되어 자연수로 주어짐
Output) 두 사람이 볼링공을 고르는 경우의 수 int
'''
# # data = [1,5,4,3,2,4,5,2]
# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
# count = 0
# for i in range(len(data)):
#     for j in range(i,len(data)):
#         if data[i] == data[j]:
#             continue
#         elif data[i] != data[j]:
#             count +=1

# print(count)

'''
1회차 > 좀 쉬운데? 해답은 나랑 좀 다르긴 하지만 비슷한 방식이었다.
'''

############################################  Q6 _ 무지의 먹방 라이브!  ############################################
'''
이름 귀엽네 ㅋㅋ
Given ) 무지에게는 먹어야 할 음식 N 개가 있다. 각 음식에는 1 ~ N 까지의 번호가 붙어있으며, 각 음식마다 섭취 소요시간이 있다.
        무지는 다음과 같은 방법으로 음식을 섭취한다
        1 ) 무지는 1번부터 N 번으로 순서대로 회전판에 의해 음식을 섭취한다.
        2 ) 원형 회전판으로 N 번 음식을 섭취 한 후에는 1번이 다시 돌아온다
        3 ) 무지는 1초동안 해당 음식을 섭취하고 남은 것은 그대로 둔 채, 다음 음식을 섭취한다. 여기서 다음 음식은 아직 남은 음식 중 
            가장 가까운 번호의 음식이다
        4 ) 회전판이 음식을 가져오는 데에는 시간이 소요되지 않음

        먹방이 시작 한 뒤 K 초 뒤에 방송이 잠시 중단되어 다음으로 먹어야 하는 음식의 번호를 알고싶다.

        food_times 의 길이는 1 이상 2,000 이하
        food_times 의 원소른 1 이상 1,000 이하의 자연수
        k 는 1 이상 2,000,000 이하의 자연수이다.
'''
# n = 3
# food_times = [3,1,2]
# k = 5
# def sol(food_times, k):
#     answer = 0
#     while True:
#         for i in range(len(food_times)):
#             if k == 0 and food_times[i] != 0:
#                 answer = i+1
#                 return answer
#             if food_times[i] !=0:
#                 food_times[i] -=1
#                 k -=1

'''
1회차 > 기본적인 그리디 알고리즘으로 구현했고 간단한 n = 3 일땐 통과를 했으나, 효율성 테스트에서 실패. 해답을 보고 큐를 이용해보고자 함.
'''