'''
case 1
증가라면 무조건 증가수열밖에 없음
case 2
감소라면 무조건 감소수열밖에 없음

바꿔줘야한다면 0 index 값이 최대 혹은 최솟값이어야함.
쭉 체크하다가 증가하면 증가수열 플래그 감소하면 감소수열 플래그

'''
import heapq
heapq.heapify
n = int(input())
data = list(map(int,input().split()))
b4 = data[0]
uf,df = 0,0
us,ds = 0,0
swap = 0
for i in range(1,n):
    now = data[i]
    if us:
        if b4 > now or now > data[0]:
            us = -1
        b4 = now
    if ds:
        if bf < now or now < data[0]:
            ds = -1
        b4 = now
    if not us and not ds:
        break

    if uf and not us:
        if now < b4:
            uf = i
            us = i
    else:
        if b4 == now:
            continue
        elif b4 < now:
            uf = i
    if df and not ds:
        if now > b4:
            bf = i
            ds = i
    else:
        if b4 == now:
            continue
        else:
            bf = i
    b4 = now
print(us,ds)