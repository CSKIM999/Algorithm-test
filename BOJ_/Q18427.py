from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q18427
#######  TODAY  #######
##### 2022. 06. 14 #####
GIVEN ) N명의 학생이 최대 M 개의 블럭을 갖고 H높이의 탑을 쌓고자 한다.
        높이가 정확히 H인 탑을 만들 수 있는 경우의 수를 계산하라
INPUT ) 첫째 줄에 N,M,H 가 공백을 기준으로 주어진다.
        ( 1<= N <= 50, 1<= M <= 10, 1<= H <= 1,000)
        둘째 줄부터 각 학생이 가진 블럭의 높이가 공백을 기준으로 주어진다.
OUTPUT) H 높이의 탑을 만드는 경우의 수를 10,007로 나눈 나머지를 출력하라
Approach ) 냅색 알고리즘을 사용하되, 데이터 처리가 관건일듯  
'''
import sys
sys.setrecursionlimit(25000)
# input = sys.stdin.readline


N,M,H = map(int,input().split())
data = {}
for i in range(N):
    temp = list(map(int,input().split()))
    for x in temp:
        try:
            data[x].append(i)
        except KeyError:
            data[x] = [i]
print(data)
dp = [[[0] for _ in range(H)] for _ in range(N+1)]
xprint(dp)