from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2230
#######  TODAY  #######
##### 2022. 07. 29 #####
GIVEN ) N 개의 정수로 이루어진 리스트가 주어진다.
        이 수열에서 두 수를 골라서 그 차이가 M 이상이면서 가장 작은 경우를 출력하라
INPUT ) 첫째 줄에 두 정수 N,M 이 주어진다. ( 100,000 이하의 자연수 N, 0<= M <=2,000,000,000)
        그 다음 N 개 줄에 걸쳐 10억 이하의 원소가 주어진다
OUTPUT) M 이상이면서 가장 작은 차이를 출력하라
Approach )  머리와 꼬리 포인터를 사용해서 풀어내자
'''
import sys
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

n,m = list(map(int,input().split()))
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
res = 1e10
h,t = 0,1
# value = [0 for _ in range(n)]

while True:
    d = lst[t]-lst[h]
    if d < m:
        if t < n-1:
            t += 1
        else:
            h += 1
            if h == t:
                break
    elif d > m:
        res = min(d,res)
        h +=1
        if h == t:
            if t < n-1:
                t +=1
            else:
                break
    elif d == m:
        res = m
        break
print(res)


'''
깔끔하게 1트
'''