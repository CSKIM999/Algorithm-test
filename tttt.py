# n nums of rows // k selected row //  ( 5 <= n <= 1,000,000 ) ,, 명령 갯수 200,000 이하
# U x // selectrow 의 X 칸 위에 있는 row 선택
# D x // 마찬가지
# C // selected row 삭제 후 바로 아래 row 선택. 만약 삭제행이 마지막 row 일경우 바로 윗행 선택
# Z 최근 삭제 행 복구

from collections import deque
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
q = deque(list(cmd))
n = 8
k = 2
delStack = deque()
tn = n-1
table = [i for i in range(n)]
boolTable = ["O"]*n
# def binarySearch(num,start,end):
#     if end-start<2:
#         return start+1
#     middle=(start+end)//2
#     if table[middle]>num:
#         return binarySearch(num,start,middle)
#     else:
#         return binarySearch(num,middle,end)


selectedRow = k
while q:
    now = list(q.popleft().split())
    if len(now) == 2:
        # D or U
        func,dist = now[0],int(now[1])
        if func == 'D':
            selectedRow = table[selectedRow+dist]
        else:
            selectedRow = table[selectedRow-dist]
    else:
        if now[0] == 'C':
            delStack.append(table[selectedRow])
            
            tn -= 1
            if selectedRow>tn:
                selectedRow = tn
            
        elif now[0] == 'Z': #Z
            last = delStack.pop()
            tn +=1
answer = ''
for i in range(n):
    if i in table:
        answer += 'O'
    else:
        answer += 'X'
print(answer)