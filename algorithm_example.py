
###############################################################################################################
############################################   Q37 _ 플로이드     #############################################
###############################################################################################################
'''
Given ) N (1 <= N <= 100) 개의 도시가 있고 한 도시에서 출발하여 다른 도시에 도착하는 m(1<=m<=100,000) 개의 버스가 있다.
        각 버스는 한번 사용할 때 필요한 비용이있다. 모든 도시의 쌍에 대해서 도시 A에서 B 로 가는데 필요한 비용의 최솟값을
        구하는 프로그램을 작성하라.
Input ) 첫째 줄에 도시의 개수 N (1 <= N <= 100) 이 주어진다
        둘째 줄에 버스의 개수 m (1 <= m <= 100,000) 이 주어진다
        셋째 줄부터는 버스의 정보가 주어진다. " 출발도시 / 도착도시 / 소요비용 " 순으로 공백으로 구분되어 주어짐
        시작도시와 도착도시를 연결하는 노선은 하나 이상이다.
Output) n개의 줄을 출력해야한다. i번째 줄에 출력하는 j번째 숫자는 i에서 j 로 이동하는 최소비용이며 i==j 일 경우 0 이다
'''

'''
1회차 > 모든 도시에서 모든 도시까지의 거리, 문제이름 "플로이드"
        플로이드 워셜 알고리즘을 사용하라는 문제이다.
'''

# inf = 1e9
# N = 5
# m = 14
# A = [[ 1, 2, 2],[ 1, 3, 3],[ 1, 4, 1],[ 1, 5, 10],[ 2, 4, 2],[ 3, 4, 1],[ 3, 5, 1],[ 4, 5, 3],[ 3, 5, 10],[ 3, 1, 8],[ 1, 4, 2],[ 5, 1, 7],[ 3, 4, 2],[ 5, 2, 4]]
# data = [[inf]*N for _ in range(N)]
# for x,y,z in A:
#     if data[x-1][y-1] == inf:
#         data[x-1][y-1] = z
#     else:
#         data[x-1][y-1] = min(data[x-1][y-1],z)

# for i in range(N):
#     for j in range(N):
#             for k in range(N):
#                 if k == j:
#                     data[j][k] = 0
#                 else:
#                     data[j][k] = min(data[j][k],data[j][i]+data[i][k])

# print(data)
            
'''
1회차 > 대표적이란 말도 창피할정도로 그냥 플로이드워셜 알고리즘 문제다. 플로이드워셜 알고리즘은 구현이 매우 쉽다 32-38 line 만 기억하고 있다면
        어떤 문제에서든지 구현이 가능하다. 하지만 나는 ijk 의 순서와 왜 그런지 다시 생각해내느라 시간이 꽤나 걸렸다.
'''



###############################################################################################################
###########################################   Q38 _ 정확한 순위     ###########################################
###############################################################################################################
'''
Given ) 학생 N 명의 성적데이터를 분실하고 비교결과만을 보유중이다. 비교결과를 토대로 성적순위를 유추할 수 있는 학생의 수를 return하라
Input ) 첫째 줄에 학생들의 수 N (2<= N <= 500)과 두 학생의 성적을 비교한 횟수 M( 2<= M <= 10,000 ) 이 주어진다.
        다음 M 개의 줄에는 두 양의 정수 A,B 가 주어지는데, A 가 B 보다 성적이 낮다는것을 의미한다.
Output) 순위를 정확히 유추할 수 있는 학생수를 출력하라
'''

# # n,m = map(int,input().split())
# n = 6
# data = [[] for _ in range(n+1)]
# dp = [[set(),set()] for _ in range(n+1)]
# give = [[1,5],[3,4],[4,2],[4,6],[5,2],[5,4]]
# for a,b in give:
#     dp[b][0].add(a)
#     dp[a][1].add(b)

# def AddAll(number,ud):
#     result = set()
#     for i in dp[number][ud]:
#         result.add(i)
#         if len(dp[i][ud]) != 0:
#             return result.union(AddAll(i,ud))

#     return result

# for i in range(n+1):
#     if dp[i][0] != 0:
#         for j in dp[i][0]:
#             rt = AddAll(j,0)
#             dp[i][0] = dp[i][0].union(rt)
#     if dp[i][1] != 0:
#         for j in dp[i][1]:
#             rt = AddAll(j,1)
#             dp[i][1] = dp[i][1].union(rt)
            
# # dp[4][0] = dp[4][0].union(AddAll(4,0))
# for i in range(n+1):
#     data[i] = len(dp[i][0]) + len(dp[i][1])

