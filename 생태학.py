dic = {}
tot = 0
table = set()
while True:
    try:
        now = input()
        tot += 1
        table.add(now)
        try:
            dic[now] += 1
        except KeyError:
            dic[now] = 1
    except EOFError:
        break
# defaultDict 써보기
table = list(table)
table.sort()
for i in table:
    ratio = dic[i] / tot
    ratio *= 100
    ratio = round(ratio,4)
    print(f'{i} {ratio:.4f}')