import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2096
#######  TODAY  #######
##### 2023. 03. 02 #####
GIVEN ) DP 내려가기
        한 줄에는 3칸이 존재하며
        다음줄로 넘어갈 때, 현재 index와 +- 1 까지의 인덱스로만 이동할 수 있다.
        맨 밑줄에 도달했을때 얻을 수 있는 최댓값과 최솟값을 출력하라
INPUT ) 첫째 줄에 줄의 갯수 N ( 10만 이하의 자연수 )
        이후 N 개 줄에 걸쳐 각 줄에 위치한 칸의 점수가 공백을 구분으로 출력된다 ( 0 ~ 9 )
OUTPUT) 최대, 최솟값을 공백으로 구분하여 출력하라
Approach ) DP  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dummy = [[0, 1e9], [0, 1e9], [0, 1e9]]
dp = [[[0, 0], [0, 0], [0, 0]], [[0, 1e9], [0, 1e9], [0, 1e9]]]


def setDP(i, j):
    dp[1][j][0] = max(dp[1][j][0], dp[0][j][0] + table[i][j])
    dp[1][j][1] = min(dp[1][j][1], dp[0][j][1] + table[i][j])
    if j-1 <= 0:  # index = 0
        dp[1][j+1][0] = max(dp[1][j+1][0], dp[0][j][0] + table[i][j])
        dp[1][j+1][1] = min(dp[1][j+1][1], dp[0][j][1] + table[i][j])
    if j-1 >= 0:
        dp[1][j-1][0] = max(dp[1][j-1][0], dp[0][j][0] + table[i][j])
        dp[1][j-1][1] = min(dp[1][j-1][1], dp[0][j][1] + table[i][j])


for i in range(n):
    for j in range(3):
        setDP(i, j)
    if i != n-1:
        dp = [[k[:] for k in dp[1]], [k[:] for k in dummy]]

answer = [0, 1e9]
for i in range(3):
    a, b = dp[-1][i]
    answer = [max(answer[0], a), min(answer[1], b)]
print(f"{answer[0]} {answer[1]}")

'''
원래 n만큼의 dp테이블을 만들었지만 메모리 제한이 4mb 여서
2행짜리 dp테이블로 변환.

사실상 dp를 가장한 누적합 문제 아님?
메모리 제한이 인상적이었던 문제.
'''
