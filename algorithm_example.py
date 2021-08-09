
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

import heapq
inf = int(1e9)
n,m = 6,7
give = [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]
data = [[] for _ in range(n+1)]
table = [[inf,i] for i in range(n+1)]
for i,j in give:
    if j not in data[i]:
        data[i].append(j)
        data[i].sort()
    if i not in data[j]:
        data[j].append(i)
        data[j].sort()
q = [(0,1)]
table[1][0] = 0
table[0][0] = 0
Max = 0
while q:
    dist, node = heapq.heappop(q)
    if table[node][0] < dist:
        continue

    for i in data[node]:
        cost = dist + 1
        if cost < table[i][0]:
            table[i][0] = cost
            heapq.heappush(q,(cost,i))
            Max = max(Max,cost)

result = [ j for i,j in table if i == Max]
print(f'{result[0]} {Max} {len(result)}')

'''
간단한 다익스트라 알고리즘으로 풀어보았다. 그 중 그나마 기억에 남는 새로운 방법은 마지막에 Max index 를 찾기 위해서 list comprehension 을
사용한 for-if 조건문을 사용한 것과, Python 3.6 부터 적용된 f-string 의 사용이다.
'''