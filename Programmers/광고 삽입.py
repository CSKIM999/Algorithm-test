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


'''
set + 투포인터로 시간복잡도 최적화
처음엔 투포인터까진 구상했으나 매번 순회하기엔 최대 900억 연산이 나옴.

대충 100시간이어도 360_000초
모든 on-off log를 array에 넣고 정렬. ( max length == 600_000 )
0초부터 max초까지 순회
동시에 array_index, 시청자테이블 관리
i 초에서 array[a_i] 의 값과 같은가? => i초에서 시작하거나 끄는 사람이 있는가?
시작하는 사람이 있다면 시청자테이블 set에 넣어주기 (O(1))
반대로 끈다면 빼주기 ( 마찬가지로 O(1) )
i 초에 한 명 이상의 키고 끄는 주문이 있을 수 있으므로 array[a_i] 의 값이 i 와 다를때까지 반복
반복이 끝나면 시청률테이블[i] = len(시청자테이블) => i초에 보고있는 시청자의 수.
len(set()) 의 시간복잡도 또한 O(1)
시청률테이블이 다 채워지면 투포인터 초기세팅 시작
0초부터 at(adv_time)까지의 시청률테이블 누적합
만약 0 이상이라면 max시청률 갱신
이후 head+1, tail-1 해주며 한칸씩 이동.
이동 후 시청률테이블 누적합을 통해 max시청률 갱신.
생각하기 귀찮은 head&tail KeyError 는 그냥 예외처리
애초에 KeyError가 나온거면 다 끝난것.

'''
