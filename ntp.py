from collections import deque
def solution(arr, processes):

    arr = list(map(int,arr))
    P = []
    for i in processes:
        if i[0] == 'r':
            a = list(map(int,(i.split(' '))[1:]))
            P.append([0]+a)
        else:
            a = list(map(int,(i.split(' '))[1:]))
            P.append([1]+a)

    standby = deque()
    time = 0
    q = deque(P)
    result = []
    TT = 0
    running = []
    count = 0
    def write(a,b,c):
        L = len(arr[a:b+1])
        arr[a:b+1] = [c]*L
    def read(a,b,Count):
        nonlocal result
        result.append(arr[a:b+1]+[Count])

    while True:
        time+=1
        temp = []
        for l in range(len(running)):
            now = running[l]
            if now[2] == time:
                if now[0] == 0:
                    read(now[3],now[4],now[-1])
                else:
                    write(now[3],now[4],now[5])
                temp.append(l)
        temp.sort(reverse=True)
        for i in temp:
            del running[i]
        if not running and not standby and not q:
            break
        if q and time == q[0][1]:
            # standby.append(q.popleft())
            ta = q.popleft()+ [count]
            count += 1
            standby.append(ta)
            
        if not running and standby:
            if 1 in [i[0] for i in standby]:
                f = [i[0] for i in standby].index(1)
                a = standby[f]
                del standby[f]
                a[2] = time+a[2]
                running.append(a)
            else:
                while standby:
                    a = standby.popleft()
                    a[2] = time+a[2]
                    running.append(a)

        elif running and standby: #비어있지 않으나
            if standby[0][0] == 0 and running[0][0] != 1: #들어가려는 프로세스가 읽기일경우
                if 1 not in [k[0] for k in standby]: #스탠바이 중 쓰기프로세스마저 없을 때
                    a = standby.popleft()
                    a[2] = time+a[2]
                    running.append(a)
                else: #있다면
                    pass
            else: #쓰기 프로세스일경우
                pass
        
        if running:
            TT+=1

    result.sort(key=lambda x: x[-1])
    answer = []
    for i in result:
        why = ''
        for j in i[:-1]:
            why += f'{j}'
        answer.append(why)
    answer.append(f'{TT}')


    return answer

print(solution(["1","2","4","3","3","4","1","5"],["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))