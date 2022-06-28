from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q11404
#######  TODAY  #######
##### 2022. 06. 28 #####
GIVEN ) n ( 100 이하의 자연수 )개의 도시와 m(10만 이하의 자연수) 개의 버스가 있다.
        각 버스는 도시사이를 연결하며 소요 비용은 정해져있다.
        각 도시간의 최소비용을 구하는 프로그램을 작성하라
INPUT ) 첫째 줄에 n , 둘째 줄에 m 이 주어지며
        셋째줄부터 m+2 번째 줄까지 버스의 정보가 주어진다.
        시작 a 도착 b 비용 c 로 이루어지며 시작==도착의 경우는 없다.
        비용은 10만 이하의 자연수이며, 각 노선은 하나 이상일 수 있다.
OUTPUT) 최소비용을 출력하고 갈수없다면 0 을 출력하라
Approach ) 플로이드워셜
데이터 = N*N 크기 행렬

'''
import sys
sys.setrecursionlimit(25000)
# input = sys.stdin.readline


inf = 1e9
N = int(input())
m = int(input())
A = []
for _ in range(m):
    A.append(list(map(int,input().split())))
data = [[inf]*N for _ in range(N)]
for x,y,z in A:
    data[x-1][y-1] = min(data[x-1][y-1],z)

for i in range(N):
    for j in range(N):
        for k in range(N):
            if k == j:
                data[j][k] = 0
            else:
                data[j][k] = min(data[j][k],data[j][i]+data[i][k])

for i in data:
    for j in i:
        if j == inf:
            j = 0
        print(j,end=' ')
    print()