# print(dp)
# print(data.count(5))


'''
해답에서는 플로이드 워셜 알고리즘을 추천했다. 하지만 집합 자료형을 통해서 풀어서 정답을 찾았는데, 채점 할 길이 없네
'''



###############################################################################################################
############################################   Q39 _ 화성 탐사     ############################################
###############################################################################################################
'''
Given ) N*N 의 2차원 공간에 각각의 칸을 지나기 위한 비용이 존재한다. 가장 왼쪽 위에 칸에서 가장 오른쪽 아래칸으로 가는
        최소비용을 구하는 프로그램을 작성하라. 탐사기계는 상하좌우 방향으로 1칸 이동할 수 있다.
Input ) 첫쨰 줄에 테스트 케이스의 수 T ( 1<= T <= 10 ) 이 주어진다.
        매 테스트 케이스의 첫째 줄에는 공간의 크기를 나타내는 정수 N ( 2 <= N <= 125 ) 이 주어진다.
        그리고 N 개의 줄에 걸쳐 각 칸의 비용이 주어지며, 공백으로 구분한다. ( 0 <= 비용 <= 9)
Output) 각 테스트케이스마다의 최소비용을 한줄에 하나씩 출력하라
'''

'''
1회차 > 해당 N 의 개수가 125 이하 이므로 플로이드 워셜 알고리즘을 쓰겠다고 생각할 수 있지만, 사실 N^2 가 주어진 데이터이므로,
        최대 N 은 125^2이다. 따라서 플로이드 워셜 알고리즘을 쓰기엔 무리가 있다. 다익스트라 알고리즘을 사용하는것을 추천했다.
'''
# import heapq
# import sys
# input = sys.stdin.readline

# n = 5
# inf = 9876543210

# data = [[3,7,2,0,1],[2,8,0,9,1],[1,2,1,8,1],[9,8,9,2,0],[3,6,5,1,5]]
# table = [[inf]*n for _ in range(n)]

# q = [(data[0][0],0,0)]
# table[0][0] = data[0][0]

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# while q:
#     distance,y,x = heapq.heappop(q)
#     if table[y][x] < distance:
#         continue

#     for i in range(4):
#         ny,nx = y + dy[i], x+dx[i]

#         if ny<0 or ny>=n or nx <0 or nx>=n:
#             continue

#         cost = distance + data[ny][nx]
#         if cost < table[ny][nx]:
#             table[ny][nx] = cost
#             heapq.heappush(q,(cost,ny,nx))

# print(table[4][4])

'''
1회차 > 전에 구현했던 다익스트라 알고리즘을 참고해서 어렵지 않게 구현했다.
'''


###############################################################################################################
#############################################   Q40 _ 숨바꼭질     ############################################
###############################################################################################################
'''
Given ) 숨바꼭질을 하면서 숨을 방을 찾고자 한다. 1~N 번방에 숨을 수 있으며, 술래는 항상 1번방에서 출발한다.
        전체 맵에는 총 M 개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결한다.
        또한 전체 맵은 항상 어떤헛간에서 다른 어떤 헛간으로 도달이 가능하게 주어진다.
        1번 헛간으로부터 최단거리가 가장 먼 헛간이 가장 안전하다고 평가한다. 숨어야하는 헛간의 번호를 출력하는 프로그램을 작성하라
Input ) 첫째 줄에는 N 과 M 이 주어지며 공백으로 구분된다 ( 2<= N <= 20,000 // 1 <= M <= 50,000)
        이후 M 개의 줄에 걸쳐 서로 연결된 두 헛간의 번호가 공백으로 주어진다.
Output) 첫번째 숫자는 숨어야하는 헛간번호를 ( 여러개라면 그 중 가장 작은 숫자 ), 두번째 숫자는 해당 거리 세번째는 같은 거리의 헛간개수
'''
'''
1회차 > 우선 N 이 최대 20,000이므로, 플로이드 워셜 알고리즘은 불가하다. 따라서 다익스트라 알고리즘을 사용해보자
'''

# import heapq
# inf = int(1e9)
# n,m = 6,7
# give = [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]
# data = [[] for _ in range(n+1)]
# table = [[inf,i] for i in range(n+1)]
# for i,j in give:
#     if j not in data[i]:
#         data[i].append(j)
#         data[i].sort()
#     if i not in data[j]:
#         data[j].append(i)
#         data[j].sort()
# q = [(0,1)]
# table[1][0] = 0
# table[0][0] = 0
# Max = 0
# while q:
#     dist, node = heapq.heappop(q)
#     if table[node][0] < dist:
#         continue

