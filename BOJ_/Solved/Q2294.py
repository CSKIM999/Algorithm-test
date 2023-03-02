import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2294
#######  TODAY  #######
##### 2023. 03. 02 #####
GIVEN ) 동전 2
        n가지 종류의 동전이 존재한다.
        해당 동전들을 사용하여 k라는 값을 만들고자 한다.
        같은 가치의 동전이 여러가지 주어질 수 있다.
INPUT ) 첫째 줄에 동전의 종류 n 은 100 이하의 자연수와 만들고자 하는 값 k 는 10,000 이하의 자연수
        그 이후 n개 줄에 걸쳐 동전의 가치가 주어진다 동전의 가치는 100,000 이하의 자연수
        중복가치의 동전이 주어질 수 있다.
OUTPUT) 동전을 최소한으로 사용하여 k를 만들 때 동전의 갯수를 구하라
        불가능한 경우 -1 을 출력하라
Approach )  dp.
'''
sys.setrecursionlimit(25000)

input = sys.stdin.readline
n, k = map(int, input().split())
arr = set()
for _ in range(n):
    arr.add(int(input()))
arr = list(arr)
arr.sort()
n = len(arr)
dp = [2e5 if i > 0 else 0 for i in range(k+1)]
for i in range(n):
    now = arr[i]
    for i in range(k+1):
        if i >= now:
            dp[i] = min(dp[i], dp[i-now]+1)
result = dp[-1]
if result == 2e5:
    print(-1)
else:
    print(result)
