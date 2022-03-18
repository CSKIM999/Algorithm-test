from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1068
#######  TODAY  #######
##### 2022. 03. 17 #####
GIVEN ) 트리에서 가장 말단을 리프노드라고한다. 특정 노드를 지웠을 때 리프노드의 갯수를 세는 프로그램을 작성하라
INPUT ) 첫째 줄에 노드의 개수 N 이 주어진다 ( 1<= N <= 50 )
        둘째 줄에 0번 노드부터 N-1 번 노드까지의 각 노드의 부모노드가 주어진다. -1 은 루트노드를 나타낸다.
        셋째 줄에 지울 노드 번호가 주어진다
OUTPUT) 지울 노드를 지웠을 때 리프노드의 갯수를 출력하라
Approach )  딱히 뭐 있나? 입력받은거로 리스트 만들고 지우려는 노드 리스트 초기화하고 bfs 돌리면 되는거 아님?
'''
# import sys
# input = sys.stdin.readline

from collections import deque

N = int(input())
lst = list(map(int,input().split()))
cut = int(input())
data = [[] for _ in range(N)]
root = 0
for i in range(N):
    parent = lst[i]
    if parent == -1:
        root = i
        continue
    if i == cut:
        continue
    data[parent].append(i)
data[cut] = []
q = deque([])
q.append(root)
result = 0

while q:
    Pnode = q.popleft()
    if Pnode == cut:
        continue
    if data[Pnode]:
        for i in data[Pnode]:
            q.append(i)
    else:
        result += 1

print(result)

'''solve'''