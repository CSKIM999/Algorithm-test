import heapq
from collections import deque

jobs = [[0, 3], [1, 9], [2, 6]]

operation = deque()
standby = heapq()

heapq.heappush(jobs[1])