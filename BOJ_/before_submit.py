from heapq import heappop, heappush
import sys
input = sys.stdin.readline
hpop, hpush = heappop, heappush
while True:
    I = list(map(int, input().split()))
    if I[0] == 0:
        break
    I.append(0)
    result = 0
    ostart = {}
    inorder = []
    height = 0
    for i in range(1, I[0]+2):
        now = I[i]
        if now > height and now > 0:
            height = now
            hpush(inorder, -now)
            ostart[now] = i
        elif now < height:
            bi = 1e9
            while inorder:
                p = -hpop(inorder)
                if p <= now:
                    hpush(inorder, -p)
                    break
                if bi > ostart[p]:
                    bi = ostart[p]
                point = (i - ostart[p])*p
                if point > result:
                    result = point
                ostart.pop(p)
            if now not in ostart:
                ostart[now] = bi
                hpush(inorder, -now)
                height = now
    print(result)
