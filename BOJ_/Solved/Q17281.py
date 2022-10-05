import sys
from collections import deque
from itertools import permutations
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q17281
#######  TODAY  #######
##### 2022. 10. 05 #####
GIVEN ) 

INPUT ) 

OUTPUT) 

Approach )  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

a = [2, 3, 4, 5, 6, 7, 8, 9]
lst = list(permutations(a, 8))
n = int(input())
seq = {i: {} for i in range(n)}
for i in range(n):
    temp = list(map(int, input().split()))
    seq[i] = {j: temp[j] for j in range(9)}
m = {1: '1', 2: '10', 3: '100', 4: '1000'}
result = 0
for per in lst:
    per = list(per)
    per.insert(3, 1)
    pi = 0
    point = 0
    for inning in range(n):
        c = 0
        log = "000"
        table = seq[inning]
        q = deque()
        while c != 3:
            hit = table[per[pi]-1]
            pi += 1
            pi %= 9
            if hit != 0:
                q.append(hit)
            else:
                c += 1
        while q:
            log += m[q.popleft()]
        point += log[:len(log)-3].count('1')
    result = max(result, point)

print(result)
