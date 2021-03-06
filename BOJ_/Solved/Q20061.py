'''
Given ) 초록과 파랑 블록은 7행으로 이루어지며 6번행이 가장 바닥이다.
        한 행이 모두 블록으로 채워진다면 그 행은 사라지며 해당 블록은 1점을 획득한다
        블록은 빨강블록에 놓아진 뒤 각자의 블록의 바닥으로 떨어지며, 다른 블록을 만나면 그 자리에 멈춘다
        만약 0,1번 행에 타일이 위치한다면 해당 블록의 6번행은 삭제되며 한 행씩 아래로 밀린다.
Input ) 첫째 줄에 타일을 놓는 횟수 N 이 주어진다.
        둘째 줄부터 블록을 놓는 정보가 N 개 주어지며 한 줄에 하나씩 t x y 형태로 주어진다
        >>> t = 1 : 크기가 1*1 블록을 (x,y) 에 놓은 경우
        >>> t = 2 : 크기가 1*2 블록을 (x,y),(x,y+1) 에 놓은 경우
        >>> t = 3 : 크기가 2*1 블록을 (x,y),(x+1,y) 에 놓은 경우
        블록은 빨간 칸의 경계를 넘어가게 주어지지 않는다.
Output) 첫째 줄에 블록을 모두 놓고 나서 얻은 점수를 출력하라
        둘째 줄에는 초록과 파랑 두 블록에 타일이 들어가있는 칸의 개수의 합을 출력하라



Approach )  이번엔 각 필요 모듈을 확실하게 구현하고 조합해보자
            공동모듈
            >>> 1. 블록을 아래로 내리기
            >>> 2. 모두 채워진 행이 존재하는지 확인 후 해당 행 지우고 블록 내리기
            >>> 3. 0,1 번 행에 타일이 위치하면 6번행 지우기
            블루블럭 모듈
            >>> 1. 주어진 타일 회전
'''
import sys
n = int(input())
get = []
for i in range(n):
    get.append(list(map(int,input().split())))
point = 0
sectorPoint = 0
Block = [[[False]*4 for _ in range(6)] for _ in range(2)] # 0 : green 1: blue

def GtoB(lot):
    temp = []
    for x,y in lot: #lot = given
        temp.append([y,(3-x)])
    return temp
    
def blockdown(t,x,y,block,gnb):
    if gnb == 1:
        if t == 1:
            lot = [[x,y]]   
        elif t == 2:
            lot = [[x,y],[x,y+1]]
        else:
            lot = [[x,y],[x+1,y]]
        lot = GtoB(lot)
    else:    
        if t == 1:
            lot = [[x,y]]
        elif t == 2:
            lot = [[x,y],[x,y+1]]
        else:
            lot = [[x,y],[x+1,y]]

    stopPosition = 5
    for row,col in lot:#정지위치 찾기
        temp = [i[col] for i in block]
        for i in range(len(temp)):
            if temp[i]:
                stopPosition = min(i-1,stopPosition)
    
    for row,col in lot:
        if gnb == 1 and t == 2:
            block[stopPosition][col],block[stopPosition-1][col] = True, True
            return
        if t == 3 and gnb != 1:
            block[stopPosition][col],block[stopPosition-1][col] = True, True
            return
        block[stopPosition][col] = True
    return

def getPoint(block):
    global point
    flag = False
    for i in range(len(block)):
        if False in block[i]:
            continue
        block.remove(block[i])
        block.insert(0,[False]*4)
        point+=1
        flag = True
        break
    if flag:
        getPoint(block)

def CheckTheTopBlock(block):

    for i in range(2):
        if True in block[i]:
            block.pop()

    for i in range(6-len(block)):
        block.insert(0,[False]*4)

def settle(All):
    temp = 0
    for sector in All:
        for i in sector:
            for j in i:
                if j:
                    temp += 1
    
    return temp

for t,x,y in get:
    for i in range(2):
        blockdown(t,x,y,Block[i],i)
        getPoint(Block[i])
        CheckTheTopBlock(Block[i])
sectorPoint = settle(Block)
print(point)
print(sectorPoint)


'''
1회차>> 바로 정답판정 1초 추가시간 없는 조건에서 520ms 아주 빠른속도는 아닌듯하다.
        17825 의 실패를 발판으로 기계적 모듈화해서 풀어보았는데 꽤 효율이 좋았다. 아무래도 구현문제여서 그런것도 있는듯함.
'''