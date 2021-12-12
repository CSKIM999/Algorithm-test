import abc


def xprint(a):
    for i in a:
        print(i)

###############################################################################################################################################################################################
################################################################################    Q17144 _ 미세먼지 안녕!    ################################################################################
###############################################################################################################################################################################################
'''
Given ) 미세먼지는 R*C 크기의 격자판에 1*1 크기로 흩뿌려져있다. (r,c)는 r행 c열을 의미한다.
        공청기는 항상 1열에 설치되어있고 ( 행열은 1 부터 시작한다는 뜻 ), 크기는 두 행을 차지하며 위아래로 나뉘어 작동한다
        공청기가 설치되지 않은 칸에는 미세먼지가 있고 미세먼지의 양은 A[r][c] 이다. 1초마다 다음과 같은 알고리즘으로 미세먼지와 공청기는 작동한다
        1. 미세먼지의 확산 -> 미세먼지의 확산은 미세먼지가 존재하는 모든 칸에서 동시에 일어난다
            1.1. (r,c) 에 위치한 미세먼지는 인접한 네 방향으로 확산된다.
            1.2. 인접한 방향에 공청기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
            1.3. 확산되는 양은 A[r][c]/5 이고 소수점은 버린다.
            1.4. A[r][c] 에 남는 미세먼지는 A[r][c] - (A[r][c]/5)*확산된 방향의 개수 이다.
        2. 공청기의 작동
            2.1. 공청기에서는 바람이 나온다.
            2.2. 위쪽 공청기의 바람은 반시계방향으로 순환하여 되돌아오고, 아래 공청기의 바람은 시계방향으로 순환하여 되돌아온다.
            2.3. 바람이 불면 미세먼지가 바람의 방향대로 한칸씩 이동한다
            2.4. 공청기에서 나온 바람은 미세먼지가 없는 바람이고 공청기로 들어간 미세먼지는 모두 정화된다.
Input ) 첫째 줄에 R,C,T ( 6<= R,C <= 50, 1<= T <= 1000 ) 가 주어진다.
        둘째 줄부터 R 개의 줄에 A[r][c] (-1 <= A[r][c] <= 1000) 가 지어진다. 공청기가 설치된곳의 A[r][c] 는 -1 이고, 나머지 값은 미세먼지의 양이다.
        -1 은 위아래로 붙어져있고, 가장 위와 아래에서 2칸 이상 떨어져있다.
Output) T초 지난 후의 방에 남은 미세먼지양을 출력하라
'''

'''
R*C 의 최대크기는 50*50 으로 2500, 미세먼지 확산에 필요한 연산 2500 리스트로 관리할까? 확산시 각 칸에 영향을 주지 않기위해선 슬라이싱이 필요함 2500000
'''

# # r,c,t = 7,8,1
# # data = [
# #     [5 ,0 ,0, 0, 0, 0, 0 ,9],
# #     [0 ,0 ,0, 0, 3, 0, 0 ,8],
# #     [-1, 0, 5, 0, 0, 0, 22 ,0],
# #     [-1, 8, 0, 0, 0, 0, 0 ,0],
# #     [0 ,0 ,0 ,0, 0 ,10 ,43 ,0],
# #     [0 ,0 ,5 ,0, 15, 0 ,0 ,0],
# #     [0 ,0 ,40 ,0 ,0, 0, 20 ,0]
# # ]

# r,c,t = map(int,input().split())
# data = []
# for i in range(r):
#     data.append(list(map(int,input().split())))

# # r,c,t = 3,3,1
# # data = [
# #     [0,0,0],
# #     [0,46,0],
# #     [0,0,0]
# # ]

# cleaner = []
# for i in range(r):
#     if data[i][0] == -1:
#         cleaner.append(i)
#         cleaner.append(i+1)

#         break
# dx,dy = [-1,0,1,0],[0,1,0,-1]

# for _ in range(t):
#     temp = [[0]*c for _ in range(r)]
#     #확산
#     tx,bx=cleaner[0],cleaner[1]
#     for i in range(r):
#         for j in range(c):
#             if (i == tx or i==bx) and j == 0:
#                 temp[i][j] = -1
#                 continue
#             if data[i][j] >= 5:
#                 now = data[i][j]
#                 sep = data[i][j]//5
#                 count = 0
#                 for q in range(4):
#                     nx,ny = i+dx[q],j+dy[q]
#                     if (0<=nx<r and 0<=ny<c) and data[nx][ny] != -1:
#                         count +=1
#                         temp[nx][ny] += sep
#                 temp[i][j] += now-sep*count
#             elif 0<= data[i][j] <5:
#                 temp[i][j] += data[i][j]
#     data = [i[:] for i in temp]
#     #공청기
#     tt,tb,bt,bb = data[0][:],data[tx][:],data[bx][:],data[-1][:]
#     L,R = [i[0] for i in data],[i[-1] for i in data]
#     tr,tl,br,bl = R[:bx],L[:bx], R[bx:],L[bx:]

