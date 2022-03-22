from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2933
#######  TODAY  #######
##### 2022. 03. 22 #####
GIVEN ) 동굴의 미네랄에 막대기를 던져 모든 행동이 끝난 후의 모습을 출력하라
        막대기는 왼쪽 오른쪽 순서로 번갈아가며 던져지며, 막대는 지정된 높이에서 수평으로 이동한다
        막대기와 처음 만나는 미네랄은 부서지며 만약 그 덩어리를 기준으로 결합되어있는 클러스터가 있다면
        그 클러스터는 추락한다. 여기서 두개이상 뭉쳐있는 미네랄 덩어리를 클러스터라 칭한다.
        클러스터가 추락하는 중간에는 그 모양이 변하지 않는다. 클러스터 중 어느 한 부분이라도 다른 클러스터 또는 땅에
        닿는 순간 추락은 멈추며, 추락이 멈추면 두 클러스터는 합쳐진다.
INPUT ) 첫째 줄에 동굴의 크기 R,C 가 주어진다 ( 1<= R,C <= 100 )
        다음 R 개의 줄에 . 또는 x 가 주어진다. . 은 빈칸, x 는 미네랄을 의미한다
        그 다음줄에는 막대를 던지는 횟수 N 이 주어진다 ( 1<= N <= 100 )
        마지막줄에 막대를 던지는 높이가 공백을 구분으로 주어지며 모든 높이는 1과 R 사이이다
OUTPUT) 입력과 같은 형식으로 미네랄의 모양을 출력하라
Approach )  미네랄이 부서지고 그 미네랄과 접한 미네랄들이 분리가 되는지 판별하는 bfs 만 있으면 구현은 쉽다
            동굴의 크기 던지는 횟수도 크지 않아 그냥 구현문제같음
'''
# import sys
# input = sys.stdin.readline


from collections import deque
d=[[1,0],[-1,0],[0,1],[0,-1]]
dic = {0:'.',1:'x','x':1,'.':0}
r,c = map(int,input().split())

# in IDE INPUT
table = [list(map(lambda x: dic[x],list(input()))) for _ in range(r)]

# in BOJ INPUT
# for i in range(r):
#     t = map(lambda x:dic[x],list(input().strip()))
#     table.append(list(t))

n = int(input())
stick = list(map(int,input().split()))
def check():
    q = deque()
    flag = True
    rt = [[0 for _ in range(c)] for _ in range(r)]
    count = 0
    for i in range(r):
        for j in range(c):
            if table[i][j] and not rt[i][j]:
                count += 1
                tempq = deque()
                tempq.append([i,j])
                q.append([i,j])
                rt[i][j] = count
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx,ny = d[k][0]+x,d[k][1]+y
                        if 0<=nx<r and 0<=ny<c: #테이블 유효범위
                            if not rt[nx][ny] and table[nx][ny]:
                                q.append([nx,ny])
                                tempq.append([nx,ny])
                                rt[nx][ny] = count
                
                if count not in rt[-1][:]:
                    flag = False
                    while tempq:
                        x,y = tempq.popleft()
                        rt[x][y] *= -1
    if flag:
        return rt,True
    else:
        return rt,False

def fall(given):
    R = []
    for i in range(c):
        temp = [j[i] for j in given]
        if min(temp)<0:
            # R.append(i)
            rm = r
            mc = 0
            for k in range(1,r+1):
                if not temp[-k]:
                    mc += 1
                elif temp[-k]>0:
                    mc = 0
                else:
                    rm = min(rm,mc)
            R.append([i,rm])
    m = min([i[1] for i in R])
    for i in range(c):
        temp = [j[i] for j in given]
        if min(temp)<0:
            for k in range(1,r+1):
                if given[-k][i]<0:
                    table[-k][i] = 0
                    table[-k+m][i] = 1
    # return R

def broke(h,s): # h는 그대로 s 는 -1(left),1(right) 로
    if s == -1:
        for i in range(c):
            if table[-h][i]:
                table[-h][i] = 0
                return
    else:
        for i in range(1,c+1):
            if table[-h][-i]:
                table[-h][-i] = 0
                return


lr = -1
for i in stick:
    broke(i,lr)
    lr *= -1
    a,t = check()
    if t:
        continue
    else:
        fall(a)

ans = []
for i in table:
    temp = ''
    for j in i:
        temp += dic[j]
    ans.append(temp)
for i in ans:
    print(i)

'''
1트 solve 예제만으로도 충분했음
'''