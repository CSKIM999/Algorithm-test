import sys
input = sys.stdin.readline


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
