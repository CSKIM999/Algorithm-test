import sys
from datetime import datetime,timedelta
input = sys.stdin.readline

n,l,f = list(input().split())
n,f = map(int,[n,f])

l = list(l.split('/'))
d = int(l[0])*24*60
l = list(map(int,l[1].split(':')))
l = l[0]*60 + l[1] + d

dic = {}
plst = []
nameIndex = {}
i = 0
for _ in range(n):
    nowday,nowtime,p,name = list(input().split())
    nowday = list(map(int,nowday.split('-')))
    nowtime = list(map(int,nowtime.split(':')))
    nowday = datetime(nowday[0],nowday[1],nowday[2],nowtime[0],nowtime[1])

    try:
        items = dic[name]
    except KeyError:
        items = dic[name] = {}
        plst.append([0,name])
        nameIndex[name] = i
        i += 1

    try:
        bday = items[p]
        delta = (nowday-bday)
        btime = (delta.seconds // 60) + (delta.days * 60 * 24)
        if btime > l:
            Index = nameIndex[name]
            plst[Index][0] += btime - l
        del dic[name][p]

    except KeyError:
        dic[name][p] = nowday

plst.sort(key=lambda x: x[1])
flag = True
for a,b in plst:
    if not a:
        continue
    print(b,a*f)
    flag = False
if flag:
    print(-1)