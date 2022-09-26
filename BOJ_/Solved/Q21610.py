from collections import deque
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q21610
#######  TODAY  #######
##### 2022. 09. 26 #####
GIVEN ) 마법사 상어가 비바람 마법을 시전한다.
        비바라기를 시전하면 다음과 같은 룰대로 진행된다.
        1. 모든 구름이 지정한 방향으로 지정한 만큼 이동한다.
        2. 각 구름이 비를 내려 현재 위치한 칸의 바구니에 저장된 물의 양이 1 증가한다.
        3. 모든 구름이 사라진다.

        4. 2에서 물이 증가한 칸에 물복사 마법을 시전한다. 이는 대각선방향으로 거리가 1 인 칸에 현재 칸에 들어있는물의 양만큼 복사해서 더한다.
            여기서 대각선방향은 경계를 넘어가지 못한다.
        5. 바구니에 저장된 물의 양이 2 이상이라면 구름이 생기고 물이 2 줄어든다. 여기서 3에서 구름이 사라진 칸은 구름이 생기는 칸에서 제외된다.
INPUT ) 첫째 줄에 N,M 이 주어진다 (N: 2이상 50이하 자연수, M: 100 이하 자연수)
        둘째 줄부터 N 개의 정수가 주어지며 각각의 정수는 r행,c열의 수를 의미함 (각 원소는 100 이하의 자연수)
        다음 M개의 줄에 이동정보(d,s)가 한줄에 하나씩 주어짐 ( d : 8 이하의 자연수, s : 50 이하의 자연수)
OUTPUT) 첫째 줄에 M 번의 이동이 모두 끝난 후의 물 양을 출력하라
Approach )  첫번째 구름은 언제나 [(n,1),(n,2),(n-1,1),(n-1,2)] 에 위치함
            방향은 총 8개. 9시방향부터 시계방향
총 마법횟수가 100회 이하라서 그냥 빡구현으로도 가능할듯
필요 함수목록 : 이동 후 비내리기, 물복사 , 바구니 순회
이동후 비내리기 => {
    만약 이동명령이 테이블 크기와 같으면 이동안해도됨
    칸 밖으로 이동해도 적절한 위치로 이동해야함.
    사라질땐 이번 루프에서 사용할 hist 에 false처리
    }
물복사 => {
    테이블 밖으로 이동하지 않기때문에 dd 루프돌려서 밖이면 제외
}
순회 => {
    hist == True 이고 물의 양 2 이상이라면 2 빼주고 구름큐에 추가 
}
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

n, m = list(map(int, input().split()))
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
order = []
for i in range(m):
    order.append(list(map(int, input().split())))

d = [[0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]]
dd = [[-1, -1, 1, 1], [-1, 1, -1, 1]]


def cv(togo, dist):
    dist = dist % n
    dx, dy = d[0][togo], d[1][togo]
    # cloud = deque()
    while q:
        x, y = q.popleft()
        nx, ny = x+(dx*dist), y+(dy*dist)
        if nx < 0:
            nx = n+nx
        elif nx >= n:
            nx -= n
        if ny < 0:
            ny = n + ny
        elif ny >= n:
            ny -= n

        table[nx][ny] += 1
        hist.add((nx, ny))


def wv():
    for x, y in hist:
        for i in range(4):
            nx, ny = x+dd[0][i], y+dd[1][i]
            if 0 <= nx < n and 0 <= ny < n and table[nx][ny] > 0:
                table[x][y] += 1


q = deque()
q.extend([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])
for a, b in order:
    hist = set()
    a -= 1
    cv(a, b)
    wv()
    for i in range(n):
        for j in range(n):
            if (i, j) in hist:
                continue
            if table[i][j] >= 2:
                table[i][j] -= 2
                q.append([i, j])
result = 0
for i in range(n):
    result += sum(table[i])
print(result)
