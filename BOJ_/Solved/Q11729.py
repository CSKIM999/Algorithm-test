from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q11729
#######  TODAY  #######
##### 2022. 03. 10 #####
GIVEN ) 하노이 탑 문제
        첫번째 장대에 있는 원판들을 모두 순서에 맞게 3번째 장대로 옮겨라
INPUT ) 원판의 갯수가 주어짐
OUTPUT) 첫째 줄에 총 이동횟수
        둘째 줄부터 이동내역을 출력하라
Approach )  대표적인 재귀문제라고 함 찾아보고 따라해보자  
https://shoark7.github.io/programming/algorithm/tower-of-hanoi << 참고링크 하노이 탑 재귀문제 아주 잘 설명해놓음
'''
# import sys
# input = sys.stdin.readline

n = 3

'''
각 문제를 분해하면 다음과같다
1. N-1 의 원판을 2번으로 옮긴다
2. N 의 원판을 3으로 옮긴다
3. N-1 의 원판을 3으로 옮긴다
원판의 갯수가 1 이상인 경우 모두 해당된다

더 세부화하자면
N-1 의 원판을 3번을 제외한 장대를 경유하여 3번으로 이동시킨다.

'''
n = int(input())
tower = [[i+1 for i in range(n)],[],[]]
hist = []
def move(N,s,t):
    tower[s].pop()
    tower[t].append(N)
    hist.append([s,t])
def hanoi(N,s,v,t):
    if N ==1:
        move(1,s,t)
    else:
        hanoi(N-1,s,t,v)
        move(N,s,t)
        hanoi(N-1,v,s,t)
hanoi(n,0,1,2)
print(len(hist))
for a,b in hist:
    print(f"{a} {b}")
