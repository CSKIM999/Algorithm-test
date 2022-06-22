from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q9370
#######  TODAY  #######
##### 2022. 06. 21 #####
GIVEN ) 한 무리가 특정 노드에서 출발하여 무작위 목적지로 이동하는것을 추리하라.
        해당 무리는 목표 노드로 항상 최단거리로 이동하며 우리는 그들의 목저지 후보군을 가지고있다.
        한가지 단서는 어느 도로를 지났는지 알 수 있다는 점.
        주어진 단서를 통해 무리가 어디로 이동하는지 추측하라
INPUT ) 첫째 줄에 테스트 케이스의 수 T ( 1<= T <= 100 ) 가 주어진다
            >>> 각 테스트케이스의 첫번째 줄에 n,m,t ( 2<= n <= 2,000 ) // ( 1 <= m <= 50,000 ) // ( 1 <= t <= 100 )
            가 주어진다. 각각 교차로, 도로, 목적지 후보의 개수 를 뜻한다
            >>> 두번째 줄에 s,g,m 가 주어진다. s는 무리의 출발지, g,h 는 지나갔다고 특정가능한 도로
            >>> 그다음 m 개의 줄에 a,b,d 가 주어진다. ( 1 <= a < b <= n  //  1 <= d <= 1,000 ) 가 주어지며 a,b 사이에 d 의 도로가 있다는 뜻
            각 노드 사이에는 2개 미만의 도로가 존재하며 g,h 사이의 도로는 무조건 존재한다. 
OUTPUT) 목적지 후보군을 공백을 구분으로 오름차순 정렬하여 출력

Approach )  다익스트라 ++ 특정노드 지날때 플래그처리
'''

''' 
구동은 되나, 시간초과풀이.
s,g,h 다익스트라 3번돌리기가 최선인듯.

import sys
input = sys.stdin.readline
import heapq
hpush = heapq.heappush
hpop = heapq.heappop


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    s, g, h = s-1, g-1, h - 1
    dest = []
    data = [[] for _ in range(n)]
    for i in range(m):
        a, b, d = map(int, input().split())
        a, b = a-1, b-1
        data[a].append((d, b))
        data[b].append((d, a))
    for i in range(t):
        dest.append(int(input()))

    q = [[0,s]]
    dist = [[1e9,0] for _ in range(n)]
    dist[s] = [0,0]
    while q:
        nowDist, now = hpop(q) #방문한 현재 노드와 출발지부터 현재노드까지의 거리
        if nowDist > dist[now][0]: # 만약 큐에 있는동안 현재 노드까지의 거리가 갱신된경우
            continue
        for x,y in data[now]: # x: 지금노드부터 해당노드까지의 거리, y: 연결된 노드

            #x+현재노드까지의 최소거리가 출발지부터 연결노드까지의 최소거리보다 작거나 같은가
            if dist[y][0] >= dist[now][0] + x:
                if dist[y][0] == dist[now][0] + x:
                    if not dist[now][1] and [y,now] not in [[g,h],[h,g]]:
                        continue
                if dist[now][1] or [y,now] in [[g,h],[h,g]]:
                    dist[y] = [dist[now][0] + x, 1]
                else:
                    dist[y][0] = dist[now][0] + x
                    if dist[y][1]:
                        dist[y][1] = dist[now][1]
                hpush(q,[dist[now][0] + x,y])

    dest.sort()
    answer = []
    for i in dest:
        if dist[i-1][1]:
            answer.append(f'{i}')
    print(' '.join(answer))
'''