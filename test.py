order = int(input())

rest = order % 5
cnt = order // 5

if rest == 0:
    print(cnt)

elif rest == 1:
    if cnt == 0:
        print(-1)
    else:
        print(cnt + 1)

elif rest == 2:
    if cnt < 2:
        print(-1)
    else:
        print(cnt + 2)

elif rest == 3:
    print(cnt + 1)

else:
    if cnt == 0:
        print(-1)
    else:
        print(cnt + 2)
