from collections import deque
from functools import partial

inf = int(1e9)
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
# array = [5,7,9,0,3,1,6,2,4,8]

###################### 선택 정렬 ######################

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1 , len(array)):
#         if array[min_index]>array[j]:
#             array[min_index], array[j] = array[j],array[min_index]


# print(array)

'''
** 선택정렬 **
각 정렬마다 최솟값을 찾기위해 탐색하고, 정렬 후 다시 탐색하므로 가장 원시적이고 느린 방법
'''

###################### 삽입 정렬 ######################

# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j]<array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]

# print(array)

'''
** 삽입정렬 **
만약 거의 정렬되지 않은 상태의 array 라면 선택정렬과 비슷한 시간을 소요하지만, 거의 정렬돼있는 경우
삽입정렬의 효율은 훨씬 더 올라간다.
'''

###################### 퀵 정렬 ######################

'''
** 퀵정렬 **
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

# def quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot = array[0]
#     lst = array[1:]

#     left = [x for x in lst if x <=pivot]
#     right = [x for x in lst if x >pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort(array))

'''
파이썬의 특성을 살린 퀵정렬 방식으로, 앞서 풀어낸 방식에 비해 아주 간결하다
하지만 매번 데이터를 비교하므로 계산 속도는 조금 느리다.


**** 하지만 ****
위의 방법과 같이 맨 앞의 데이터를 피벗으로 삼을때, 만약 이미 대다수가 정렬되어있는 데이터라면
퀵정렬은 매우 느리게 작동한다. 앞서 공부했던 삽입정렬과는 반대되는 셈
'''


###################### 순차 탐색 ######################
'''
순차탐색은 지금까지 해왔던 리스트의 앞부분부터 원하는 검색값을 하나씩 차례대로 비교하는 방법이다.
이는 복잡한 알고리즘을 필요로하지 않으므로 구현또한 매우 간단하다.
기본 메서드에서 count() 메서드 또한 이 순차탐색을 이용한다.
이 파일에선 굳이 알고리즘을 작성하지 않겠다 앞서 말한대로 count() 메서드가 그 순차탐색을 사용하기 때문
'''

###################### 이진 탐색 ######################

'''
*** 이진탐색은 배열 내부의 데이터가 이미 정렬되어있어야만 사용할 수 있는 탐색방법이다.
이진탐색은 배열이 정렬되어있지 않다면 사용할 수 없지만, 만약 정렬되어있다면 순차탐색보다 훨씬 빠르게 값을 찾을 수 있다.

시작점과 끝점의 인덱스를 확인 후 중간점 인덱스의 값 또한 확인한다.
이미 정렬이 되어있다면 중간점을 기점으로 하여 원하는 탐색값은 중간보다 위에 혹은 중간보다 아래에 있을 것이다.
여기서 중간점의 인덱스값이 실수라면 소수점 이하의 값은 버린다.
'''

# array = [0,2,4,6,8,10,12,14,16,18]
# array.sort()

# n = 4

# def binary_search(array, target, start, end):
    
#     if len(array[start:end+1]) == 2 and array[start] != target and array[end] != target:
#         print('Target 값은 Array 안에 없습니다.')
#         return
    
#     mid = (start + end) // 2  #  "//" 연산자는 나누고 소수점 이하는 버리는 연산자
#     if target > array[mid]:
#         binary_search(array,target,mid,end)
#     elif target < array[mid]:
#         binary_search(array,target,start,mid)
#     elif target == array[mid]:
#         print('Target 의 index_number 는 : ' + str(mid))
    
# binary_search(array,n,0,len(array)-1)



###################### 다이나믹 프로그래밍 ######################
'''
여기서 다이나믹이란, 동적 프로그래밍이 아닌, 프로그래밍 구동 중 메모리를 새롭게 할당하는 방법을 의미한다
예를들어 피보나치 수열의 경우 f(n) 을 구하기 위해 f(n-1,n-2) 두 값이 계속해서 필요하게 된다
따라서 큰 수열을 구하고자 할수록 단순한 프로그래밍만으로는 앞서 설명한 대로, 해당 요소를 구성하는
하위 요소값을 또 다시 계산해야하기 때문에 소요시간이 기하급수적으로 늘어나게 된다.
그래서 사용되는 방법이 다이나믹 프로그래밍이다. 이는 [[ 이미 계산한 값을 저장하여 다시 계산하지 않는다 ]]
라는 키워드로 메모리를 조금 더 사용하지만 큰 수의 계산에서는 훨씬 더 빠른 계산속도를 보장한다

