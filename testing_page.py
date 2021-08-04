from collections import deque
Data = deque()
Data.appendleft(1)
Data.appendleft(0)

print(Data)
Data = list(Data)
print(Data)
