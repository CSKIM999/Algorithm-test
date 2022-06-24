import sys
input = sys.stdin.readline
T = int(input())
Tr = []
for _ in range(T):
    func = list(input())
    N = int(input())

    arrInput = input().strip()[1:-1]
    if N>0:
        arr = arrInput.split(',')
        arr = list(map(int,arr))
    else:
        arr = []

    flag = True
    rflag = True
    fm, bm, tm = 0, 0, 0
    res = []
    for f in func:
        if f == 'R':
            flag = not flag
        elif f == 'D':
            if flag:
                fm += 1
                tm +=1
            else:
                bm +=1
                tm +=1
        if tm>N:
            print('error')
            Tr.append('error')
            rflag = False
            break
    if rflag:
        if bm!= 0:
            res =arr[fm:-bm]
        else:
            res = arr[fm:]
        if not flag:
            res.reverse()
        print(str(res).replace(' ',''))