#     for i in data[node]:
#         cost = dist + 1
#         if cost < table[i][0]:
#             table[i][0] = cost
#             heapq.heappush(q,(cost,i))
#             Max = max(Max,cost)

# result = [ j for i,j in table if i == Max]
# print(f'{result[0]} {Max} {len(result)}')

'''
간단한 다익스트라 알고리즘으로 풀어보았다. 그 중 그나마 기억에 남는 새로운 방법은 마지막에 Max index 를 찾기 위해서 list comprehension 을
사용한 for-if 조건문을 사용한 것과, Python 3.6 부터 적용된 f-string 의 사용이다.
'''



###############################################################################################################
#############################################     Q41 _ 여행계획     ##########################################
###############################################################################################################
'''
Given ) N 개의 여행지 사이에는 도로가 존재할 수 있으며, 존재한다면 두 여행지는 양방향 통행이 가능하다.
        이 때, 하나의 여행계획을 세우고, 해당 여행지를 모두 방문할 수 있는지 여부를 판단하는 프로그램을 작성하라
Input ) 첫째 줄에 여행지의 수 N 과 계획에 속한 도시의 수 M 이 주어진다. ( 1 <= N,M <= 500 )
        다음 N 개의 줄에 걸쳐 N*N 행렬을 통해 임의의 두 여행지의 서로 연결 여부가 입력된다.
        마지막 줄에 여행계획에 포함된 여행지가 입력된다
Output) 모두 방문이 가능하다면 "YES" 를 불가능하다면 "NO" 를 출력하라
'''
# n,m  = 5,4

# data = [[0,1,0,1,1],[1,0,1,1,0],[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]

# node = [[] for _ in range(n+1)]
# parent = [[i] for i in range(n+1)]
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 1:
#             node[i+1].append(j+1)

# for i in range(1,n+1):
#     if len(node[i]) != 0:
#         for j in node[i]:
#             if parent[i] == parent[j]:
#                 continue
#             parent[j],parent[i] = min(parent[i],parent[j]),min(parent[i],parent[j])
#     else:
#         continue

# print(parent)


# Q = [2,3,4,3]
# for i in range(len(Q)):
#     Q[i] = parent[i+1]
# if Q.count(Q[0]) == len(Q):
#     print('YES')
# else:
#     print('NO')
#     print(Q)

'''
서로소 집합 알고리즘을 사용해서 dp_parent 리스트를 만들고 매번 dp 값을 확인하여 가장 작은 루트노드에 연결되는 하나의 집합으로
만들었다. 제대로 풀었는지는 모르겠다
'''



###############################################################################################################
##############################################     Q42 _ 탑승구     ###########################################
###############################################################################################################
'''
Given ) 공항에 G 개의 탑승구가 있으며, P 개의 비행기가 들어올 예정이다. P개의 비행기를 도킹하다가 도킹이 불가능한 비행기가
        나올 경우 공항의 운행이 중단된다. 최대한 많은 비행기를 도킹하고자 할 때, 비행기의 최대 도킹수를 구하는 프로그램을 작성하라
Input ) 첫째 줄에는 탑승구의 수 G ( 1<= G <= 100,000 ) 가 주어진다
        둘째 줄에는 비행기의 수 P ( 1<= P <= 100,000 ) 가 주어진다
        그 다음 P 개의 줄에 각각의 비행기가 도킹할 수 있는 탑승구의 정보 A 가 주어진다.  A 이하의 탑승구에 도킹할 수 있다는 뜻이다.
        (1<= A <=G)
Output) 최대 도킹수를 구하라
'''
'''
1회차 > 우선 G*P 가 100억을 넘어가므로, O(N^2) 이상의 알고리즘을 사용해선 안된다.
'''


# G,P = 4,6
# data = [2,2,3,3,4,4]
# dp = [i for i in range(G+1)]

# def union_pa(pa,b):
#     if pa[b] != b:
#         return union_pa(pa,pa[b])
#     elif pa[b] == 0:
#         return False
#     else:
#         pa[b] = pa[b-1]
#         return pa

# count = 0
# for i in range(P):
#     if not union_pa(dp,data[i]):
#         print(count)
#         break
#     # union_pa(dp,data[i])
#     count +=1

'''
1회차 > 해답의 서로소집합 알고리즘의 아이디어를 조금 따와서 풀어보았다. dp와 상당히 유사하게 풀어냈다.
        새롭게 사용하고 알게된 것은 line 293 의 if 문 안에 함수를 사용했을 때 만약 False 가 return 되지 않더라도, 가지고있던
        dp 는 새롭게 갱신된다는 사실이었다. 따라서 line 296 에서 한번 더 함수를 실행시키면 한 루프에 두번 함수가 실행되는것.
        bool 형태의 return 을 받아서 if 문에 사용하니 생각보다 더 간결한 코드 작성이 가능했다.
'''