#     data[0][:-1] = tt[1:]
#     for i in range(tx):
#         data[i][-1] = tr[i+1]
#         if data[i][0] != -1 and i != 0:
#             data[i][0] = tl[i-1]
#     data[tx][1:] = [0] + tb[1:-1]

#     data[bx][1:] = [0] + bt[1:-1]
#     for x,i in enumerate(range(bx+1,r)):
#         data[i][-1] = br[x]
#         if i<r-1:
#             data[i][0] = bl[x+2]
#     data[-1]= bb[1:] + [br[-2]]

# result = 2
# for i in range(r):
#     result += sum(data[i])
# print(result)

###############################################################################################################################################################################################
####################################################################################    Q17144 _ 낚시왕    ####################################################################################
###############################################################################################################################################################################################
'''
Given ) r*c 의 격자칸에 상어가 들어있으며 각 상어는 크기와 속도를 가지고 있다. 
        낚시왕은 처음에 1번열의 한칸 왼쪽에 위치한다. 1초마다 알고리즘에 따라 이동하며, 가장 오른쪽열의 오른쪽에 위치하면 이동을 멈춘다.
            1.낚시왕이 오른쪽으로 한 칸 이동한다
            2.낚시왕이 있는 열에 있는 상어 중 지면과 가장 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
            3.상어가 이동한다
        상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초 이다. 상어가 이동하려고 하는 칸이 격자판의 경계를 넘어갈 때, 상어는 방향을 반대로 바꾸어 속력을 유지한채로 이동한다
        한 칸에 상어는 두마리 이상 위치할 수 있으며, 이 경우 가장 큰 상어가 나머지상어를 모두 잡아먹는다
        격자판의 상태가 주어질 때 낚시왕이 잡은 상어 크기의 합을 구해보자
Input ) 첫째 줄에 R,C,M 이 주어진다 ( 2<= r,c <= 100 // 0<= M <= r*c)
        둘째 줄부터 m 개의 줄에 상어의 정보가 주어진다. 상어의 정보는 다섯개의 정수로 이루어져있다
        r,c,s,d,z (1<=r<=R // 1<=c<=C // 0<=s<=1000 // 1<=d<=4 // 1<=z<=10000 )
        r,c 는 상어의 좌표, s 는 속력, d는 방향, z 는 크기이다. d 는 1~4 로 위/아래/오른쪽/왼쪽 을 의미한다.
Output) 낚시왕이 잡은 상어 크기의 합을 출력하라
'''

# # r,c,m = 4,6,8
# # give =[
# #     [4, 1, 3, 3, 8],
# #     [1, 3, 5, 2, 9],
# #     [2, 4, 8, 4, 1],
# #     [4, 5, 0, 1, 4],
# #     [3, 3, 1, 2, 7],
# #     [1, 5, 8, 4, 3],
# #     [3, 6, 2, 1, 2],
# #     [2, 2, 2, 3, 5]
# # ]

# r,c,m = map(int,input().split())
# give = []
# for i in range(m):
#     give.append(list(map(int,input().split())))


# data = [[[] for _ in range(c)] for _ in range(r)]
# dic = {0:-1,1:1,2:2,3:-2}
# for x,y,s,d,z in give:
#     d = dic[d-1]
#     data[x-1][y-1].append((s,d,z))
# king = 0

# # 1
# for idx in range(c): # c 로변경하기
#     # 2
#     for q in range(r):
#         if data[q][idx]:
#             s,d,z = data[q][idx][0]
#             king += z
#             data[q][idx] = []
#             break
    
#     #3
#     temp = []
#     for i in range(r):
#         for j in range(c):
#             if data[i][j]:
#                 s,d,z = data[i][j][0] #5 1 9
#                 x,y = i,j
#                 data[i][j].remove((s,d,z))
#                 #이동

#                 if d == -1 or d == 1:
#                     n = s%((r-1)*2)
#                     while n!=0:
#                         if d > 0:
#                             t = r-x-1
#                             if n<t:
#                                 x += n
#                                 n = 0
#                             else:
#                                 x +=t
#                                 n -=t
#                                 d*=-1
#                         else:
#                             if n<x:
#                                 x -=n
#                                 n = 0
#                             else:
#                                 n -=x
#                                 x = 0
#                                 d *= -1
                        
#                 else:
#                     n = s%((c-1)*2)
#                     while n!=0:
#                         if d > 0:
#                             t = c-y-1
#                             if n<t:
#                                 y += n
#                                 n = 0
#                             else:
#                                 y +=t
#                                 n -=t
#                                 d*=-1
#                         else:
#                             if n<y:
#                                 y -=n
#                                 n = 0
#                             else:
#                                 n -=y
#                                 y = 0
#                                 d *= -1

