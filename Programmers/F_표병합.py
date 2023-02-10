commands = ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2",
            "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]


def solution(commands):
    s, m = "single", "merged"
    table = [[[s, None] for _ in range(51)] for _ in range(51)]
    dic = {}

    def C(r, c):
        if table[r][c][0] == s:
            return [r, c]
        else:
            if type(table[r][c][1]) != list:
                return [r, c]
            return table[r][c][1]

    def U(value1, value2):
        if type(value1) == list:
            r, c = value1
            r, c = C(r, c)
            table[r][c][1] = value2
        else:
            for i in range(51):
                for j in range(51):
                    if table[i][j][1] == value1:
                        table[i][j][1] = value2

    def M(value1, value2):
        ar, ac, br, bc = [*value1, *value2]
        ar, ac, br, bc = [*C(ar, ac), *C(br, bc)]
        if ar == br and ac == bc:
            return
        if table[ar][ac][1] == None:
            value = table[br][bc][1]
        else:
            value = table[ar][ac][1]
        try:
            dic[(ar, ac)].append((br, bc))
        except KeyError:
            dic[(ar, ac)] = [(br, bc)]
        if table[br][bc][0] == m:
            childList = dic[(br, bc)]
            for i, j in childList:
                table[i][j][1] = [ar, ac]
                dic[(ar, ac)].append((i, j))
            dic.pop((br, bc))
            table[br][bc][1] = [ar, ac]
        else:
            table[ar][ac] = [m, value]
            table[br][bc] = [m, [ar, ac]]

    def UM(r, c):
        cr, cc = C(r, c)[:]
        value = table[cr][cc][1]
        try:
            child = dic[(cr, cc)]
            for ir, ic in child:
                table[ir][ic] = [s, None]
            dic.pop((cr, cc))
        except KeyError:
            pass
        table[cr][cc] = [s, None]
        table[r][c] = [s, value]

    def P(r, c):
        r, c = C(r, c)
        value = table[r][c][1]
        if value == None:
            return "EMPTY"
        else:
            return value
    answer = []

    for string in commands:
        SS = list(string.split())
        if SS[0] == "UPDATE":
            try:
                value2 = SS[3]
                value1 = [int(SS[1]), int(SS[2])]
            except IndexError:
                value1 = SS[1]
                value2 = SS[2]
            U(value1, value2)
        elif SS[0] == "MERGE":
            value1 = [int(SS[1]), int(SS[2])]
            value2 = [int(SS[3]), int(SS[4])]
            M(value1, value2)
        elif SS[0] == "UNMERGE":
            r, c = int(SS[1]), int(SS[2])
            UM(r, c)
        elif SS[0] == "PRINT":
            r, c = int(SS[1]), int(SS[2])
            answer.append(P(r, c))
    return answer


print(solution(commands))