###############################################################################################################
############################################     Q43 _ 어두운 길     ##########################################
###############################################################################################################
'''
Given ) 한 마을은 N 개의 집과 M 개의 도로로 구성되어있다. 모든 도로에는 가로등이 구비되어있는데 해당 도로의 가로등을 하루동안
        키기 위해 소요되는 비용은 해당 도로의 길이와 같다. 정부에서는 일부 가로등을 비활성화하고 마을의 임의의 두 집이
        가로등이 켜진 도로만으로 오갈 수 있게 만들고자 한다. 일부 가로등을 비활성화 할 때 최대 절약비용을 구하는 프로그램을 작성하라
Input ) 첫째 줄에 집의 수 N ( 1 <= N <= 200,000 ) 와 도로의 수 M ( 1<= M <= 200,000 ) 이 주어진다.
        다음 M 개의 줄에 걸쳐 도로에 대한 정보 X,Y,Z 가 주어지며 공백으로 구분된다. ( X 와 Y 사이에 양방향 도로가 있으며, 그 길이는 Z )
Output) 첫째 줄에 일부 가로등을 비활성화 했을 때, 절약 가능한 최대금액을 출력하라
'''
'''
1회차 > 풀기도 전에 최소신장 알고리즘 (크루스칼) 이라는걸 알아봤다. 
        총 도로의 거리 Max 에서 최소신장 알고리즘값 Min 을 빼서 result 를 return 하자
        크루스칼 알고리즘은 서로소 집합 알고리즘과 같이 parents 집합을 사용한다. ( find, union 도 사용한다는 얘기 )
'''
# n,m = 7,11
# data = [[0,1,7],[0,3,5],[1,2,8],[1,3,9],[1,4,7],[2,4,5],[3,4,15],[3,5,6],[4,5,8],[4,6,9],[5,6,11]]
# mapping = []
# parent = [i for i in range(n+1)]
# for x,y,z in data:
#     mapping.append((z,x,y))
# mapping.sort()



# def find_parent(parent,x):
#     if parent[x] != x:
#         return find_parent(parent,parent[x])
#     else:
#         return parent[x]

# def union_parent(parent,x,y):
#     a = find_parent(parent,x)
#     b = find_parent(parent,y)
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b
# total,result = 0,0
# for cost,x,y in mapping:
#     total += cost
#     if find_parent(parent,x) != find_parent(parent,y):
#         union_parent(parent,x,y)
#         result += cost



# print(mapping)
# print(total - result)

'''
1회차 > 정답 // line 357 에서 total - result 가 아닌 자꾸 cost 로 해서 이상한 값이 나왔지만, 코드 자체는 틀리지 않았었음
        크루스칼 알고리즘 전에 서로소집합 알고리즘을 잘 숙지해놓아야 할 듯
'''



###############################################################################################################
#############################################     Q44 _ 행성터널     ##########################################
###############################################################################################################
'''
Given ) 행성은 3차원 좌표로 x,y,z 값이 주어진다. 또한 행성간 연결비용은 델타x,y,z 중 최솟값으로
        각 행성을 잇는 최소비용을 구하는 프로그램을 작성하라
Input ) 첫째 줄에 행성의 개수 N 이 주어짐 ( 1 <= N <= 100,000 )
        다음 N 개 줄에 좌표 x,y,z 가 주어짐
        모든 좌표값은 -1e9 보다 크거나 같고 1e9 보다 작거나 같다.
        좌표값이 겹치는 경우는 없음
Output) 첫째줄에 모든 행성을 터널로 연결하는데 필요한 최소비용을 출력하라
'''

'''
1회차 > 바로 행성의 수가 최대 100,000개 이므로 아마도 시간복잡도에서 문제가 생길것이라고 판단했음
        기본적인 해답에서의 팁은 일반적 크루스칼알고리즘으로는 최대 행성의 개수가 십만개이므로, 최대 100억개까지 계산을 해야할 수도 있단
        점이다. 따라서 몇가지 필터링을 걸쳐 크루스칼알고리즘을 사용할 것을 추천하고있다.
'''
# import sys
# input = sys.stdin.readline
# def find_parent(parent,x):
#     if parent[x] != x:
#         return find_parent(parent,parent[x])
#     else:
#         return parent[x]

