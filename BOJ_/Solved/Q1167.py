from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1167
#######  TODAY  #######
##### 2022. 03. 16 #####
GIVEN ) 트리의 지금은 트리에서 임의의 두 점 사이의 거리가 가장 긴 것을 말한다 트리의 지름을 구하는 프로그램을 작성하라
INPUT ) 첫째 줄에 트리 정점의 개수 V ( 2 <= V <= 100,000 ) 가 주어지고 둘째 줄부터 V 개 줄에 걸쳐 간선의 정보가 주어지며, 그 정보는 다음과 같다.
        두개의 숫자로 이루어져 있으며, 첫번째 숫자는 정점번호, 두번째 숫자는 정점까지의 거리 이다.
        그리고 각 줄의 끝에는 -1 가 입력으로 주어진다.
OUTPUT) 첫째 줄에 트리의 지름을 출력하라
Approach )  bfs 를 통해 구해볼예정
'''
# import sys
# input = sys.stdin.readline

from collections import deque

V = int(input())

data = [[] for _ in range(V+1)]

for i in range(V):
    temp = list(map(int,input().split()))
    now = temp[0]
    for j in range(1,len(temp)-1,2):
        data[now].append([temp[j],temp[j+1]])

result= 0

start = 1
end = 0
startb4 = 1
while True:
    q = deque([])
    hist = [0 for _ in range(V+1)]
    hist[start] = -1
    for i in data[start]:
        q.append(i)
    while q:
        a,b = q.popleft()
        hist[a] = max(hist[a],b)
        if hist[a]>hist[end]:
            end = a
        for c,d in data[a]:
            if not hist[c]:
                q.append([c,d+b])

    if result < hist[end]:
        result = hist[end]
    elif result == hist[end]:
        if end == startb4:
            break
    startb4 = start
    start = end
    end = 0
print(result)

'''
1트 SOLVE // 키워드아이디어가 아주 좋았다. 
'''