#                     # for q in range(s):
#                     #     if 0<= y+(d//2) < c:
#                     #         y += d//2
#                     #     else:
#                     #         d *= -1
#                     #         y += d//2

#                 temp.append((x,y,s,d,z))
#     for x,y,s,d,z in temp:
#         if data[x][y]:
#             if data[x][y][0][2] < z:
#                 data[x][y].clear()
#                 data[x][y].append((s,d,z))
#                 continue
#             else:
#                 continue
#         data[x][y].append((s,d,z))

# print(king)


###############################################################################################################################################################################################
#############################################################################    Q17140 _ 이차원 배열과 연산     ##############################################################################
###############################################################################################################################################################################################
'''
Given ) 크기가 3*3 의 배열 A 가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.
            R 연산 : 배열 A 모든 행에 대해서 정렬을 수행한다. 행의 개수 >= 열의 개수인 경우 적용
            C 연산 : 배열 A 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우 적용
        각 행/열 을 정렬하기 위해선, 각각의 수가 몇 번 나왔는지 알아야한다. 그 다음 등장횟수가 커지는 순서로 정렬하고, 같은 수라면 그 수가 커지는 순서로 정렬하여 다시 배열 A 에 넣는다.
        정렬 결과를 배열에 넣을땐, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.
        연산을 통해 나온 리스트를 넣는다면 현재 리스트의 길이와 다를 수 있다. 그 경우 비어있는 곳에 0 을 채워넣으면 된다.
        또한 0이 채워진 리스트를 다시 정렬할 때 0 은 수로서는 무시하고 진행한다.
        행/열 의 크기가 100 이상 넘어간다면, 앞의 100개를 제외한 나머지를 버린다.
Input ) 첫째 줄에 r,c,k 가 주어진다 ( 1 <= r,c,k <= 100 )
        둘째 줄부터 3개의 줄에 배열 A 에 들어가있는 수가 주어진다. 배열 A 에 들어가있는 수는 100 보다 작거나 같은 수 이다.

Output) A[r][c] 에 들어있는 값이 k 가 되기위한 연산의 최소시간을 출력하라. 100초가 지나도 A[r][c] == k 가 아니라면 -1 을 출력하라
'''

'''
Approach ) 우선 R/C 연산을 구현하고 몇번 반복해보자. 반복에 따른 내가 모르는 규칙이 발생할 수도 있다. 정렬의 방식은 계수정렬을 의미하는 듯하다. 최대 100개의 원소를 가지지만, 
꺼내는 속도를 더욱 더 빠르게 하기위해 queue 를 써볼까 한다
'''

# from collections import deque

# def Csort(lst):
#     counting = [[i,0] for i in range(101)]
#     result = []
#     for i in lst:
#         counting[i][1]+=1
#     counting.sort(key= lambda x:x[1])

#     # print(counting)
#     counting = deque(counting)
#     while counting:
#         a,b = counting.popleft()
#         if b == 0 or a == 0:
#             continue
#         else:
#             result += [a,b]
#     return result


# def cal_c(x): #열 정렬
#     vert = []
#     bm = 0
#     for i in range(len(x[0])):
#         tmp = [j[i] for j in x]
#         tmp = Csort(tmp)
#         if len(tmp) >= 100:
#             tmp = tmp
#         bm = max(bm,len(tmp))
#         vert.append(tmp)
#     result = [[] for _ in range(bm)]
#     for i in range(len(vert)):
#         if len(vert[i]) < bm:
#             t = [0]*(bm-len(vert[i]))
#             vert[i] += t
#         for j in range(bm):
#             result[j].append(vert[i][j])
#     return result

# def cal_r(x): #행 정렬
#     bm = 0
#     hor = []
#     for i in x:
#         i = Csort(i)
#         if len(i) >= 100:
#             i = i[:100]
#         bm = max(bm,len(i))
#         hor.append(i)
#     result = []
#     for i in hor:
#         if len(i) < bm:
#             t = [0]*(bm-len(i))
#             i+=t
#         result.append(i)
#     return result

# r,c,k = map(int,input().split())
# data = []
# for i in range(3):
#     data.append(list(map(int,input().split())))
# count = 0

# while count!=101:
#     try:
#         if data[r-1][c-1] == k:
#             break
#     except IndexError:
#         pass
#     count += 1
#     if len(data)>=len(data[0]):
#         data = cal_r(data)
#     else:
#         data = cal_c(data)

# if count != 101:
#     print(count)
# else:
#     print(-1)
'''
1회차 > 무난한 정답판정. 시간도 추가없는 0.5초였지만, data 의 크기가 최대 100*100에 불과해서 러프하게 작성했다.
'''


