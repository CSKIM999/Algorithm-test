n = int(input())
strlst = []
for i in range(n):
    strlst.append(list(input()))


for str in strlst:
    l = len(str)
    hl = l//2
    flag = [1,2,2]
    # abcba
      
    
    '''  [팰린드롬, 유사p tail, 유사p head]
    axbcba 
    a    a [1,2,2]
     x  b  [0,1,1] 
      b b  [-1,1,0]
       cc  [-2,1,-1]

    '''

    for i in range(hl+1):
        if l == 3:
            if str[0] != str[2]:
                if str[0] == str[1] or str[1] == str[2]:
                    flag[0] = 0
                else:
                    flag[0] = 0
                    flag[1] = 0
                    flag[2] = 0
            break
        if l == 4 and i == hl:
            break

        tail = str[i]
        head = str[-i-1]
        if flag[1] !=2:
            phead = str[-i-2]
        else:
            phead = str[-i-1]
        if flag[2] != 2:
            ptail = str[i+1]
        else:
            ptail = str[i]

        if head != tail:
            flag[0] -=1
        if phead != tail:
            flag[1] -=1
        if ptail != head:
            flag[2] -= 1
        if max(flag) < 0:
            break

    if flag[0] == 1:
        print(0)
    elif flag[1] > 0 or flag[2] > 0:
        print(1)
    else:
        print(2)