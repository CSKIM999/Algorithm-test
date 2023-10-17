from collections import deque
def solution(n, wires):
    i = 0
    table = [[] for _ in range(n)]
    answer = 1e9
    for i,j in wires:
        i,j = i-1,j-1
        table[i].append(j)
        table[j].append(i)
    
    for i in range(n-1):
        a,b = wires[i]
        a -=1
        b -=1
        table[a].remove(b)
        table[b].remove(a)
        link = [None for _ in range(n)]
        for j in range(n):
            now = link[j]
            q = deque()
            if now == None:
                link[j] = j
                for k in table[j]:
                    q.append(k)
                while q:
                    new = q.popleft()
                    if link[new] == None:
                        link[new] = j
                        for k in table[new]:
                            q.append(k)
        c,d = min(link),max(link)
        cc,dc = link.count(c),link.count(d)
        print(link)
        print(c,d)
        print(cc,dc)
        cal = abs(cc-dc)
        answer = min(cal,answer)
        table[a].append(b)
        table[b].append(a)
    return answer

n = 7
wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
solution(n,wires)