# def union_parent(parent,x,y):
#     a = find_parent(parent,x)
#     b = find_parent(parent,y)
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b
# road = []
# result = 0
# n = int(input())
# data = []
# for i in range(n):
#     dt = list(map(int,input().split()))
#     data.append(dt)

# x_d = []
# y_d = []
# z_d = []
# parents = [ i for i in range(n+1)]
# for i in range(1,n+1):
#     x_d.append((data[i-1][0],i))
#     y_d.append((data[i-1][1],i))
#     z_d.append((data[i-1][2],i))
# x_d.sort()
# y_d.sort()
# z_d.sort()

# for i in range(n-1):
#     road.append((x_d[i+1][0]-x_d[i][0],x_d[i][1],x_d[i+1][1]))
#     road.append((y_d[i+1][0]-y_d[i][0],y_d[i][1],y_d[i+1][1]))
#     road.append((z_d[i+1][0]-z_d[i][0],z_d[i][1],z_d[i+1][1]))
# road.sort()

# for cost,x,y in road:
#     if find_parent(parents,x) != find_parent(parents,y):
#         union_parent(parents,x,y)
#         result += cost
# print(result)

'''
1회차 > 거의 내가 풀지 못했다. 크루스칼알고리즘이 살짝 헷갈리니 해결방향이 잡혀도 구현을 못했다.
        일단 풀고나서의 리뷰를 하자면, 크루스칼알고리즘을 위해서는 cost , x , y 가 필요하나 문제에선
        좌표가 주어지고 좌표가 곧 cost였다. 따라서 x축에서의 최소거리 y축에서의 최소거리 z 축에서의 최소거리를
        전처리로 sort 한 후에 크루스칼 알고리즘을 사용했음.
'''



###############################################################################################################
#############################################     Q45 _ 최종 순위     #########################################
###############################################################################################################
'''
Given ) 상당히 불친절한 대회주최측에서 지난 해까지 최종순위를 발표하다가 올해부터는 변동사항만 발표하기로 했습니다
        작년에 팀 13이 팀 6 보다 높았는데 올 해 팀 6이 팀 13보다 순위가 높다면 (6,13) 을 발표한다
        작년 순위와 상대적 순위가 모두 바뀐 모든 팀 목록이 주어질 때 올해 순위를 만드는 프로그램을 작성하라
Input ) 첫 줄에는 테스트케이스의 개수가 주어진다. 테스트케이스는 100개를 넘지 않는다. 각 테스트케이스는 다음과 같이 이루어진다
        >>> 팀의 수 n 을 포함하는 한 줄 ( 2<= n <= 500)
        >>> n개의 정수 t 를 포함하는 한 줄 (1 <= t <= n), t는 작년에 i등을 한 팀의 번호입니다. 1등이 가장 높은등수이며 모든 t 는 다르다
        >>> 상대적인 등수가 바뀐 쌍의 수 m( 0<= m <= 25,000)
        >>> 두 정수 a 와 b 를 포함하고있는 m 줄 ( 1<= a<b <= n )에 걸쳐 상대적 등수바 바뀐 두 팀이 주어진다
Output) 각 테스트케이스에 대해 다음을 출력하라
        >>> n개의 정수를 한 줄에 출력하라. 출력하는 숫자는 올해 순위이며, 1등부터 순서대로 출력하라.
        >>> 만약 확실한 순위를 알 수 없다면, '?' 를 출력하라. 데이터에 일관성이 없어 불가능하다면 'IMPOSSIBLE' 을 출력하라
'''
'''
1회차 > 서로소알고리즘을 통해 paresnts 리스트를 사용해서 루트노드를 찾아가는 방식으로 할까 했으나, 아무래도 아닌것같아서
        해답의 제안을 보니 위상정렬 알고리즘을 통해 자신보다 낮은 노드로 향하는 위상을 만들라고 제시받았다.
        위상정렬 알고리즘의 진행순서
        0. 각 노드에 대해서 진입차수 ( 해당 노드로 향하는 간선의 개수 ) 를 정리한다
        0-1. 진입차수가 0 인 노드를 큐에 넣는다
        1. 큐에서 노드를 꺼낸다.
        2. 꺼낸 노드와 연결된 간선을 제거한다. 그에 따라 진입차수가 0 이 되는 노드를 다시 큐에 넣는다.
        2를 완료했을 때 큐가 빌 때 까지 1과 2를 반복한다.
'''
# from collections import deque
# import sys
# input = sys.stdin.readline
# case = int(input())
# N = []
# give = []
# move = []
# move_data = [[] for _ in range(case)]
# for i in range(case):
#     N.append(int(input()))
#     give.append(list(map(int,input().split())))
#     move.append(int(input()))
#     for j in range(move[i]):
#         move_data[i].append(list(map(int,input().split())))