여기서 모든 상황에서 다이나믹 프로그래밍이 사용될 순 없고 다음의 조건을 따른다.
** 큰 문제를 작은 문제로 나눌 수 있다
** 작은 문제의 해답은 그것을 포함하는 큰 문제에서도 동일하다
그렇기 때문에 피보나치 수열이 아주 대표적인 다이나믹 프로그래밍의 예제라고 볼 수 있다.
'''


# # 탑다운방식
# d = [0] * 101
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
    
#     if d[x] !=0:
#         return d[x]

#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(100))


# # 바텀 업 방식
# d = [0] * 100

# d[1] = 1
# d[2] = 1
# n=99


# for i in range(3,n+1):
#     d[i] = d[i-1]+d[i-2]

# print(d[n])

'''
다이나믹 프로그래밍의 전형적 형태는 바텀업이다.
'''




###################### 최단 경로 찾기 ######################
'''
최단경로 알고리즘에는 대표적으로 "다익스트라 알고리즘","플로이드 워셜", "벨만 포드 알고리즘" 으로 세가지가 있다.
그중에서 다루고자 하는 알고리즘은 다익스트라 알고리즘과 플로이드 워셜이다.

우선 다익스트라 알고리즘은 기본적으로 그리디 알고리즘에 속한다. 매 번 가장 비용이 적은 노드를 선택하여 반복을 통해 답을 찾기 때문이다.
그 알고리즘은 다음과 같다
1. 출발 노드 설정  => 2. 최단 거리 테이블 초기화 => 3. 방문하지 않은 노드 중 거리가 가장 짧은 노드 선택 =>
=> 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산, 그 값을 통해 거리테이블 갱신 => 5. 모든 노드를 확인할 때 까지 3과 4를 반복
'''

n = 6 # number of nodes

#  **** 튜플은 리스트와 달리 한번 넣은 자료의 수정이 까다롭다. (= 연산자로 불가) 그렇기 때문에 반대로 자신의 코드가 잘못 진행되는지도 판단 가능함
data = [[],[(2,2),(3,5),(4,1)],[(3,3),(4,2)],[(2,3),(6,5)],[(3,3),(5,1)],[(3,1),(6,2)],[]]
visited = [False] * (n+1)
distance = [inf] * (n+1)

distance[0],visited[0] = 0,True
# 각 list 의 [0] 값은 비워두었음 매번 인덱스 설정할 때 +1 하기 귀찮으니까
distance[1] = 0

def get_smallest_index(distance):
    index = 0
    min_val = inf
    for i in range(1,n+1):
        if visited[i] !=True: 
            if distance[i] != 0 and distance[i] < min_val:
                min_val = distance[i]
                index = i
    return index

def travel(node):
    if False not in visited:
        return
    visited[node] =True
    for i in range(len(data[node])):
        w2go = data[node][i][0]
        if distance[w2go] == inf:
            distance[w2go] =  distance[node] + data[node][i][1]
        else:
            distance[w2go] = min((distance[node]+data[node][i][1]),distance[w2go])
    index = get_smallest_index(distance)
    print(distance)
    travel(index)

travel(1)

'''
우선, 책과 다르게 나는 재귀함수를 사용했다. 이 문제에서 사용해도 괜찮았던 이유는 노드의 수가 약 1000개보다 훨씬 적었기 때문이다.
만약 노드의 수가 그보다 더 늘어난다면 재귀함수의 재귀회수 제한을 풀던지 아니면 반복문을 통해 위의 travel()  함수를 반복시켜야 할 것이다.

그리고 이는 비교적 느린 방법의 경로찾기이다. 테스트를 준비한다면 다음에 이어질 다른 방법의 다익스트라 알고리즘 구현방법을 체화 시켜야 한다.
'''