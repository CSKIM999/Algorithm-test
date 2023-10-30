n,m,t = list(map(int,input().split()))
table = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] != 0:
            table[i][j] = [temp[j]]
        
playerLoc = [[0,0] for _ in range(m) ]
playerDir = [0]*m
playerPow = [[0,0] for _ in range(m) ]
points = [0]*m
for i in range(m):
    x,y,d,s = list(map(int,input().split()))
    x -= 1
    y -= 1
    playerLoc[i] = [x,y]
    playerDir[i] = d
    playerPow[i][0] = s

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def move(playerId):
    '''
    1. 플레이어는 본인이 바라보는 방향으로  한 칸 이동
	2. 만약 바라보는 다음 칸이 격자를 벗어나는 경우 반대로 방향을 바꾸어 이동
    '''
    x,y = playerLoc[playerId]
    d = playerDir[playerId]
    nx,ny = x+dx[d], y+dy[d]
    fight = None
    if 0<=nx<n and 0<=ny<n:
        pass
    else:
        if d == 0:
            d = 2
        elif d == 1:
            d = 3
        elif d==2:
            d = 0
        else:
            d = 1
        nx,ny = x+dx[d], y+dy[d]
    if [nx,ny] in playerLoc:
        fight = playerLoc.index([nx,ny])
    playerLoc[playerId] = [nx,ny]
    playerDir[playerId] = d
    return fight


def checkGun(playerId):
    '''
    1. 있다면 플레이어는 해당 총을 획득.
    2. 만약 플레이어가 총을 들고 있다면 공격력이 강한 총을 가지고, 다른 총을 바닥에 둔다.
    '''
    x,y = playerLoc[playerId]
    if table[x][y] == [] or len(table[x][y]) == 0: # 비어있다면 바로 돌아가기
        return # 여기 좀 바꿔줘야함
    
    myGun = playerPow[playerId][1]
    newGun = table[x][y][-1]
    if myGun == 0 or myGun < newGun:
        playerPow[playerId][1] = newGun
        table[x][y] = table[x][y][:-1]
        if myGun < newGun and myGun != 0:
            table[x][y].append(myGun)
        table[x][y].sort()

def loserMove(playerId):
    x,y = playerLoc[playerId]
    d = playerDir[playerId]
    myGun = playerPow[playerId][1]
    if myGun != 0:
        table[x][y].append(myGun)
        table[x][y].sort()
    playerPow[playerId][1] = 0
    for i in range(4):
        nd = (d+i)%4
        nx,ny = x+dx[nd], y+dy[nd]
        if 0<=nx<n and 0<=ny<n and [nx,ny] not in playerLoc:
            playerLoc[playerId] = [nx,ny]
            playerDir[playerId] = nd
            checkGun(playerId)
            return

def fight(playerId_1, playerId_2):
    '''
     두 플레이어는 싸우게 된다. 해당 플레이어의 초기능력치 + 총을 가졌다면 가진 총의 공격력 합을 비교하여 싸움.
		1. 싸움에서 이긴 플레이어
		   두 플레이어의 총+능력치 의 차이만큼 *포인트* 로 얻게 됩니다
		2. 싸움에서 진 플레이어
		   자신이 가지고있던 총을 해당 격자에 내려놓고 (배열 정렬) 바라보던 방향으로 한 칸 이동합니다. 
           만약 이동하려는 칸에 다른 플레이어가 있거나 격자 밖인 경우엔 오른쪽으로 90도씩 이동하며 빈칸을 찾고 이동합니다.
		3. 다시 이긴 플레이어는 승리한 칸에 떨어져있는 총들을 비교하여 가장 공격력이 높은 총을 획득합니다.
    '''
    player1 = sum(playerPow[playerId_1])
    player2 = sum(playerPow[playerId_2])
    if player1 < player2:
        winner = playerId_2
        loser = playerId_1
    elif player1 == player2:
        p1Power = playerPow[playerId_1]
        p2Power = playerPow[playerId_2]
        if p1Power > p2Power:
            winner = playerId_1
            loser = playerId_2
        else:
            winner = playerId_2
            loser = playerId_1
    else:
        winner = playerId_1
        loser = playerId_2
    
    points[winner] += abs(player1-player2)
    loserMove(loser)
    checkGun(winner)

for _ in range(t):
    for pid in range(m):
        whoThere = move(pid)
        if whoThere == None:
            checkGun(pid)
        else:
            fight(pid,whoThere)
print(' '.join(map(str,points)))