import bisect
import sys
input = sys.stdin.readline
bl = bisect.bisect_left
n = int(input())
lst = list(map(int, input().split()))

dic = {}
stack = []
answer = [0]*n
for index, tower in enumerate(lst):
    alphaIndex = bl(stack, tower)
    if alphaIndex == len(stack):
        stack = [tower]
        dic[tower] = index
        continue
    tango = stack[alphaIndex]
    # stack.insert(alphaIndex, tower)
    stack = [tower] + stack[alphaIndex:]
    answer[index] = dic[tango]+1
    dic[tower] = index
print(answer)
'''
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dic = {}
stack = []
answer = ["0"]*n
for index, tower in enumerate(lst):
    while stack:
        top = stack.pop()
        if top > tower:
            answer[index] = f"{dic[top]+1}"
            dic[tower] = index
            stack.append(top)
            stack.append(tower)
            break

    if not stack:
        stack.append(tower)
        dic[tower] = index
        continue
answer = ' '.join(answer)
print(answer)

'''
