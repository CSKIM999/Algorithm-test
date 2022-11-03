given = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]

table = [[0]*10 for _ in range(10)]


def draw(lst):
    ax, ay, bx, by = lst
    flag = False
    for i in range(ax, bx):
        if not flag:
            if not table[i][ay]:
                table[i][ay] = 'u'
            elif table[i][ay] == 'l':       
                flag = True
            elif table[i][ay] == 'r':
                table[i][ay] = 'u'
        elif flag:
            if table[i][ay] == 'r':
                flag = False
                table[i][ay] = 'u'
    for i in range(ay, by):
        if not flag:
            if not table[bx][i]:
                table[bx][i] = 'r'
            elif table[bx][i] == 'u':
                flag = True
        else:
            if table[bx][i] == 'd':
                flag = False
                table[bx][i] = 'r'
    for i in range(bx, ax, -1):
        if not flag:
            if not table[i][by]:
                table[i][by] = 'd'
            elif table[i][by] == 'l':
                table[i][by] = 'd'
            elif table[i][by] == 'r':
                flag = True
        else:
            if table[i][by] == 'l':
                flag = False
                table[i][by] = 'd'
    for i in range(by, ay, -1):
        if not flag:
            if not table[ax][i]:
                table[ax][i] = 'l'
            elif table[ax][i] == 'd':
                flag = True
        else:
            if table[ax][i] == 'u':
                flag = False
                table[ax][i] = 'l'


for item in given:
    draw(item)

a = [print(i) for i in table]
