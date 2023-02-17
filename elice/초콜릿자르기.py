
answer = 0
a = "5 1 4 3 4 2 5 6"
arr = list(map(int, a.split()))
l = len(arr)
s = []
pivot = 0
for i in range(l):
    now = arr[i]
    if now > pivot:
        pivot = now
        if s:
            start = s[-1][0]
            s.append([i, start, now])
        else:
            s.append([i, -1, now])
    else:  # now <= pivot now 가 피벗보다 작으면? 무조건 s 가 있는거 아님?
        pivot = now
        while True:
            if not s:
                s.append([i, -1, now])
                break
            a, st, v = s[-1]
            if v >= now:
                value = (i-st-1)*v
                answer = max(answer, value)
                s.pop()
            else:
                s.append([i, a, now])
                break


while s:
    act, st, val = s[-1]
    value = (l-st-1)*val
    answer = max(answer, value)
    s.pop()

print(answer)

'''
0 index 처리가 헷갈려서 애먹은 문제.
이런건 진짜 시간들이면 안되는건디;;
'''
