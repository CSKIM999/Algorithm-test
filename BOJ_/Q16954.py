from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q16954
#######  TODAY  #######
##### 2022. 06. 28 #####
GIVEN ) 8*8 크기의 체스판에서 탈출하고자 한다.
        체스판의 각 칸은 벽 또는 빈칸이다. 캐릭터는 체스판의 왼쪽 아래에서 오른쪽 위로 이동하고자 한다.
        매 초마다 벽은 한칸씩 내려간다. 만약 벽이 떨어져서 테이블 밖으로 나가면 그 벽은 사라진다.
        캐릭터는 상하좌우대각으로 한칸씩 이동하거나 현재 위치에 서 있을수 있다. 또한 벽으로는 이동할 수없다.
        1초에 캐릭터가 먼저 이동하고 그 이후 벽이 이동하며, 벽이 캐릭터 위로 이동하면 캐릭터는 더이상 이동할 수 없다.
        캐릭터는 과연 오른쪽 윗칸으로 이동할수 있을까?
INPUT ) 8개 줄에 걸쳐 체스판이 주어지고 가장 왼쪽 아랫칸은 항상 벽이 아니다.
OUTPUT) 가능하다면 1 불가능하다면 0 을 출력하라
Approach ) 1초 루프를 잘 설정하자
8칸짜리인만큼 해봐야 8개의 벽 움직임 케이스가 있을것임.
각 bfs 케이스에 모두 테이블을 넣으면 낭비일것같음.
먼저 벽 움직임 케이스 8개를 만들고 이후 bfs

0초 ~ 7초까지의 케이스, 케이스를 벗어나면 무조건 가능하다는 뜻임
bfs
case[sec][x][y]
지금시간 = 0
큐.(7,0)
for 지금 in 근처9칸
    만약 테이블을 벗어나지 않는다면?
        만약 case[지금시간+1][지금x][지금y] 가 "." 이라면?
            만약 지금[x] == 0 and 지금[y] == 7 이라면?
                return 1
            큐에 지금 더하기 
return 0
'''
import sys
input = sys.stdin.readline
from collections import deque

table = []
for _ in range(8):
    a = list(input().strip())
    temp = []
    for i in a:
        if i == "#":
            temp.append(1)
        else:
            temp.append(0)
    table.append(temp)
case = []
case.append(table)

for i in range(1,9):
    temp = []
    for j in range(i):
        temp.append([0]*8)
    temp.extend(table[:-i])
    case.append(temp)

def sol():
    q = deque()
    q.append([7,0,0])
    while q:
        x,y,sec = q.popleft()
        for i in range(-1,2):
            for j in range(-1,2):
                nx,ny = x+i,y+j
                if 0<= nx < 8 and 0<= ny < 8:
                    try:
                        if not case[sec+1][nx][ny] and not case[sec][nx][ny]:
                            if nx==0 and ny ==7:
                                return 1
                            q.append([nx,ny,sec+1])
                    except IndexError:
                        return 1
    return 0

print(sol())