###############################################################################################################################################################################################
##################################################################################    Q17142 _ 연구소 3     ###################################################################################
###############################################################################################################################################################################################
'''
Given ) 연구소 내에 있는 바이러스를 유출하려고 한다. 바이러스는 활성/비활성 상태로 나뉘며, 가장 처음의 바이러스는 모두 비활성 상태이며 활성 상태 바이러스는 상/하/좌/우 인접한 모든 칸에 동시 복제되며
        1초를 소요한다. 승원이는 M 개의 바이러스를 활성 상태로 변경하고자 한다.
        연구소는 n*n 크기이며, 활성 바이러스가 비활성 바이러스가 있는 칸으로 이동하면, 비활성 바이러스가 활성으로 변한다.
Input ) 첫째 줄에 연구소의 크기 n (4<= n <= 50) , 놓을 수 있는 바이러스의 수 m (1 <= m <= 10) 이 주어진다
        둘째 줄부터 n 개의 줄에 연구소의 상태가 주어진다. 0은 빈칸, 1은 벽, 2는 바이러스를 놓을 수 있는 자리이다. 2 의 개수는 m 보다 크거나 같고 10보다 작거나 같은 자연수이다.
Output) 연구소의 모든 빈칸에 바이러스가 있게 되는 최소시간을 출력 // 만약 어디에 두어도 모든 빈칸에 퍼트리지 못한다면, -1을 출력
'''

'''
1회차 > 각 노드들을 dfs 로 처리하고 각 위치에 두었을때의 퍼지는 모양을 bfs 로 구현해보자
'''

# from collections import deque
# from itertools import combinations
# import sys

# input = sys.stdin.readline

# n,m = map(int,input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))

# answer = 1e9
# germ = []
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 2:
#             germ.append([i,j])
# def plague(data,cycle):
#     global answer
#     temp = [i[:] for i in data]
#     for i in range(n):
#         for j in range(n):
#             if temp[i][j] == 1:
#                 temp [i][j] = -1
#             elif temp[i][j] == 2:
#                 if [i,j] in cycle:
#                     temp[i][j] = 1
#                 else:
#                     temp[i][j] = -2
#             else:
#                 temp[i][j] = 0
#     # hist = [[True]*n for _ in range(n)]
#     search = [(1,0),(-1,0),(0,-1),(0,1)]
#     cycle = [i[:]+[1] for i in cycle]
#     q = deque(cycle)
#     result = 0
#     while q:
#         x,y,count = q.popleft()
#         for dx,dy in search:
#             if 0<=x+dx<n and 0<=y+dy<n:
#                 if temp[x+dx][y+dy] == 0:
#                     if count+1 == answer:
#                         return answer
#                     temp[x+dx][y+dy] = count+1
#                     q.append((x+dx,y+dy,count+1))
#                 elif temp[x+dx][y+dy] == -2:
#                     temp[x+dx][y+dy] = 1
#                     q.append((x+dx,y+dy,count+1))

#     for i in range(n):
#         for j in range(n):
#             if temp[i][j] == 0:
#                 return -1
#             elif temp[i][j] >result:
#                 result = max(result,temp[i][j])
#     flag = True
#     return result

# # def dfs(lst=[]):
# #     global m,answer,germ
# #     if len(lst) > m:
# #         return
# #     elif len(lst) > 0:
# #         # tmp = plague(data,lst)
# #         answer +=1
# #         # print(answer)
# #         # if tmp != -1:
# #         #     answer = min(answer,tmp)
# #     for i in germ:
# #         if i in lst:
# #             continue
# #         lst.append(i)
# #         dfs(lst)
# #         lst.remove(i)

    

# ind = list(combinations(germ,m))
# for j in ind:
#     if len(j) == 1:
#         tmp = plague(data,[j[0]])
#         if tmp != -1:
#             answer = min(answer,tmp)
#     else:
#         tmp = plague(data,[k for k in j])
#         if tmp != -1:
#             answer = min(answer,tmp)
    
# if answer == 1e9:
#     answer = -1
# else:
#     answer = answer-1
# print(answer)


'''
1회차 > pypy 로는 충분히 pass 하고 python3 로도 넉넉히 패스했다. dfs 와 bfs 를 동시사용하라는 말이 많았는데 combination 으로도 가능했다.

'''


