d = [[-1,1],[-1,-1],[1,-1],[1,1]] # 1,2,3,4 분면의 좌표기준값
t = int(input())

for _ in range(t):
    n = int(input())
    table = set()
    for _ in range(n):
        x,y = list(map(int,input().split()))
        table.add((x,y))
    result = 0
    for x,y in table:
        for div in range(4): # 4분면 순회
            bomb = 0
            xdiv,ydiv = d[div][0],d[div][1]
            nx,ny = x+xdiv*10,y+ydiv*10
            xCalib,yCalib = 0,0 # 각 모서리에 10칸 이하로 인접한 경우를 보정해주기 위한 변수
            if nx < 0 or nx > 10000: # nx 가 테이블을 벗어난다면 10칸 이하로 인접했다는 뜻
                if nx < 0: # 보정작업
                    xCalib = -nx
                    nx = 0
                else:
                    xCalib = 10000-nx
                    nx = 10000
            if ny < 0 or nx > 10000:
                if ny < 0:
                    yCalib = -nx
                    ny = 0
                else:
                    yCalib = 10000-ny
                    ny = 10000
            xStart,xEnd = min(x,nx),max(x,nx) #for 문을 돌리기 위한 시작점 끝점 세팅
            yStart,yEnd = min(y,ny),max(y,ny)
            if xCalib > 0: #시작점 세팅 끝난 후 보정값 더해주기
                xEnd += xCalib
            else: # 보정 기본값이 0 이어서 그냥 더해줘도 상관없다
                xStart += xCalib
            if yCalib > 0:
                yEnd += yCalib
            else:
                yStart += yCalib
            # 매우 단순한 2중 for문. 만약 지뢰가 있으면 bomb 를 더해주고 마지막에 result 와 비교.
            for cx in range(xStart,xEnd+1):
                for cy in range(yStart,yEnd+1):
                    if (cx,cy) in table:
                        bomb += 1
            result = max(bomb,result)

    print(result)