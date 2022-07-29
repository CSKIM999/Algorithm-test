import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
res = 1e10
h,t = 0,1
while True:
    d = lst[t]-lst[h]
    if d < m:
        if t < n-1:
            t += 1
        else:
            h += 1
            if h == t:
                break
    elif d > m:
        res = min(d,res)
        h +=1
        if h == t:
            if t < n-1:
                t +=1
            else:
                break
    elif d == m:
        res = m
        break
print(res)