# for i in range(case):
#     n,data,change = N[i],give[i],move_data[i]
#     cycle = False
#     unknown = False
#     array = [ [] for _ in range(n+1)]
#     for i in range(n):
#         num = data[i]
#         array[num] = array[num] + data[i+1:]

#     for a,b in change:
#         if a in array[b]:
#             array[a].append(b)
#             array[b].remove(a)
#         else:
#             array[b].append(a)
#             array[a].remove(b)

#     degree = [[i,0,False] for i in range(n+1)]
#     for i in range(n+1):
#         degree[i][1] = (n-1)-len(array[i])
#     q=deque()
#     result = []
#     for i,j,k in degree:
#         if j == 0:
#             q.append(i)
#             result.append(i)
            


#     for i in range(n):
#         if len(q) >= 2:
#             unknown = True
#             break
#         elif len(q) == 0:
#             cycle = True
#             break

#         node = q.popleft()
        
#         degree[node][2] = True

#         if degree[node][1] == 0:
#             for i in array[node]:
#                 degree[i][1] -= 1
#                 if degree[i][1] == 0:
#                     q.append(i)
#                     result.append(i)
#         # for i in degree:
#         #     if i[1] == 0 and i[2] == False:
#         #         q.append(i[0])
#         #         i[2] = True
#         #         result.append(i[0])

#     if cycle:
#         print('IMPOSSIBLE')
#     elif unknown:
#         print('?')
#     else:
#         for i in result:
#             print(i,end=' ')
#         print()

'''
1회차 > 상당히 오래걸렸다. 하지만 나름 나의 코드로 짜내서 풀었다. 마지막에 자잘한 오류들이 있긴 했지만, 결국은
        내가 푼 3단계 문제라는것에 상당히 의의를 둔다. 그러나 degree 상태를 bool 형태로 굳이 두지 않았어도 되었었다.

'''

###############################################################################################################
#############################################     Q46 _ 아기 상어     #########################################
###############################################################################################################
'''
Given ) N*N 의 공간에 M 마리의 물고기와 한 마리의 아기상어가 존재한다. 한칸에는 물고기가 최대 1 마리 존재하며
        아기상어와 물고기의 크기는 자연수로 주어진다. 아기상어의 처음 크기는 2 이고 1초에 상하좌우 인접 1칸 이동할 수 있다.
        아기상어는 자신의 크기보다 크기가 큰 물고기가 있는 칸은 지나가지 못하고, 크기가 같은 물고기가 있는 칸은
        지나갈 수만 있으며, 작은 물고기가 있는 칸은 지나감과 동시에 먹는다. 만약 물고기가 먹히면 그 칸은 빈칸이 된다.
        아기상어의 이동규칙은 다음과 같다.
        >>> 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다
        >>> 먹을 수 있는 물고기가 2마리 이상이라면 거리가 가장 가까운 물고기를 먹으러 간다
            >>> 거리는 아기상어가 있는 칸에서 해당 물고기가 있는 칸까지의 칸의 최솟값
            >>> 거리가 같다면, y 값이 작은 물고기를 (위에 있는 물고기) y값마저 같다면 x값이 작은 물고기를 (왼쪽에 있는 물고기) 먹는다
        아기상어는 자신의 크기와 같은 수의 물고기를 먹으면 성장한다. 만약 더이상 먹을 수 있는 물고기가 없다면
        프로그램은 종료된다. 프로그램은 몇초 뒤에 종료될것인가?
Input ) 첫째 줄에 N 이 주어진다 ( 2<= N <= 20 )
        둘째 줄 부터 N 개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0,1,2,3,4,5,6,9 로 주어지며 그 의미는 다음과 같다
        >>> 0 : 빈칸
        >>> 1~6 : 물고기의 크기
        >>> 9 : 아기상어의 위치
Output) 프로그램이 종료되는 시간을 출력하라
'''

'''
1회차 > 물고기의 크기별 위치정보를 리스트로 정리하고 
        case 1 : 먹을 수 있는 물고기가 없을 때
        case 2 : 먹을 수 있는 물고기가 한 마리 일 때
        case 3 : 먹을 수 있는 물고기가 여러마리 일 때
        case 4 : 먹을 수 있는 물고기가 있으나, 큰 물고기로인해 가로막힌 경우
        네가지 케이스를 상정하고, 필요한 기능들을 나열해보자면
        >>> 다음 이동해야 할 위치 선정
        >>> 다음 지점까지 이동할 경로 설정
'''

