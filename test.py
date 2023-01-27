play_time, adv_time, logs = "99:59:59", "25:00:00", [
    "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]


def solution(play_time, adv_time, logs):
    def convert(num):
        if num < 10:
            return f"0{num}"
        return f"{num}"

    def time_to_sec(string):
        h, m, s = list(map(int, string.split(':')))
        sec = h*3600+m*60+s
        return sec
    pt = time_to_sec(play_time)
    at = time_to_sec(adv_time)
    dic = []
    for index, item in enumerate(logs):
        start, end = list(item.split("-"))
        start, end = time_to_sec(start), time_to_sec(end)
        dic.append((start, index, True))
        dic.append((end, index, False))
    sumCount = {i: 0 for i in range(pt+1)}
    dic.sort()
    onTable = set()
    dl = len(dic)
    index = 0
    for i in range(pt):
        if i == 5458:
            pt
        time, node, HorT = dic[index]
        if i == time:
            if HorT:
                onTable.add(node)
            else:
                onTable.remove(node)
            while True:
                index += 1
                if index == dl:
                    break
                time, node, HorT = dic[index]
                if i == time:
                    if HorT:
                        onTable.add(node)
                    else:
                        onTable.remove(node)
                else:
                    break
        sumCount[i] = len(onTable)
        if index == dl:
            break
    mPoint = [0, 0, 0]
    point = 0
    for i in range(at+1):
        point += sumCount[i]
    if point > 0:
        mPoint = [point, 0, at]
    head, tail = at, 0
    for _ in range(at, pt+1):
        try:
            if point > mPoint[0]:
                mPoint = [point, tail, head]
            point -= sumCount[tail]
            point += sumCount[head]
            head += 1
            tail += 1
        except KeyError:

            break
    h = mPoint[1]//3600
    m = (mPoint[1]-3600*h)//60
    s = (mPoint[1]-3600*h-60*m)

    return f"{convert(h)}:{convert(m)}:{convert(s)}"
