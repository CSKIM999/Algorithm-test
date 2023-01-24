def solution(N, number):
    answer = -1
    if N == number:
        return 1

    def cal(lst1, lst2):
        returnSet = set()
        for i in lst1:
            for j in lst2:
                item1, item2 = max(i, j), min(i, j)
                summary = [item1+item2, item1-item2, item1*item2, item1//item2]
                for item in summary:
                    if item <= 0:
                        continue
                    if item == number:
                        return returnSet, True
                    returnSet.add(item)
        return returnSet, False

    dic = {}
    dic[1] = [N]

    temp = f'{N}'
    for i in range(2, 9):
        dic[i] = set()
        temp += f'{N}'
        if number == int(temp):
            return i
        else:
            dic[i] = set([int(temp)])

        hist = set()
        for j in range(1, i):
            for k in range(1, i):
                if j+k != i:
                    continue
                t_hist = [j, k]
                t_hist.sort()
                t_hist = tuple(t_hist)
                if t_hist in hist:
                    continue
                hist.add(t_hist)

                a, b = dic[j], dic[k]
                get, flag = cal(a, b)
                if flag:
                    return i
                dic[i].update(get)

    return answer


print(solution(5, 12))


'''
9ood
'''
