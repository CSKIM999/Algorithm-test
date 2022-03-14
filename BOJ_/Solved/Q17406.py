from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q17406
https://www.acmicpc.net/problem/17406
#######  TODAY  #######
##### 2022. 03. 11 #####
GIVEN ) N*M 크기의 배열에 숫자가 들어있고 그 안의 배열을 회전시키고자 한다.
        한칸씩 들어가며 불가능할 때 까지 시계방향으로 회전시킨다
        회전은 회전연산자에 따르며 회전연산자 R,C,S 는 다음과 같다.
        (R-S,C-S)부터 (R+S,C+S) 까지의 정사각 배열을 한칸씩 들어가며 회전시킨다
        그리고 주어진 회전 연산들을 한번씩 모두 사용했을 때
        가능한 각 행들의 합의 최솟값을 출력하라
INPUT ) 첫째 줄에 N,M,K 가 주어지고
        이후 N 개의 줄에 배열의 숫자들
        그리고 K개의 줄에 회전 연산정보 R,C,S 가 주어진다.
OUTPUT) 배열의 행합 최솟값을 출력하라
Approach )  배열회전은 어렵지 않다
            그리고 K의 수가 최대 6 이므로 PERMUTATION 을 사용해도 무방할 듯 하다.
'''
'''
필요 :  바깥부터 안쪽으로 한줄씩 들어오며 돌리기
        연산 경우의수 구하기
        경우의수 바탕으로 돌리기
'''
# import sys
# input = sys.stdin.readline

from itertools import permutations
N,M,K = list(map(int,input().split()))
table = []
rt = []
result =1e9
for i in range(N):
    table.append(list(map(int,(input().split()))))
for i in range(K):
    rt.append(list(map(int,(input().split()))))
get = list(permutations(rt,K))
def rot(table,lst):
    global result
    for x,y,c in lst:
        x = x-c-1
        y = y-c-1
        c = c*2+1
        for j in range(c):
            l,u,r,d = [i[y+j] for i in table[x+j:x+c-j]],table[x+j][y+j:y+c-j],[i[y+c-1-j] for i in table[x+j:x+c-j]],table[x+c-1-j][y+j:y+c-j]
            ll,uu,rr,dd = l[1],u[-2],r[-2],d[1]
            tl,tr = l[1:]+[dd],[uu]+r[:-1]
            table[x+j][y+j:y+c-j],table[x+c-1-j][y+j:y+c-j] = [ll]+u[:-1], d[1:]+[rr]
            # print(tl,tr)
            for i in range(len(tl)):
                table[x+j+i][y+j] = tl[i]
                table[x+j+i][y+c-j-1] = tr[i]
            if 2<=len(l)<=3:
                break
    for i in table:
        result = min(result,sum(i))
for cs in get:
    rot([i[:] for i in table],cs)
print(result)

'''
1 트 SOLVE
'''