n = 0
k = []
p = []
h = []
while True:
    a = int(input())
    for i in range(a-1):
        if a % (i+1) == 0:
            k.append(i+1)
    p.append(k)
    k = []
    if a == -1:
        break
    else:
        h.append(a)
p = p[:3]

for s in range(len(h)-1):
    if h[s] != sum(p[s]):
        print(h[s], 'is NOT perpect')
        break
    elif h[s] == sum(p[s]):
        for v in range(len(p)):
            print(h[v], " = ", end="")
            for u in range(len(p[v])):
                print(p[v][u], " ", end='')
                if u == (len(p[v]) - 1):
                    print()
                else:
                    # + 출력
                    print("+", end="")
