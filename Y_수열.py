'''
case 1
증가라면 무조건 증가수열밖에 없음
case 2
감소라면 무조건 감소수열밖에 없음

바꿔줘야한다면 0 index 값이 최대 혹은 최솟값이어야함.
쭉 체크하다가 증가하면 증가수열 플래그 감소하면 감소수열 플래그

'''
from collections import deque
n = int(input())
if n <= 2:
    print(0)


num = list(map(int,input().split()))
q = deque(num)
v = q.popleft()
d = 0
count = 0
while q:
    if count == 4:
        break
    now = q.popleft()
    if d == 0:
        if v < now:
            d = 1
            count +=1
        elif v > now:
            d = -1
            count +=1
        else:
            d = 0
    elif d == 1:
        if now < v:
            d = 0
            count += 1
    elif 

# pCount = 0
# d = 0
# def getDir(idx):
#     if num[idx] < num[idx+1]:
#         return 1
#     elif num[idx] > num[idx+1]:
#         return -1
#     else:
#         if idx+2 < n:
#             return getDir(idx+1)
#         else:
#             return d*(-1)
# d = getDir(0)
# index = 0
# for i in range(1,n-1):
#     if d == 1:
#         if num[i] > num[i+1]:
#             if pCount == 1:
#                 pCount = 2
#                 break
#             else:
#                 pCount = 1
#                 index = i
#                 d = getDir(i+1)
#     else:
#         if num[i] < num[i+1]:
#             if pCount == 1:
#                 pCount = 2
#                 break
#             else:
#                 pCount = 1
#                 index = i
#                 d = getDir(i+1)

# if pCount == 2:
#     print(-1)
# else:
#     print(index+1)