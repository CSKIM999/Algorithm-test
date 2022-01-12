'''
Q19236 - 청소년상어
Given ) 4*4 크기의 공간이 주어지고 물고기가 한 칸에 한 마리씩 존재한다.
        각 물고기는 번호와 방향을 가지며 번호는 1이상 16이하인 자연수이며,
        두 물고기가 같은 번호를 가지는 경우는 없다.
        물고기가 배치되고 0,0 에 존재하는 물고기를 청소년 상어가 먹으며 게임이 시작된다.
        상어의 방향은 0,0 에 존재하던 물고기의 방향을 상속받는다.
        
        물고기는 번호가 작은 물고기부터 한 칸씩 이동한다.
            물고기는 빈칸과 다른 물고기가 있는 칸으로만 이동할 수 있다
                만약 다른 물고기가 있다면 서로의 위치를 바꾼다

            만약 이동하려는 칸에 상어가 있거나 공간의 경계를 넘는다면 그 칸은 이동 불가능한 칸으로 간주한다.
                이동하려는 칸이 이동 불가능한 칸이라면, 물고기의 방향을 반시계 방향으로 45도 회전시킨다.
                회전을 통해 주변 최대 8칸 이내에 이동할 수 있는 칸이 없다면 이동하지 않는다.

        물고기의 이동이 끝나면 상어가 이동한다.
            상어는 현재 바라보고있는 방향으로 이동할 수 있으며 한번에 여러개의 칸을 이동할 수 있다.
            상어는 물고기가 있는 칸으로만 이동할 수 있으며, 이동하는 칸의 물고기를 먹고 그 물고기의 방향을 가진다.
            이동하는 중간에 마주치는 물고기는 먹지 않는다.

            만약 현재 바라보는 방향에 이동할 수 있는 칸이 없다면 공간에서 벗어나 집으로 간다.
Input ) 첫째 줄부터 4개의 줄에 물고기의 정보가 1번행부터 순서대로 주어진다.
        물고기의 정보는 두 정수 ai,bi 로 이루어지며 ai 는 물고기의 번호, bi 는 방향을 의미한다.
        bi 는 8보다 작거나 같은 자연수이며, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다. ( 반시계방향 )
Output) 상어가 먹을 수 있는 물고기 번호 합의 최댓값을 출력하라 
            

Approach )  많지는 않으나 경우의 수가 존재한다. 따라서 bfs 를 사용해야함.
            필요 모듈
            물고기 이동 관련
                물고기의 이동 : 빈칸이라면 이동, 물고기라면 위치바꾸기
                물고기의 회전 : 물고기를 45도씩 회전하며 이동 가능한 방향 찾기 && 처음 방향과 같아지면 이동안하기
            상어 이동 관련
                현재 상어가 바라보는 방향에 존재하는 물고기 리스트 반환
                물고기를 먹고 해당 물고기의 방향 상속
                바라보는 방향에 물고기 리스트 존재하지 않을경우 종료
'''

# rotate :  ↑, ↖, ←, ↙, ↓, ↘, →, ↗
rt = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
get = [
    [7, 6, 2, 3, 15, 6, 9, 8],
    [3, 1, 1, 8, 14, 7, 10, 1],
    [6, 1, 13, 6, 4, 3, 11, 4],
    [16, 1, 8, 7, 5, 2, 12, 2]
] # 출력 33
table = [] #[number,rotate]
Fish = [] #[인덱스번호 == 물고기번호 ,[x,y,d]]
result = 0

#게임시작과 0,0 위치한 물고기 먹기
num,rot = table[0][0]
shark = [0,0,rot]
result += num
Fish[num] = []
def getFlist(shark): # return : [Fishnum,FishRotate] || [] emptylist == gameover
    global rt,table
    temp =[]
    x,y,r = shark
    for i in range(4):
        nx,ny = x+(rt[r][0]*i),y+(rt[r][1]*i)
        if not 0<=nx<4 or not 0<=ny<4:
            break
        if table[nx][ny]: #현재 타겟이 비어있지 않다면 == 빈칸을 추려내기위함
            temp.append(table[nx][ny])

    return temp

def moveFish(fishes):
    global table
    for i in range(len(fishes)):
        if not fishes[i]:
            continue
        x,y,d = fishes[i]
        comp = d
        flag = True
        #회전 분기점
        while flag:
            nx,ny = x+rt[d][0],y+rt[d][1]
            target = table[nx][ny]
            if target == 0 or (not 0<=nx<4 or not 0<=ny<4):
                # 이동 불가의 경우
                d =  (d+1)%8
                if d == comp:
                    flag = False
            elif not target: #만약 비어있다면
                table[nx][ny] = i
                fishes[i] = [nx,ny,d]
                flag = False
            else:
                table[x][y],table[nx][ny] = table[nx][ny],table[x][y]
                fishes[i] = [nx,ny,d]
                fishes[target] = [x,y,fishes[target][2]]
                flag = False
        
def moveShark(Target,Fishes,Shark,Result,Table): #target = [fishnum,fishrot],Fishes : Fish
    x,y,r = Shark
    nx,ny,nr = Fishes[Target[0]]
    Result += Target[0]
    Shark = [nx,ny,nr]
    Table[nx][ny] = [0,nr]

    Fishes[Target] = []
    Table[x][y] = []
    

def dfs(Result,Table,Fishes,Shark):
    pass