###############################################################################################################################################################################################
#####################################################################################    Q17779 _ 게리맨더링2     #####################################################################################
###############################################################################################################################################################################################
'''
Given ) N*N 크기의 재현시에 각 구역을 5개 선거구로 나눠야하고, 각 구역은 다섯 선거구 중 하나에 포함되어야한다. 선거구는 구역을 적어도 하나 포함해야 하고  한 선거구에 포함된 구역은
        모두 연결되어 있어야 한다. 구역 A 에서 인접한 구역을 통해 B 구역으로 갈 수 있을 때 두 구역은 연결되어있다 한다. 중간에 통하는 인접구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함돼야한다.
        선거구는 다음과같이 나뉜다.
        1. 기준점 (x,y) 와 경계의 길이 d1,d2 를 정한다. (d1,d2 >= 1, 1<=x<=x+d1+d2<=N , 1<= y-d1<y<y+d2<= N)
        2. 다음칸은 경계선이다.
            2.1. (x,y),(x+1,y-1),...,(x+d1,y-d1)
            2.2. (x,y),(x+1,y+1),...,(x+d2,y+d2)
            2.3. (x+d1,y-d1),(x+d1+1,y-d1+1),...,(x+d1+d2,y-d1+d2)
            2.4. (x+d2,y+d2),(x+d2+1,y+d2-1),...,(x+d2+d1,y+d2-d1)
        3. 경계선과 경계선의 안에 포함되는곳이 5번선거구다.
        4. 5번 선거구에 포함되지 않는 구역의 선거구 번호는 다음 기준을 따른다.
            1번선거구 : 1<=r<x+d1 , 1<=c<=y
            2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
            3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
            4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
Input ) 첫째 줄에 재현시의 크기 N 이 주어진다. ( 5 <= N <= 20 )
        둘째 줄부터 N 개의 줄에 N 개의 정수가 주어진다. A[r][c] 는 r행c열의 정수를 의미
Output) 첫째 줄에 최대 인구수 선거구와 최소 인기수 선거구의 차이를 출력하라
'''

# n = 6
# data = [
#     [1, 2, 3, 4, 1, 6],
#     [7, 8, 9, 1, 4, 2],
#     [2, 3, 4, 1, 1, 3],
#     [6, 6, 6, 6, 9, 4],
#     [9, 1, 9, 1, 9, 5],
#     [1, 1, 1, 1, 9, 9]
# ]

# import sys
# input = sys.stdin.readline
# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))

# def divide(N,x,y,d1,d2):
#     a,b,c = x+d1-1,x+d2-1,y-d1+d2-1
#     bd = set()
#     mat = [[0]*N for i in range(N)]
#     bd.add((x,y))
#     for i in range(1,d1+1):
#         bd.add((x+i,y-i))
#         bd.add((x+d2+i,y+d2-i))
#     for i in range(1,d2+1):
#         bd.add((x+i,y+i))
#         bd.add((x+d1+i,y-d1+i))
    
#     bd =sorted(bd,key= lambda x:(x[0],-x[1]) )
#     b1,b2 = 0,0
#     while bd:
#         t1,t2 = bd.pop()
#         if b1!=t1-1:
#             mat[t1-1][t2-1] = 5
#             b1,b2 = t1-1,t2-1
#             continue
#         else:
#             mat[b1][b2+1:t2] = [5]*(t2-1-b2)
#             b1,b2 = 0,0

#     for i in range(N):
#         for j in range(N):
#             if 0<=i<a and 0<=j<=y-1 and mat[i][j] ==0:
#                 mat[i][j] = 1
#             elif 0<=i<=b and y-1<j and mat[i][j] == 0:
#                 mat[i][j] = 2
#             elif a<=i and 0<=j<c and mat[i][j] == 0:
#                 mat[i][j] = 3
#             elif mat[i][j] == 0:
#                 mat[i][j] = 4

#     return mat
# result= 1e9
# # 0<x<n-1 // 0<= y <n-2 // x-1+(n-y)/2
# for x in range(1,n-1):
#     for y in range(2,n):
#         flag = True
#         for d1 in range(n):
#             for d2 in range(n):
#                 try:
#                     test = data[x+d1+d2][y] + data[x+d2][y+d2]
#                 except IndexError:
#                     break
#                 tmp = divide(n,x,y,d1,d2)
                
#                 sd = [0 for _ in range(5)]
#                 for i in range(n):
#                     for j in range(n):
#                         now = tmp[i][j]
#                         sd[now-1] += data[i][j]
                
#                 tr = max(sd) - min(sd)
#                 result = min(result,tr)

                        
# print(result)
'''
1회차 > 시간소요를 너무 생각하느라 오래걸렸는데, 조금 러프하게 풀어도 넉넉히 시간을 충족했음.
'''

