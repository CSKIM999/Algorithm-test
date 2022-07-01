from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1984
#######  TODAY  #######
##### 2022. 06. 30 #####
GIVEN ) 세로 R 칸, 가로 C 칸으로 이뤄진 보드가 있고 각 칸에는 알파벳이 하나씩 적혀있다.
        말은 상하좌우 인접 한칸만 이동 가능하지만, 지금까지 방문한 적 없는 알파벳이어야만 한다.
        좌측 상단 0,0 에서 시작해서 최대 몇칸까지 이동할 수 있는지 출력하라.
INPUT ) 첫째 줄에 R 과 C 가 빈칸을 구분으로 주어진다. (R과 C 는 20 이하의 자연수)
        이후 R개의 줄에 걸쳐 C 개의 대문자 알파벳들이 빈칸없이 주어진다.
OUTPUT) 이동 가능한 최대 칸수를 출력하라
Approach )  멀리가는거니까 dfs 괜찮을듯?
A-Z 를 문자열로 쓰고 for 문 돌려서 딕셔너리로 만들기

ABCDEFGHIJKLMNOPQRSTUVWXYZ

비트마스킹으로 갈까?

맵데이터는 숫자딕셔너리 2차원행렬화

함수 dfs(지금,기록,카운트)
    글로벌 결과

    만약 지금 카운트가 결과보다 크다면?
        결과 = 카운트

    x,y = 지금 
    for 4방향
        nx,ny

        만약 nx,ny가 테이블 안에 있다면
            num = table[nx][ny]
            만약 not 기록[num] 이라면
                temp = 기록[:]
                temp[num] = 1
                dfs([nx,ny],temp[:],카운트+1)
            
    return
    

'''

import sys
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
dic = {}
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = len(a)
for i in range(n):
    dic[a[i]] = i
r,c = map(int,input().split())
dp = [[0 for _ in range(c)] for _ in range(r)]
data = []
for _ in range(r):
    data.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        data[i][j] = dic[data[i][j]]

hst = [0]*n
hst[data[0][0]] = 1
d = [[0,1],[0,-1],[1,0],[-1,0]]
C = 1
def dfs(now,hist,count):
    global C,dp
    if count > C:
        C = count
    if C == 26:
        return
    x,y = now
    for w in range(4):
        nx,ny = x+d[w][0],y+d[w][1]
        if 0<= nx < r and 0<=ny<c:
            nxtnum = data[nx][ny]
            if not hist[nxtnum]:
                temp = hist[:]
                temp[nxtnum] = 1
                dfs([nx,ny],temp[:],count+1)
    return

dfs([0,0],hst,C)
print(C)
'''
살짝 수정해서 solve // dfs 에서 매번 새로운 hist 줄게 아니라 
방문할 곳이 없으면 마지막으로 넣은 걸 off 하는방식이 메모리 최적화에 좋다.
하지만 시간이 7.5sec 으로 턱걸이수준. 다음에 다시한번 풀어볼것
'''