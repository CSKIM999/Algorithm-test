from collections import deque

info = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5],
         [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
l = len(info)
path = [[] for _ in range(l)]
for node in edges:
    a, b = min(node), max(node)
    path[a].append(b)
    path[b].append(a)

dic = {}
dic[0] = path[0]
q = deque()
q.append(0)
while q:
    now = q.popleft()
    try:
        for x in dic[now]:
            for y in path[x]:
                if y == now:
                    continue
                try:
                    dic[x].append(y)
                except KeyError:
                    dic[x] = [y]
            q.append(x)
    except KeyError:
        continue

q = deque()
q.append([1, 0, dic[0]])
result = 1
while q:
    sheep, wolf, options = q.popleft()
    result = max(result, sheep)
    if sheep == wolf:
        continue
    ol = len(options)
    for i in range(ol):
        temp = options[:]
        now = temp[i]
        ss = 1 if info[options[i]] == 0 else 0
        ws = 1 if info[options[i]] == 1 else 0
        try:
            temp.extend(dic[now])
        except KeyError:
            pass
        temp.remove(now)
        q.append([sheep+ss, wolf+ws, temp[:]])

print(result)
