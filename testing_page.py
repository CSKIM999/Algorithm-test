from collections import deque
from functools import partial

start = [2,3]
queue = deque([start])

print(len(queue))

new_one = [4,3]
new_two = [3,3]
check = [4,3]
check_two = [1,3]

queue.append(new_one)
queue.append(new_two)

print(queue)
print(len(queue))

v = queue.pop()
print(str(v[0]) + '    ' + str(v[1]))
print(queue)

print(len(queue))

if (check in queue) and (check_two not in queue):
    print('a')