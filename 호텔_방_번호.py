'''
테케가 과연 몇개일 것인가
이거 너무 과한거 아니야?
'''

# n,m = list(map(int,input().split()))]
while True:
    try:
        n,m = list(map(int,input().split()))
        res = 0
        for i in range(n,m+1):
            numCount = [0 for _ in range(10)]
            flag = 1
            for j in str(i):
                now = int(j)
                if numCount[now]:
                    flag = 0
                    break
                numCount[now] += 1
            if flag:
                res += 1
        print(res)
    except:
        break