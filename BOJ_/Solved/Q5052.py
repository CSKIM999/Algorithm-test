import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q5052
#######  TODAY  #######
##### 2023. 02. 10 #####
GIVEN ) 

INPUT ) 

OUTPUT) 

Approach )  
'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
output = '''
NO
YES
YES
YES
NO
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
NO
NO
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
NO
YES
NO
YES
YES
YES
YES
YES
'''
ye = output.split()
print(len(ye))


def insert(d, v):
    global flag
    if not flag:
        return False
    now = int(v[0])
    if len(v) == 1:
        try:
            test = d[now]
            flag = False
            return
        except KeyError:
            d[now] = {-1: True}
            return
    else:
        try:
            try:
                test = d[now][-1]
                if test:
                    flag = False
                    return
            except KeyError:
                pass
            return insert(d[now], v[1:])
        except KeyError:
            d[now] = {}
            return insert(d[now], v[1:])


n = int(input())
for i in range(n):
    if i == 19:
        n
        pass
    k = int(input().strip())
    arr = []
    dic = {}
    confirm = True
    flag = True
    for _ in range(k):
        string = input().strip()
        if flag:
            insert(dic, string)
        if not flag:
            confirm = False
            pass
    if confirm:
        print("YES")
    else:
        print("NO")

# n = int(input())
# for _ in range(n):
#     k = int(input())
#     arr = []
#     for _ in range(k):
#         arr.append(input())
#     arr = tuple(arr)
#     l = len(arr)
#     flag = False
#     for i in range(l):
#         pivot = arr[i]
#         for j in range(i+1, l):
#             if flag:
#                 break
#             now = arr[j]
#             flag = now.startswith(pivot)
#         if flag:
#             break
#     if flag:
#         print("NO")
#     else:
#         print("YES")