# n = 20
# data = [
#     [4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1,4,3,2,1],
#     [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
#     ]
# import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))

# feed = [[] for _ in range(7)]
# shark = [2]
# shark_size = 2
# result = 0

# for i in range(n):
#     for j in range(n):
#         if data[i][j] != 0 and data[i][j] != 9:
#             x = data[i][j]
#             feed[x].append((i,j))
#         elif data[i][j] == 9:
#             shark.append([i,j])


# def dfs(now):
#     q = deque()
#     dist = [[-1]*n for _ in range(n)]
#     x,y = now
#     dist[x][y] = 0
#     dx,dy = [0,0,-1,1],[-1,1,0,0]
#     q.append([x,y])
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if 0<= nx and nx <n and 0<= ny and ny < n:
#                 if (dist[nx][ny] > (dist[x][y]+1) or dist[nx][ny] == -1) and shark[0] >= data[nx][ny]:
#                     dist[nx][ny] = dist[x][y]+1
#                     q.append([nx,ny])

#     return dist


# def find_next(dist):
#     temp = 0
#     target = []
#     for i in feed[1:shark[0]]:
#         temp += len(i)
#         for j in i:
#             target.append(j)
#     if temp == 0:
#         return False

#     to_go = []
#     for x,y in target:
#         if dist[x][y] != -1:
#             to_go.append([dist[x][y],(x,y)])
#     to_go.sort()

#     return to_go 

# while True:
#     temp = find_next(dfs(shark[1]))
#     # if temp == False  """""or len(temp) == 0""""": << 이부분이 인덱스에러의 문제였음
#     if temp == False or len(temp) == 0:

#         break
#     for i in range(7):
#         if temp[0][1] in feed[i]:
#             feed[i].remove(temp[0][1])
#             break
#     data[shark[1][0]][shark[1][1]] = 0
#     result += temp[0][0]
#     shark[1] = temp[0][1]
#     data[shark[1][0]][shark[1][1]] = 9
#     shark_size -=1
#     if shark_size == 0:
#         shark[0] +=1
#         shark_size = shark[0]

# print(result)

'''
1회차 > 나는 dfs 를 사용해서 풀어서 시간초과판정을 받았다. 해답에서는 큐를 이용한 bfs 를 추천한다.
        다음에 다시한번 풀어봐야겠다.
        
'''

# import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))

# shark = [2]
# result = 0
# shark_size = 2
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 9:
#             shark.append((i,j))
#             data[i][j] = 0

            

# def find(array,shark):
#     x,y=0,0
#     min_val = 500
#     for i in range(n):
#         for j in range(n):
#             if array[i][j] != -1 and 1<=data[i][j]<shark[0]:
#                 if array[i][j] < min_val:
#                     x,y = i,j
#                     min_val = array[i][j]
    
#     if min_val == 500:
#         return False
#     return [min_val,[x,y]]

# def bfs(data,shark):
#     n = len(data)
#     dist = [[-1]*n for _ in range(n)]
#     q = deque()
#     q.append(shark[1])
#     dist[shark[1][0]][shark[1][1]] = 0
#     dx,dy = [0,0,-1,1],[-1,1,0,0]
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx,ny = x+dx[i] , y+dy[i]
#             if 0<=nx and nx<n and 0<=ny and ny<n and data[nx][ny] <= shark[0]:
#                 if dist[nx][ny] > (dist[x][y]+1) or dist[nx][ny] == -1:
#                     dist[nx][ny] = dist[x][y]+1
#                     q.append([nx,ny])

#     return dist

# while True:
#     ans = find(bfs(data,shark),shark) 
#     # 움직일 때 바뀌어야 할 것
#     # 1. 먹이리스트 갱신 2. 상어위치 갱신 3. 상어있던자리 비우기 4.현재시간 5.상어크기카운트
#     if ans == False:
#         break
#     result += ans[0] # 4
#     nx,ny = ans[1]
#     data[nx][ny] = 0 # 2
#     shark_size -=1
#     shark[1] = (nx,ny)
#     if shark_size == 0:
#         shark[0] +=1
#         shark_size = shark[0]

# print(result)

'''
2회차 > 엄청 많이 시도했지만 Index에러를 받고 아무리봐도 feed리스트 때문인것같아서 feed리스트를 사용하는 방식에서 find 에서 매번 가장 최소거리 먹이를 매번 찾아다니는 방식으로
        바꿔주었다. 역시나 feed 리스트가 문제였다. 하지만 feed 자체는 생각보다 참신한 아이디어같으니 다음에 한번 다시 feed리스트의 인덱스에러를 해결해서 풀어보자
'''


