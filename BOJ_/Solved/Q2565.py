from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2565
#######  TODAY  #######
##### 2022. 05. 30 #####
GIVEN ) 두 전봇대 사이 전깃줄을 추가하다 보니 교차하는 경우가 발생하여 교차하는 전깃줄을 없애고자 한다
        교차하는 전깃줄이 없도록 제거해야 할 전깃줄의 최소 갯수를 구하라
INPUT ) 첫째 줄에 전깃줄의 갯수가 주어진다. 전깃줄의 개수는 100 이하의 자연수.
        둘째 줄부터 한줄에 하나씩 A와 B 전봇대가 연결되는 위치정보가 주어진다. 각 위치정보는 500 이하의 자연수이며,
         같은 위치에 둘 이상의 전깃줄은 연결되지 않는다.
OUTPUT) 첫째 줄에 남아있는 모든 전깃줄이 교차하지 않게 없애야하는 전깃줄의 최소개수를 출력하라
Approach )  LIS 알고리즘 사용

'''
# import sys
# input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append([a,b])
data.sort()
X = [i[1] for i in data]
index = 0
dp = [0]

for i in X:
    if dp[index]<i:
        dp.append(i)
        index +=1
        continue
    for j in range(index,-1,-1):
        if dp[j] < i:
            dp[j+1] = i
            break
        
print(N-index)