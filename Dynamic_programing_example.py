###############################################################################################################
################################################   Q31 _ 금광   ###############################################
###############################################################################################################
'''
Given ) N*M 행렬 크기의 금광이 있다. 각 칸에는 특정량의 금이 들어가있고 채굴자는 1열부터 시작해서 가장 오른쪽 열
        까지 이동하며 채굴자는 최대크기의 금을 얻어야한다. 채굴자는 오른쪽 위,중앙,아래 세칸으로 움직일 수 있다.
        최대크기 금을 얻는 프로그램을 작성하라
Input ) 첫째 줄에 테스트케이스 T 가 입력됩니다. ( 1 <= T <= 1,000 )
        매 테스트 케이스 첫째 줄에 n 과 m 이 공백으로 구분되어 입력됨. (1 <= N,M <= 20) 
        둘째 줄에 n*m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됨. (0<= 각 위치에 매장된 금의 개수 <= 100)
Output) 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대크기를 출력하라. 테스트케이스는 줄바꿈을 이용해 구분한다.
'''

'''
1회차 > bfs 를 사용하면 될 듯하다. DP 파트이지만 bfs 를 통해서 각 테스트케이스마다의 최댓값을 구해내고자 함
'''
# c = 2
# n,m = [3,4],[4,4]
# data = [[1,3,3,2,2,1,4,1,0,6,4,7],[1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]]
# nxt = [[1,1,1],[1,0,-1]]
# from collections import deque
# #테스트케이스
# for i in range(c):
#     q = deque(data[i])
#     table = [[] for _ in range(n[i])]
#     #data 행렬화
#     for j in range(n[i]):
#         for k in range(m[i]):
#             table[j].append(q.popleft())

#     #bfs 시작
#     result = 0
#     for j in range(n[i]):
#         q.append([j,0,table[j][0]])
#         while q:
#             y,x,value = q.popleft()
#             if x != (m[i]-1):
#                 for k in range(3):
#                     ny,nx = y+nxt[1][k],x+nxt[0][k]
#                     if 0<= ny < n[i] and 0<= nx <m[i]:
#                         nval = table[ny][nx]
#                         q.append([ny,nx,value+nval])
#             else:
#                 result = max(result,value)
#     print(result)

'''
당연히 나와야 할 정답이 안나와서 헤멨다. line 32 의 result = 0 을 line 33 for 문 안에 넣어서 매번 초기화를 시켜서 정답이 안나왔던 것.
해답에서는 bfs가 아닌 새로운 value 행렬을 만들었다 이 방법이 더욱 효과적일 듯 하다.
아무래도 Dp 파트이다보니 Dp 를 사용하는게 맞기도 하고 매우매우 간단하다.
0열은 정해진 값이므로 넣고 1열에는 데이터값과 새로운 행렬의 0열값을 더한 값 중 최댓값을 넣어주는 방식이다.
'''


###############################################################################################################
#############################################   Q32 _ 정수삼각형   ############################################
###############################################################################################################
'''
Given ) 정수로 이루어진 정삼각형 행렬이 있다. 맨 위 꼭짓점부터 시작하여 특정 규칙을 따라 내려오며 더할 때
        가장 큰 수를 만드는 경로를 구하는 프로그램을 작성하라.
        여기서 규칙은 현재 선택된 숫자에서 왼쪽 위 혹은 오른쪽 위와 더해서 큰 수를 가진다.
Input ) 첫째 줄에 삼각형의 크기 n (1<= n <= 500) 이 주어지고
        둘째 줄부터 n+1 번째 줄까지 정수 삼각형값이 주어진다.
Output) 최대합을 출력하라

1회차 > Q31 과 유사한 문제 똑같이 dp_table 을 만들어서 구했음.
'''

# n = int(input())
# data = [[] for _ in range(n)]
# for i in range(n):
#     data[i] = list(map(int,input().split()))

# table = [i[:] for i in data]
# for i in range(1,n):
#     for j in range(len(data[i])):
#         for k in range(2):
#             if 0<= j-k <len(data[i-1]):
#                 val = data[i][j] + table[i-1][j-k]
#                 table[i][j] = int(max(table[i][j],val))
#                 val = 0

# print(max(table[n-1]))
'''
똑같이 line 81 에 int(max(table[i][j],val)) 여기서 int만 씌워주고 print값을 result 가 아닌 마지막 행의 max값으로 바꾸었더니
정답판정을 받았다. 나도 왜 전거가 틀렸는지는 모르겠다.
'''


###############################################################################################################
################################################   Q32 _ 퇴사   ###############################################
###############################################################################################################
'''
Given ) 지금으로부터 N+1 이후에 퇴사 할 예정인 직원이 남은 N 일동안 최대한 많은 상담을 하고자 한다.
        각 일자마다 상담에 걸리는 시간과, 보상금이 정해져있다. 이 때, 만약 1일차에 3일이 소요되는 상담이라면
        2,3 일에는 상담이 불가능하다. 또한 N+1 일에는 퇴사이므로 상담은 N일까지 끝마쳐야한다.
        이 때, 최대금액을 구하는 프로그램을 작성하라.
Input ) 첫째 줄에 N ( 1<= N <= 15 )이 주어진다
        둘째 줄 부터는 N 개의 줄에 T와 P 가 공백으로 구분되어 주어지며, 1일부터 N일까지 순서대로 주어진다.
        ( 1 <= T <= 5 // 1 <= P <= 1,000 )
Output) 최대이익을 출력하라
'''

n = int(input())
data = [[0,0] for _ in range(n)]
for i in range(n):
    a,b = map(int,(input().split()))
    data[i][0],data[i][1] = a,b
dp = [0]* (n+1)
mval = 0
for i in range(n-1,-1,-1):
    index = data[i][0] + i
    if index <= n:
        mval = max(dp[index]+data[i][1],mval)
        dp[i] = mval
        pass
    else:
        dp[i] = mval

print(max(dp))
