from collections import deque
value = 100
test = [[0 for _ in range(value)] for _ in range(value)]

test = [[1 if index == 0 else 0 for index, _ in enumerate(j)] for j in test]
test[0] = [1 for _ in range(value)]
# [print(i) for i in test]
for i in range(1, value):
    for j in range(1, value):
        test[i][j] = test[i-1][j] + test[i][j-1]
print(test[-1][-1])
q = deque()


a = set()

a.add((1, 2))
a.add((1, 2))
print(a)
