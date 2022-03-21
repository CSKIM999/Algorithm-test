import sys
input = sys.stdin.readline
from collections import deque
a = [1,2,3,4,5,6]
b = deque(a)
print(b.index(2))

print(b[1])