###############################################################################################################################################################################################
################################################################################     Q13460 _ 구슬 탈출 2    ##################################################################################
###############################################################################################################################################################################################
'''
Given ) N*M 크기의 보드가 1x1 칸으로 나누어져 가장 바깥 행과 열은 벽으로 막혀있다. 보드에는 구멍이 하나 있고 임의의 공간에 빨간 구슬과 파란 구슬이 각각 들어가있다.
        게임의 목표는 파란 구슬이 구멍으로 들어가기 전에 빨간 구슬을 꺼내는 것이다. 구슬은 중력을 이용하여 이리 저리 굴린다.
        각각의 동작에서 공은 동시에 움직이며 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 구슬은 각각 한칸을 차지하여 동시에 같은 칸에 있을 수없다.
        기울이는 동작을 그만하는것은 더이상 구슬이 움직이지 않을 때 까지이다. 최소 몇번 움직여서 구슬을 뺄 수 있는지 프로그램을 작성하라.
Input ) 첫째 줄에는 가로 세로 N과 M 이 주어진다. ( 3<= N,M <= 10 )
        그 이후 N개의 줄에 걸쳐 M 개의 문자열이 주어진다. '.','#','O','R','B' 에서 . 은 빈칸을 의미하고, #은 벽, O 는 구멍, R 은 빨간 구슬 B 는 파란 구슬을 의미한다.
Output) 최소 몇번만에 빨간 구슬을 구멍을 통해 빼낼 수 있는 지 출력하라. 만약 10번을 초과한다면 -1 을 출력하라.
'''
'''
2회차 > 움직임 함수를 dfs 를 통해 구현할것. 추가로 빨간구슬과 파란구슬은 각각 움직임이 끝나고 한 자리를 차지한다.
'''

# n,m = 7,7
# table = [
#     '#######',
#     '#..R#B#',
#     '#.#####',
#     '#.....#',
#     '#####.#',
#     '#O....#',
#     '#######'
# ]
# dic = {'#':4,'.':0,'R':1,'B':2, 'O':7}
# n,m = map(int,input().split())
# table = []
# for i in range(n):
#     table.append(input())
# matrix = []
# blue,red = [],[]
# goal = []
# for i in table:
#     matrix.append([dic[j] for j in i])
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == 1:
#             red = [i,j]
#         elif matrix[i][j] == 2:
#             blue = [i,j]
#         elif matrix[i][j] == 7:
#             goal = [i,j]

# def go_horizon(mat,ball,side): #matrix 와 ball 의 좌표 반환예정 /// side = 1 -> right & -1 ->left
#     x,y = ball
#     temp = mat[x][:]
#     ny = y
#     while True:
#         if temp[ny+side] != 0:
#             if temp[ny+side] == 7:
#                 temp[y] = 0
#                 mat[x] = temp
#                 ball = [-1,-1]
#                 return mat,ball
#             temp[ny],temp[y] = temp[y],temp[ny]
#             break
#         else:
#             ny += side
#     mat[x] = temp
#     ball = [x,ny]

#     return mat,ball

# def go_vertical(mat,ball,side): # side = 1 -> down & side = -1 up
#     x,y = ball
#     temp = [i[y] for i in mat]
#     nx = x
#     while True:
#         if temp[nx+side] != 0 :
#             if temp[nx+side] == 7:
#                 temp[x] = 0
#                 for i in range(n):
#                     mat[i][y] = temp[i]
#                 ball = [-1,-1]
#                 return mat,ball
#             temp[nx],temp[x] = temp[x],temp[nx]
#             break
#         else:
#             nx += side
#     for i in range(n):
#         mat[i][y] = temp[i]
#     ball = [nx,y]
#     return mat,ball

# def move(matrix,red,blue,voh,side): # voh -> 0 = v 1 = h
#     rx,ry = red
#     bx,by = blue
#     if voh == 1: #세로이동
#         if ry == by: #같은 선상일때
#             if side == 1: #아래로 움직일때
#                 if rx<bx:
#                     matrix,blue = go_vertical(matrix,blue,side)
#                     matrix,red = go_vertical(matrix,red,side)
#                 else:
#                     matrix,red = go_vertical(matrix,red,side)
#                     matrix,blue = go_vertical(matrix,blue,side)
#             else:
#                 if rx<bx:
#                     matrix,red = go_vertical(matrix,red,side)
#                     matrix,blue = go_vertical(matrix,blue,side)
#                 else:
#                     matrix,blue = go_vertical(matrix,blue,side)
#                     matrix,red = go_vertical(matrix,red,side)
#         else:
#             matrix,blue = go_vertical(matrix,blue,side)
#             matrix,red = go_vertical(matrix,red,side)
#     else: #가로이동
#         if rx == bx:
#             if side == 1: #오른쪽
#                 if ry < by:
#                     matrix,blue = go_horizon(matrix,blue,side)
#                     matrix,red = go_horizon(matrix,red,side)
#                 else:
#                     matrix,red = go_horizon(matrix,red,side)
#                     matrix,blue = go_horizon(matrix,blue,side)
#             else:
#                 if ry < by:
#                     matrix,red = go_horizon(matrix,red,side)
#                     matrix,blue = go_horizon(matrix,blue,side)
#                 else:
#                     matrix,blue = go_horizon(matrix,blue,side)
#                     matrix,red = go_horizon(matrix,red,side)
#         else:
#             matrix,blue = go_horizon(matrix,blue,side)
#             matrix,red = go_horizon(matrix,red,side)
#     return matrix,red,blue
# # voh [0:v , 1:h] , vside[1:down,-1:up] , hside[-1:left,1:right]
# result = 11
# def dfs(give,r,b,count):
#     global goal,result
#     temp = []
#     if count >= result:
#         return
#     temp,rr,bb = move([i[:] for i in give],r,b,0,-1)
#     if temp != give:
#         dfs([i[:] for i in temp],rr,bb,count+1)
#         if rr==[-1,-1] and bb!=[-1,-1]:
#             result = min(result,count)
#     temp,rr,bb = move([i[:] for i in give],r,b,0,1)
#     if temp != give:
#         dfs([i[:] for i in temp],rr,bb,count+1)
#         if rr==[-1,-1] and bb!=[-1,-1]:
#             result = min(result,count)
#     temp,rr,bb = move([i[:] for i in give],r,b,1,-1)
#     if temp != give:
#         dfs([i[:] for i in temp],rr,bb,count+1)
#         if rr==[-1,-1] and bb!=[-1,-1]:
#             result = min(result,count)
#     temp,rr,bb = move([i[:] for i in give],r,b,1,1)
#     if temp != give:
#         dfs([i[:] for i in temp],rr,bb,count+1)
#         if rr==[-1,-1] and bb!=[-1,-1]:
#             result = min(result,count)