###############################################################################################################
###########################################     Q46 _ 청소년 상어     #########################################
###############################################################################################################
'''
Given ) 4*4 공간에 물고기가 16마리 존재라며 각 물고기는 1 이상 16 이하의 번호를 가지며 8가지 방향을 갖고있다.
        청소년 상어는 주어진 4*4 공간의 (0,0) 에 위치한 물고기를 먹으며 등장하며 상어의 방향은 잡아먹은 물고기의 방향이 된다.
        이후 물고기가 이동하며 물고기의 이동 알고리즘은 다음과 같다.
        >>> 물고기는 번호가 작은 물고기부터 오름차순으로 이동한다. 물고기는 한 칸 이동할 수 있고 상어나 공간을 넘어가지 않는 방향으로 움직일 수 있다.
        >>> 물고기가 이동하려는 칸이 이동이 불가능하다면 반시계방향으로 45' 회전하며 이동 가능한 방향을 찾는다. 만약 없다면 이동하지 않는다.
        >>> 물고기가 다른 물고기가 있는 칸으로 이동할 땐 서로의 위치를 바꾸는 식으로 이동한다.
        
        물고기가 모두 이동하고나서 상어가 이동하며 상어는 현재 방향으로 한번에 여러칸 이동할 수 있다. 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고 방향성을 얻는다
        이동하는 중간에 지나는 칸에 위치한 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동이 불가하며, 더 이상 이동할 칸이 없다면 집으로 간다.
        상어가 이동한 후에는 다시 물고기가 이동하며 이후 이 과정이 반복된다.

Input ) 첫째 줄부터 4개의 줄에 각 칸에 들어있는 물고기의 정보가 1번 행부터 주어진다. 물고기의 정보는 두 정수 a,b 로 이루어지며, 
        a는 물고기의 번호 b는 방향을 의미한다. 방향 b 는 1에서 8까지의 자연수이며 각 순서대로 12시방향에서 반시계방향(↑, ↖, ←, ↙, ↓, ↘, →, ↗ )을 의미한다.

Output) 상어가 먹을 수 있는 물고기 번호 합의 최댓값을 출력하라
'''

'''
1회차 > 우선적으로 물고기의 이동규칙은 크게 어렵지 않아 move 함수로 작성하고 각 칸으로 이동할 때 마다 최댓값의 경우의 수가 달라지므로, dfs로 구성해보자
        move함수는 어차피 순서대로 이동해야하니 큐를 이용해서 (number,(x,y),rotate)로 움직여보자
'''
n =4
Give = [
    [7,6,2,3,15,6,9,8],
    [3,1,1,8,14,7,10,1],
    [6,1,13,6,4,3,11,4],
    [16,1,8,7,5,2,12,2]
]
num_list = [i for i in range(1,17)]
rx = [0,-1,-1,0,1,1,1,0,-1]
ry = [0,0,-1,-1,-1,0,1,1,1]
num_list.remove(Give[0][0])
Give[0][0] = -1
data = [[] for _ in range(4)]
rotate = [[] for _ in range(4)]
for i in range(4):
    for j in range(0,n*2,2):
        data[i].append(Give[i][j])
        rotate[i].append(Give[i][j+1])

def move_fish(rot,x,y,count):
    nx,ny = x + rx[rot], y + ry[rot]
    if 0<= nx < n and 0<= ny <n and data[nx][ny] != -1:
        data[x][y],data[nx][ny] = data[nx][ny],data[x][y]
        rotate[x][y],rotate[nx][ny] = rotate[nx][ny],rotate[x][y]
    else:
        rot += 1
        if rot == 9:
            rot = 1
        count +=1
        if count == 8:
            return None
        return move_fish(rot,x,y,count)


#물고기 움직이기
for num in num_list:
    count = 0
    check = False
    for i in range(4):
        for j in range(4):
            if data[i][j] == num:
                rot = rotate[i][j]
                move_fish(rot,i,j,count)
                check = True
                break
        if check == True:
            break

print(data)
def getlist():
    lst =[]
    for i in range(4):
            for j in range(4):  
                if data[i][j] == -1:
                    rot = rotate[i][j]
                    x,y = i,j
    
    for i in range(1,4):
        nx,ny = x + (rx[rot])*i , y + (ry[rot])*i
        if 0<= nx <n and 0<=ny<n:
            lst.append([data[nx][ny],rotate[nx][ny],nx,ny])
    lst.sort()
    return lst

print(getlist())
