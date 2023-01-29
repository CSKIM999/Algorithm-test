users = [[1, 2000], [10, 10000]]
emoticons = [1000, 1100, 1200, 1300]


def solution(users, emoticons):
    emo = emoticons
    e = len(emo)
    sales = {10: .9, 20: .8, 30: .7, 40: .6}
    pt = [10, 20, 30, 40]
    ticket = [[0, i] for i in range(e)]
    users.sort()

    def check(promo):
        ra = [0, 0]
        pd = {i: 0 for i in pt}
        for p, i in promo:
            for j in range(p+1):
                pd[pt[j]] += emo[i]*sales[pt[p]]
        for w, m in users:
            sp = ((w // 10))*10
            if sp == 0:
                sp = 10
            if sp > 40:
                sp = 40
            if pd[sp] >= m:
                ra[0] += 1
            else:
                ra[1] += pd[sp]
        return ra
    answer = [0, 0]
    flag = True
    while flag:
        if ticket == [[1, 0], [1, 1], [1, 2], [1, 3]]:
            flag
        ra = check(ticket)
        if ra[0] > answer[0]:
            answer = ra[:]
        elif ra[0] == answer[0] and ra[1] > answer[1]:
            answer = ra[:]
        if answer == [1, 3680.0]:
            flag
        i = 0
        while True:
            ticket[i][0] += 1
            p = ticket[i][0]
            if p == 4:
                if i == e-1:
                    flag = False
                    break
                ticket[i][0] = 0
                i += 1
                continue
            break

    return answer


a = '4'
print(type(a))
