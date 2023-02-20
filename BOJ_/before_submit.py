n = int(input())
table = list(map(int, input().split()))
left, right = [[table[-1], n-1]], [[table[0], 0]]
dt = {i: [0, 0] for i in range(n)}
pivot = {i: [None, None] for i in range(n)}


def stackAppend(arr, num, now, numi):
    while True:
        if len(arr) == 0:
            if num <= now:
                return
            arr.append([num, numi])
            return
        if arr[-1][0] <= num or arr[-1][0] <= now:
            arr.pop()
        else:
            if num <= now:
                return
            arr.append([num, numi])
            return


for i in range(1, n):
    j = n-(i)
    stackAppend(right, table[i-1], table[i], i-1)
    stackAppend(left, table[j], table[j-1], j)
    lr, ll = len(right), len(left)
    dt[i][0] = lr
    dt[j-1][1] = ll
    if lr != 0:
        pivot[i][0] = right[-1][1]
    if ll != 0:
        pivot[j-1][1] = left[-1][1]

for i in range(n):
    value = sum(dt[i])
    if value:
        l, r = pivot[i]
        if l == None:
            print(value, r+1)
            continue
        if r == None:
            print(value, l+1)
            continue
        al = abs(i-l)
        ar = abs(i-r)
        if al <= ar:
            print(value, l+1)
        else:
            print(value, r+1)
    else:
        print(value)
