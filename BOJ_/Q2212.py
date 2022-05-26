from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2212
#######  TODAY  #######
##### 2022. 05. 26 #####
GIVEN ) 한 개의 직선 상에 N 개의 센서와 K 개의 집중국이 건설된다.
        K 개의 집중국이 수신 가능영역을 최소화하여 그 영역 길이의 최소합을 구하라
        직선상 위치하므로, 원점에서 떨어진 거리값 정수 하나로 센서의 좌표가 표현된다.
        집중국의 수신 가능영역은 0 이상이며, 각 센서의 좌표의 중복은 허용된다.
INPUT ) 첫째 줄에 센서의 개수 N ( 1 <= N <= 10,000 ), 둘째 줄에 집중국의 개수 K ( 1 <= K <= 1,000 )가 주어진다
        셋째 줄에는 N 개의 센서의 좌표가 한개의 정수로 N 개 주어진다.
        각 좌표 사이는 빈칸으로 구분되며 1,000,000 이하의 자연수이다.


OUTPUT) 첫째 줄에 영역의 최소합을 출력하라

Approach )  list = [[index,sum=0],[index,sum=0],[index,sum=0]]
            1. K가 N 보다 작은가?
            >>> YES
            => 센서를 순회하며 현재 index+1 값과의 차가 가장 작은 값 확인
            => 순회가 끝나고 최소값 index와 index+1 노드 수정
            >>> NO
            => return 0 => 각 센서 바로 위에 집중국을 놓을 수 있다.

            1.YES => 수정된 N 의 크기가 K 와 같은가? (1 씩 줄어들기때문에 무조건 지나치게 될 것)
                >>> YES => return
                >>> NO => GoTo 1.

'''
# import sys
# input = sys.stdin.readline

N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst = [[i, 0] for i in lst]

while True:
    if K < N:
        minimum = 1e9
        minIndex = N
        for i in range(N-1):
            dist, summary = lst[i]
            Dist, Summary = lst[i+1]
            if minimum > Dist - dist + Summary:
                minIndex = i
                minimum = Dist - dist + Summary
        dist, summary = lst[minIndex]
        Dist, Summary = lst[minIndex+1]
        lst[minIndex][1] = Dist-dist+Summary
        N -=1
        del lst[minIndex+1]
    else:
        total = sum(i[1] for i in lst)
        print(total)
        break