from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2011
#######  TODAY  #######
##### 2022. 03. 04 #####
GIVEN ) 암호가 주어질 때 가능한 경우의 수를 모두 구하라

INPUT ) 첫째 줄에 5000자리 이하의 암호가 주어진다
OUTPUT) 경우의 수를 1000000으로 나눈 나머지를 출력하라
Approach )  1개 연속 2 개연속의 경우의 수는 피보나치 1,2,3,5,8 라는것을 알았다
            또한 비연속 경우의 수는 곱셈이다 "52166111" 의 경우 dp[3]*dp[3] 이 되는것
            피보나치만 만들어보자

            해보니 0 의 경우가 문제임
            앞에 1 혹은 2 가 오지 않는 0 의 경우 잘못된 암호
            또는 1 혹은 2가 오는 0의 경우 연속수를 끊음
            2 인 경우 6까지만 유효숫자

'''
# import sys
# input = sys.stdin.readline
key = 1000000
dp = [0]*5001
dp[1],dp[2] = 1,2
for i in range(3,5001):
    dp[i] = dp[i-1]+dp[i-2]
x = list(str(input().strip()))
c = 1
flag = False
temp = []
for k in range(len(x)):
    i = x[k]
    if 1<=int(i)<=2:
        c+=1
        flag = True
    elif int(i) == 0:
        if k==0 or not 1<=int(x[k-1])<=2:
            flag = False
            temp = [0]
            break
        if c>2:
            c -= 2
        else:
            c=1
        temp.append(c)
        c = 1
        flag= False
    else:
        if 6<int(i) and k>0 and x[k-1]=='2':
            c-=1
        if flag:
            temp.append(c)
        c = 1
        flag = False
if flag:
    temp.append(c-1)
elif not temp and len(x) > 0:
    temp.append(1)
result = 0
if temp[0] != 0:
    result = dp[temp[0]]
    for t in temp[1:]:
        if t>100:
          for i in range(len(dp),t+1):
            dp[i] = dp[i-1]+dp[i-2]
        result *= dp[t]

print(result%key)

'''
이 붕신같은문제 03 입력값이 [0,3] 이 아니라 [3] 으로 들어와서 자꾸 오류났던 것
사실상 1시간전에 다 푼건디 ㅅㅂ
'''