from heapq import heappop, heappush
import sys
from lib import xprint, Prepare_Coding_Test
from bisect import bisect_left as bl
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q6549
#######  TODAY  #######
##### 2022. 10. 06 #####
GIVEN ) 직사각형 여러개가 정렬돼있는 도형 히스토그램에서 가장 넓은 크기의 직사각형을 찾고자 한다.
INPUT ) 한개의 입력에 여러개의 TC 가 주어진다. 각 TC 는 한줄로 이루어지며 맨 처음 직사각형의 수 N ( 100,000 이하의 자연수 )
        그 다음 n 개의 수 ( 10억 이하의 자연수 )가 주어진다.
        입력 마지막 줄에는 0 이 주어진다.
OUTPUT) 각 TC에 대한 가장 넓은 크기의 직사각형 넓이를 출력하라
Approach )  지금 블록보다 큰 블록을 만날땐 inorder에 넣고 작은 블록을 만날땐 새로운 블록보다 큰 inorder 들을 빼야함
'''
sys.setrecursionlimit(25000)
input = sys.stdin.readline
hpop, hpush = heappop, heappush
while True:
    I = list(map(int, input().split()))
    if I[0] == 0:
        break
    I.append(0)
    result = 0
    ostart = {}
    inorder = []
    height = 0
    for i in range(1, I[0]+2):
        now = I[i]
        if now > height and now > 0:
            height = now
            hpush(inorder, -now)
            ostart[now] = i
        elif now < height:
            bi = 1e9
            while inorder:
                p = -hpop(inorder)
                if p <= now:
                    hpush(inorder, -p)
                    break
                if bi > ostart[p]:
                    bi = ostart[p]
                point = (i - ostart[p])*p
                if point > result:
                    result = point
                ostart.pop(p)
            if now not in ostart:
                ostart[now] = bi
                hpush(inorder, -now)
                height = now
    print(result)

'''
자료형 활용의 깊은 고민이 있어야함
'''
