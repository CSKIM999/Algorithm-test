from collections import deque
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1039
#######  TODAY  #######
##### 2022. 09. 19 #####
GIVEN ) 1 이상 1,000,000 이하의 정수 N 이 주어진다.
        K 번 숫자의 각 자릿수를 바꿀 수 있을 때, 바꿔서 얻을 수 있는 최대 수를 구하라
        여기서 바꿔진 수가 0 으로 시작할 순 없다.
INPUT ) 첫째 줄에 N과 K 가 주어진다. K 는 10 이하의 자연수이다.
OUTPUT) 최대 수를 출력하고 구할 수 없는 상황이라면 -1 를 출력하라
Approach )
불가능한 경우 => {숫자가 하나뿐인 경우, 맨 앞에 위치할 수가 0 이 되는경우 뿐일 때}
모든 경우의 수는 BFS 로 돌리고 필터링을 거치자.


반복 q:
    현재 n 이 k 보다 큰가? => pass
    
                                                                                         

'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

n, k = input().split()
n, k = list(map(int, n)), int(k)
chklst = [[i, n.count(i)] for i in range(1, 10) if n.count(i) > 0]
chklst.sort(key=lambda x: (-x[0], -x[1]))
if chklst[0][0] == 0:
    del chklst[0]
q = deque()


def findIndex(numlist, w2k):
    l = len(numlist)
    arr = []
    for i in range(l):
        if numlist[i] == w2k:
            arr.append(i)

    return arr


result = -1
flag = True
if len(n) == 1:
    flag = False

if flag:
    q.append([n, 0, 0, [i[:] for i in chklst]])
    while q:
        now, pivot, count, src = q.popleft()
        if count >= k:
            # 총 k 번 정렬 완료한 경우 => result 값 max처리
            get = int(''.join(map(str, now)))
            result = max(result, get)
            continue
        if src == []:
            # 정렬은 끝났으나 횟수가 남은경우
            temp = now[:]
            temp[-1], temp[-2] = temp[-2], temp[-1]
            if temp[0] == 0:
                continue
            q.append([temp[:], pivot, count+1, [i[:] for i in src]])
            continue
        node = src[0][0]
        src[0][1] -= 1
        if src[0][1] == 0:
            del src[0]

        nodeIndex = findIndex(now, node)

        for i in nodeIndex:
            temp = now[:]
            if i < pivot:
                continue
            elif i == pivot:
                q.append([now[:], pivot+1, count, [i[:] for i in src]])
                continue
            else:
                if temp[i] == 0:
                    continue
                temp[i], temp[pivot] = temp[pivot], temp[i]
                q.append([temp[:], pivot+1, count + 1, [i[:] for i in src]])


print(result)


'''
무난하게 1트 솔브
간만에 푸니까 살짝 오래걸리긴 함.
풀기전에 플로우부터 적고 푸는연습 다시해야할듯
'''
