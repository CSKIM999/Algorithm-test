from collections import deque
import sys
from lib import xprint, Prepare_Coding_Test
# Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q9935
#######  TODAY  #######
##### 2023. 02. 11 #####
GIVEN ) 

INPUT ) 

OUTPUT) 

Approach )  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

# import bisect
input = sys.stdin.readline
string = input().strip()
bomb = input().strip()
bl = len(bomb)
answer = ""
q = deque(string)
compare = deque()
qi = deque()
while q:
    now = q.popleft()
    compare.append(now)
    if len(compare) > bl:
        cleft = compare.popleft()
        qi.append(cleft)
    if ''.join(compare) == bomb:
        compare = deque()
        try:
            for _ in range(bl-1):
                compare.appendleft(qi.pop())
        except IndexError:
            continue
while compare:
    qi.append(compare.popleft())
answer = ''.join(qi)
if answer == '':
    answer = "FRULA"
print(answer)

# l = len(string)
# while string:
#     if i + bl - len(q) >= l:
#         break
#     if i in bombed:
#         i += 1
#         continue
#     q.append(string[i])
#     qi.append(i)
#     if len(q) > bl:
#         q.popleft()
#         qi.popleft()
#     if ''.join(q) == bomb:
#         while qi:
#             bombed.add(qi.popleft())
#         q = deque()
#         i -= bl
#         if i < 0:
#             i = 0
#     else:
#         i += 1
# if len(bombed) == len(string):
#     answer = "FRULA"
# else:
#     for i in range(l):
#         if i not in bombed:
#             answer += string[i]
# print()

# output = '''
# anananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananT
# '''
# print(answer == output.strip())
