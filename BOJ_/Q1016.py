import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1016
#######  TODAY  #######
##### 2022. 10. 13 #####
GIVEN ) 어떤 정수 X 가 1보다 큰 제곱수로 나누어떨어지지 않을 때 그 수를 제곱 ㄴㄴ 수라고 한다.
        min & max 값이 주어지면 min보다 크거나 같고 max 보다 작거나 같은 제곱 ㄴㄴ수가 몇개 있는지 출력한다.
INPUT ) 첫째 줄에 MIN & MAX 값이 주어진다.
OUTPUT) 첫째 줄에 MIN 보다 크거나 같고 MAX 보다 작거나 같은 제곱 ㄴㄴ 수의 개수를 출력하라
Approach )  에라토스테네스의 체 응용
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
MIN, MAX = list(map(int, input().split()))

length = MAX - MIN + 1
dic = {i: True for i in range(MIN, MAX+1)}


for number in range(2, 2000000):
    now = number**2
    if now > MAX:
        break
    i = MIN//now
    while now*i <= MAX:
        if now*i >= MIN and dic[now*i]:
            dic[now*i] = False
            length -= 1
        i += 1

print(length)

'''
short coding . . .
'''
