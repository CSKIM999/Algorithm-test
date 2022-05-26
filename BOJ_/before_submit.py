import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst = [[i, 0] for i in lst]

while True:
    if K < N:
        minimum = 1e9
        minIndex = N
        for i in range(N-1):
            dist, summary = lst[i]
            Dist, Summary = lst[i+1]
            if minimum > Dist - dist + Summary:
                minIndex = i
                minimum = Dist - dist + Summary
        dist, summary = lst[minIndex]
        Dist, Summary = lst[minIndex+1]
        lst[minIndex][1] = Dist-dist+Summary
        N -=1
        del lst[minIndex+1]
    else:
        total = sum(i[1] for i in lst)
        print(total)
        break