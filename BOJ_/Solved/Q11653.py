from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q11653
#######  TODAY  #######
##### 2022. 03. 11 #####
GIVEN ) N의 소인수를 구하라 1이라면 무시해도된다
INPUT ) N 이 주어진다
OUTPUT) N 의 소인수를 한줄씩 출력하라
'''
# import sys
# input = sys.stdin.readline
n = int(input())
while True:
    if n == 1:break
    c = 2
    while True: 
        if n%c == 0: print(c);n = n//c;break
        c+=1