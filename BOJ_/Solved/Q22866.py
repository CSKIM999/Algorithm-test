import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q22866
#######  TODAY  #######
##### 2023. 02. 20 #####
GIVEN ) 일직선 상에 건물들이 위치한다.
        바라보는 방향에서 건물들은 일직선 상에 위치하기에 같거나 작은 높이라면 보이지 않는다.
        해당 조건에서 각 건물의 옥상에서 양옆으로 보이는 건물의 수를 찾고자 한다.
        

INPUT ) 

OUTPUT) 

Approach )  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
n = int(input())
table = list(map(int, input().split()))
left, right = [[table[-1], n-1]], [[table[0], 0]]
dt = {i: [0, 0] for i in range(n)}
pivot = {i: [None, None] for i in range(n)}
# 8
# 3 7 1 6 3 5 1 7


def stackAppend(arr, num, now, numi):
    while True:
        if len(arr) == 0:
            if num <= now:
                return
            arr.append([num, numi])
            return
        if arr[-1][0] <= num or arr[-1][0] <= now:
            arr.pop()
        else:
            if num <= now:
                return
            arr.append([num, numi])
            return


for i in range(1, n):
    j = n-(i)
    stackAppend(right, table[i-1], table[i], i-1)
    stackAppend(left, table[j], table[j-1], j)
    lr, ll = len(right), len(left)
    dt[i][0] = lr
    dt[j-1][1] = ll
    if lr != 0:
        pivot[i][0] = right[-1][1]
    if ll != 0:
        pivot[j-1][1] = left[-1][1]

for i in range(n):
    value = sum(dt[i])
    if value:
        l, r = pivot[i]
        if l == None:
            print(value, r+1)
            continue
        if r == None:
            print(value, l+1)
            continue
        al = abs(i-l)
        ar = abs(i-r)
        if al <= ar:
            print(value, l+1)
        else:
            print(value, r+1)  # 항상 index에서 문제가 생긴다.
    else:
        print(value)


'''
이번에도 Index 부분에서 오류가 생김
인덱스 처리에서 헷갈리지 않을 확실한 방법이 좀 필요해보임.
시간낭비도 시간낭비인데 틀리는 경우도 너무 많음


'''
