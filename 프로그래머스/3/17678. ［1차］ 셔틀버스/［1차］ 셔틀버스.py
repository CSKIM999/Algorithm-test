'''
우선 마지막 차가 될 때 까지 차를 보낸 뒤에 생각해야할 것 같음.
조건에 맞춰서 차를 보낸다.
1. 차가 가득 차면 보낸다.
2. 시간이 지나면 보낸다.
이후 시간이 지났지만 타지 못한 사람은 그대로 줄에 서있는다.
만약 마지막 차인데 내가 맨 뒤에섰을 때 타지 못한다면 마지막에 탄 사람보다 1분만 더 일찍나오면 된다.
'''
def busTimer(index,term):
    h,m = 9,0
    value = term * index
    sh,sm = value // 60, value % 60
    rh,rm = f'{h+sh}', f'{m+sm}'
    return f'{rh.zfill(2)}:{rm.zfill(2)}'
def justOneMinute(time):
    h,m = list(map(int,time.split(':')))
    if m - 1 < 0:
        h = f'{h-1}'
        m = '59'
    else:
        h = f'{h}'
        m = f'{m-1}'
    return f'{h.zfill(2)}:{m.zfill(2)}'
    
def solution(n, t, m, timetable):
    timetable.sort()
    userIndex = 0
    for i in range(n):
        busCount = 0
        busTime = busTimer(i,t)
        while busCount < m and userIndex < len(timetable):
            now = timetable[userIndex]
            if busTime >= now:
                userIndex += 1
                busCount += 1
            else:
                break
    if busCount == m:
        index = min(len(timetable)-1,max(userIndex-1,0))
        return justOneMinute(timetable[index])
    else:
        return busTime
    