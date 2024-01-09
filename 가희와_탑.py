n,a,b = list(map(int,input().split()))
table = [0]*n

if a+b > n+1:
    print(-1)
else:
    if a == b:
        temp = list(range(1,a)) + list(range(a,0,-1))
        for i in range(len(temp)):
            table[-i-1] = temp[i]
        for i in range(n-(2*a-1)):
            table[i] = 1
    else:
        if a > b:
            arrA = list(range(1,a+1))
            arrB = list(range(b-1,0,-1))
            arr = arrA + arrB
            diff = n - len(arr)
            table = [1]*diff + arr
                
        else: # a < b
            arrB = list(range(b-1,0,-1))
            
            if a != 1:
                arrA = list(range(1,a))
                arr = arrA + [b] + arrB
                diff = n - len(arr)
                table = [1]*diff + arr
            else:
                arrA = [1]*(n-b+1)
                arrA[0] = b
                table = arrA + arrB

    print(' '.join(map(str,table)))