# dfs(matrix,red,blue,1)
# if result == 11:
#     print(-1)
# else:
#     print(result)


'''
2회차 > 정답판정 받음. 각 움직임을 모듈화 하여 객체지향성을 띠는 연습을 더 해야할듯
'''

###############################################################################################################################################################################################
#############################################################################   Q20055 _ 컨베이어벨트 위 로봇    ##############################################################################
###############################################################################################################################################################################################
'''
Given ) 길이 N 인 컨베이어 벨트가 있고, 길이가 2N 인 벨트가 이 컨베이어를 중심으로 돈다.
        1번은 "올리는 위치", 2N번은 "내리는 위치" 이다. 로봇은 벨트 위로 올리는 위치에만 올릴 수 있다.
        로봇을 옮기는 과정은 다음을 따른다.
        1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        2. 가장 벨트에 먼저 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
            2.1.로봇이 이동하기 위해선 다음칸에 로봇이 없으며, 그 칸 내구도가 1 이상 남아있어야 한다.
        3. 올리는 위치에 있는 칸의 내구도가 0 이 아니라면 올리는 위치에 로봇을 올린다.
        4. 내구도가 0 인 칸이 K 개 이상이라면, 과정을 종료한다. 아니라면, 1번드로 돌아간다.
Input ) 첫째 줄에 N,K 가 주어진다. 둘째 줄에 A1-A2n 이 주어진다. ( 2<= N <= 100  /// 1<= K <= 2N /// 1 <= Ai <= 1,000 )
Output) 몇번째 단계에서 break 되었는지 출력하라
'''

'''
1회차 > 딱봐도 쉬운문제. 이해하는게 더 오래걸림. while 문으로 계속 돌리되, [bool,count] 리스트를 통해 만들든 리스트를 두개 동기화하든 상관없어보임 그래봐야 N 이 100
        하지만 객체 지향적으로 코딩하려 노력해보자.
        -> return 값이 없는 단순한 함수
'''
# n,k = map(int,input().split())
# data = list(map(int,input().split()))
# robot=[]

# half = len(data)//2
# result = 0

# def roll():
#     global data
#     data = [data[-1]]+data[:-1]
#     if len(robot) != 0:
#         for i in range(len(robot)):
#             robot[i] = (robot[i] + 1)%len(data)
#                 # if data[robot[i]] > 0:
#                 #     data[robot[i]] -= 1


# def Check(now):
#     new = (now + 1)%len(data)
#     if data[new] > 0:
#         if new not in robot:
#             return True
#     return False

# def GoDown():
#     if (half-1) in robot:
#         robot.remove(half-1)

    
# while True:
#     roll()
#     GoDown()

#     #로봇 움직임 구현
#     if len(robot) != 0: #로봇이 1개 이상이라면
#         for i in range(len(robot)): # 로봇 인덱스를 순회하며 로봇 움직임 구현
#             if Check(robot[i]): #만약 로봇이 움직일수 있다면
#                 robot[i] = (robot[i] + 1) % len(data) #움직인다
#                 data[robot[i]] -= 1
#     GoDown()

#     #로봇 올리기
#     if Check(-1):
#         data[0] -= 1
#         robot.append(0)

#     result += 1

#     if data.count(0) >= k:
#         break

# print(result)
'''
1회차 > pypy3 사용 정답. 내용은 쉬운데 설명이 준나게 드러운문제였음.
'''

