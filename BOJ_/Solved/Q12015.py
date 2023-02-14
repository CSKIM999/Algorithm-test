import bisect
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q12015
#######  TODAY  #######
##### 2023. 02. 14 #####
GIVEN ) LIS 문제.
INPUT ) 

OUTPUT) 

Approach )  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

bisect = bisect.bisect_left
n = int(input())
arr = list(map(int, input().split()))
lis = []
for i in arr:
    if not lis:
        lis.append(i)
        continue
    if lis[-1] < i:
        lis.append(i)
    elif lis[-1] == i:
        continue
    else:
        index = bisect(lis, i)
        lis[index] = i
print(len(lis))


'''
항상 bisect 로 풀땐 이진탐색 구현방법을 기억해 둘 것.
'''
