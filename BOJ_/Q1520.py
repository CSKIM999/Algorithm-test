from lib import xprint,Prepare_Coding_Test
import sys
sys.setrecursionlimit(25000)
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1520
#######  TODAY  #######
##### 2022. 05. 31 #####
GIVEN ) 직사각형 모양의 지도를 참고하여 산을 내려가고자 한다. 각 칸에는 해당 지점의 높이가 주어지며 
        무조건 현재보다 높이가 더 낮은 지점으로만 이동하여 목표 지점으로 이동하고자 한다.
        상하좌우로 인접한 행렬로만 이동이 가능하며 왼쪽 위부터 오른쪽 아래로 이동하고자 한다.
        항상 내리막으로만 이동하는 경로의 개수를 구하라
INPUT ) 첫째 줄에 세로의 크기 M, 가로의 크기 N 이 공백을 구분으로 주어진다. ( 1<= M,N <= 500 )
        이어 다음 M 개의 줄에 걸쳐 한줄에 N 개씩의 원소(높이) 가 공백을 구분으로 주어진다. ( 1<= E <= 10,000 )
OUTPUT) 이동 가능한 경로의 수 H 를 출력하라
'''
# import sys
# input = sys.stdin.readline


n,m = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
dd = [[1,0],[0,1],[-1,0],[0,-1]]
def dfs(now):
    global dp
    x,y = now
    nowValue = data[x][y]
    for i in range(4):
        nx,ny = x+dd[i][0],y+dd[i][1]
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny] < nowValue:
                dp[nx][ny] += 1
                dfs([nx,ny])
    if (now != [n-1,m-1]) and (now != [0,0]):
        count = 0
        for j in range(4):
            nx,ny = x+dd[j][0],y+dd[j][1]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny] < nowValue and dp[nx][ny] >= 0:
                    count += 1
        if not count:
            dp[x][y] = -1
            
dfs([0,0])
xprint(data)
xprint(dp)