###############################################################################################################################################################################################
################################################################################   Q17837  _ 새로운 게임 2     ################################################################################
###############################################################################################################################################################################################
'''
Given ) N*N 크기의 판에서 K개의 말이 순서에 따라 움직인다. 말은 방향을 가지며 두 개 이상 겹쳐질 수 있으나 순서를 구분한다. 턴 한번에 1번부터 K 번 말까지 순서대로 이동시킨다.
        현재 말이 다음에 이동할 다음칸에 대한 룰은 다음과 같다.
        1. 흰색의 경우 -> 그 칸으로 이동한다. 만약 다른 말이 이미 존재한다면 가장 위에 A번 말을 올려놓는다.
            A번 말의 위에 다른말이 있는경우 모든 말이 함께 이동한다.
            ex ) D,E 말이 이미 존재하고 A,B,C 말이 그 위로 이동한다면 E,D,A,B,C 가 된다.
        2. 빨간색의 경우 -> 이동한 후 이동한 말의 순서가 반대로 바뀐다.
            A,B,C 가 이동하고 이동하려는 칸에 말이 없는 경우 C,B,A 가 위치한다.
            A,D,F,G 가 이동하고, 이동하려는 칸에 E,C,B로 있는 경우에는 E,C,B,G,F,D,A 가 된다.
        3. 파란색의 경우 -> 현재 이동하려는 말의 방향을 반대로 하고 한칸 이동한다.
            만약 반대방향이 막혀 이동할 수 없다면 이동하지 않고 가만히 있는다.
        4. 체스판을 벗어나는 경우
            3번으로 취급하여 처리한다.
Input ) 첫째 줄에 체스판의 크기 N, 말의 개수 K 이 주어진다.
        둘째 줄부터 N개의 줄에 걸쳐 체스판의 정보가 주어진다. 0은 흰색, 1 은 빨간색, 2는 파란색을 의미한다.
        다음 K 개의 줄에 말의 정보가 1번부터 순서대로 주어진다. 각 행은 순서대로 행,열,방향 이 주어진다.
        방향은 1,2,3,4 순서로 동,서,북,남 방향이다.
Output) 한 칸에 말이 4개 이상 올라간다면 그 즉시 게임은 종료된다.
        게임이 종료되는 턴의 번호를 출력한다. 그 값이 1000을 넘어간다면, -1을 출력한다.
'''
# n,k = 4,4
# data = [
#     [0, 0, 2, 0],
#     [0, 0, 1, 0],
#     [0, 0, 1, 2],
#     [0, 2, 0, 0]
# ]
# dot = [[1,0,0],[2,1,2],[1,1,0],[3,0,1]]
direction = [[0,1],[0,-1],[-1,0],[1,0]]
n,k = map(int,input().split())
data = []
dot = []
for i in range(n):
    data.append(list(map(int,input().split())))
for j in range(k):
    a,b,c = map(int,input().split())
    dot.append([a-1,b-1,c-1])
for i in range(n):
    data[i] = [2]+data[i]+[2]
data = [[2]*(n+2)] + data + [[2]*(n+2)]
socket = [[[] for _ in range(n)] for _ in range(n)]
for i,a in enumerate(dot):
    x,y,d =a
    socket[x][y].append(i)
flag = True
result = 1


def check():
    for i in range(n):
        for j in range(n):
            if len(socket[i][j]) >= 4:
                return False
    return True

def white(idx):
    x,y,d = dot[idx]
    I = socket[x][y].index(idx)
    nx,ny = x+direction[d][0],y+direction[d][1]
    C = socket[x][y][I:]
    for n1 in C:
        nd = dot[n1][2]
        dot[n1] = [nx,ny,nd]
    dot[idx] = [nx,ny,d]
    socket[nx][ny] += (socket[x][y][I:])
    del socket[x][y][I:]

def red(idx):
    x,y,d = dot[idx]
    I = socket[x][y].index(idx)
    nx,ny = x+direction[d][0],y+direction[d][1]
    C = socket[x][y][I:]
    for n1 in C:
        nd = dot[n1][2]
        dot[n1] = [nx,ny,nd]
    socket[nx][ny] += list(reversed(socket[x][y][I:]))
    del socket[x][y][I:]

def blue(idx):
    x,y,d = dot[idx]
    if d%2 == 1:
        d-=1
    else:
        d+=1
    dot[idx] = [x,y,d]
    nx,ny = x+direction[d][0],y+direction[d][1]
    if data[nx+1][ny+1] == 2:
        return
    elif data[nx+1][ny+1] == 1:
        red(idx)
    else:
        white(idx)

def operation(lst):
    global flag
    for i in range(len(lst)):
        x,y,d = lst[i]
        nx,ny = x+direction[d][0],y+direction[d][1]
        if data[nx+1][ny+1] == 1:
            red(i)
        elif data[nx+1][ny+1] == 2:
            blue(i)
        else:
            white(i)
        if not check():
            flag = False
            break


while True:
    operation(dot)
    if flag == False:
        break
    if result > 1000:
        result = -1
        break
    result += 1

print(result)