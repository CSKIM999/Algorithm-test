from collections import deque
from functools import partial

########### 리스트 초기화 ###########
# array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# array[1][1] = 'kkk'

# print(array)
# print('')

# n,m = 3,4
# array=[[0]*m]*n
# print(array)
# print('')
# array[1][1] = 'kkk'
# print(array)
# print('')

"""
리스트를 초기화 할 땐 
array =[[0]*m for _ in range(n)] 와 같은 리스트 컴프리헨션을 사용해야함.
만약 위와같이 초기화 할 경우 리스트는 
A=[0,0,0,0] & array = [A , A , A] 와 같이 저장되어버림.
따라서 array[1][1]='kkk' 의 경우 나는 2행 A의 2열의 값을 지정했지만
Python은 3행 모두 A 라는 객채로 보기때문에 모든 A 행의 2열 값이 'kkk' 로 바뀌어버리는 것이다.

하지만 리스트컴프리헨션의 경우
A=[0,0,0,0] & array = [A1 , A2 , A2] 
와 같이 저장되고 따라서 내가 만약
array[1][1]='kkk' 와 같이 2행 A의 2열의 값을 지정한다면
Python 내에서 A2의 2열값을 지정하는것이므로 다른 행에는 영향을 미치지 않는다.
"""


########### 리스트 관련 메소드 ###########
# a=[1,2,3,5,4,5,6]
# a.remove(4)  # 확인할 수 있듯이 remove 메서드는 인덱스 값이 아닌 데이터값을 삭제함.
# print(a)


# a=[1,2,3,4,5,5,6,5]
# a.remove(5)   #실행시켜 볼 경우 맨 앞의 5만 없애는것을 확인 할 수 있음 따라서 모든 값을 지우기위해선
# print(a)      #컴프리헨션을 사용하는것이 빠르다
# print('')
# RemoveSet={3,5}
# result = [i for i in a if i not  in RemoveSet]
# print(result)


####################### 인접리스트 표현방식 #####################

# graph = [[]for _ in range(3)]

# graph[0].append((1,7))
# graph[0].append((2,5))

# graph[1].append((0,7))

# graph[2].append((0,5))

# print(graph)

'''

위와같이 리스트 안의 리스트, 2차원 리스트로 인접리스트를 표현함.
이는 graph = [[0,7,5],[7,0,INF],[5,INF,0]] 와 같이 2차원 인접행렬로 표현한 방식보다
단 1가지 값을 찾아낼 땐 메모리 손실이 크지만, 모든 노드를 순회해야하는 경우 오히려 메모리손실이 적다.

'''


###################### DFS 예제 ######################
'''
Depth First Search [[ 깊이 우선 탐색 ]]
이는 가장 멀리있는 노드를 우선적으로 탐색한 후 원점 노드로 돌아오며 탐색하는 방식
'''
# graph = [
#     [], # 0 번 노드에 연결되어있는 다른노드
#     [2,3,8], # 1 번 노드에 연결되어있는 다른노드
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# # DFS 메서드 정의
# def dfs(graph,v,visited):
#     # 현재 노드의 방문처리
#     visited[v]=True
#     print(v,end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현
# visited = [False]*9

# dfs(graph,1,visited)


###################### BFS 예제 ######################
'''
Breadth First Search [[ 너비 우선 탐색 ]]
알고리즘은 다음과 같다
1. 탐색 시작 노드를 큐에 넣는다
2. 큐에 들어있는 노드를 꺼내(선입선출) 해당 노드와 인접한 노드를 낮은숫자 순서로 큐에 넣는다
3. 방문하지 않은 노드가 없을때까지 2를 반복한다.
'''
# graph = [
#     [], # 0 번 노드에 연결되어있는 다른노드
#     [2,3,8], # 1 번 노드에 연결되어있는 다른노드
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

# def bfs(graph, start, visited):
#     # 큐 Queue 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드 방문처리
#     visited[start] = True
#     # queue 가 빌때까지 반복
#     while queue:
#         # queue 에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         print(v, end=' ')   #아마도 pop 메소드는 queue 에서 뽑아내서 return 값으로 주는듯 함
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소를 큐에 순서대로 삽입(순서는 오름차순으로 알아서 정해짐)
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# visited = [False]*9

# bfs(graph,1,visited)


###################### 정렬 연습 ######################
array = [5,7,9,0,3,1,6,2,4,8]

###################### 선택 정렬 ######################

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1 , len(array)):
#         if array[min_index]>array[j]:
#             array[min_index], array[j] = array[j],array[min_index]


# print(array)

'''
각 정렬마다 최솟값을 찾기위해 탐색하고, 정렬 후 다시 탐색하므로 가장 원시적이고 느린 방법
'''

###################### 삽입 정렬 ######################

# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j]<array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]

# print(array)

'''
만약 거의 정렬되지 않은 상태의 array 라면 선택정렬과 비슷한 시간을 소요하지만, 거의 정렬돼있는 경우
삽입정렬의 효율은 훨씬 더 올라간다.
'''

###################### 퀵 정렬 ######################

'''
정렬 방법을 쓰기에 앞서서 퀵 정렬에 대한 설명을 먼저 짚고 넘어가자
퀵정렬은 기준을 정하고, 그보다 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
여기서 그 기준을 피벗이라 함.

#1 정렬하고자 하는 리스트의 1번째 데이터를 피벗으로 사용
#2 리스트 앞쪽에서 뒷 방향으로 피벗보다 큰 첫번째 데이터를 찾고 뒤에서 역으로 피벗보다 작은 첫번째 데이터를 교환한다
#3 만약 정방향과 역방향이 엇갈릴 경우 더 작은 데이터값과 피벗값을 교환한다
#4 피벗을 기준으로 작은 값, 큰 값의 새로운 2개 리스트가 생성됨
#5 새로 생성 된 리스트에서 재귀함수를 통해 #1부터 다시실행

'''
# # array = [5,7,9,0,3,1,6,2,4,8]
# print(array)

# def quick_sort(array, start, end):
#     if start >= end:
#         return

#     left, right = start+1,end
#     pivot = start
#     while left<=right:
#         while left<=end and array[left] < array[pivot]:
#             left+=1

#         while (right >= start) and (array[right] > array[pivot]):
#             right-=1

#         if left>right:
#             array[pivot],array[right] = array[right],array[pivot]
#         else:
#             array[left],array[right] = array[right],array[left]
#     quick_sort(array,start,right-1)
#     quick_sort(array,right+1,end)


# quick_sort(array,0,len(array)-1)
# print(array)

###################### Python_Ver 퀵 정렬 ######################

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    lst = array[1:]

    left = [x for x in lst if x <=pivot]
    right = [x for x in lst if x >pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))