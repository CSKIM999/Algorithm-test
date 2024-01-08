string = list(input())
stringLen = len(string)

def getStr(str):
    temp = ''
    operation = ''
    for i in str:
        if i in ['*','/','+','-']:
            operation += i
        else:
            temp += i
    return temp, operation

def calcul(arr):
    mult = []
    hand =''
    Flag = False
    for i in arr: # 곱셈먼저
        if i in ['*','/','+','-']: # 연산자 체크
            if i in ['*','/']: # 곱셈의 경우
                hand = i
                Flag = True
            else: # 덧셈의 경우
                mult.append(i)
        else: # 숫자
            if Flag:
                last = mult.pop()
                mult.append(last+i+hand)
                # l,lo = getStr(last)
                # n,no = getStr(i)
                # new = l + n
                # newO = lo + no + hand
                # mult.append(new+newO)
                Flag = False
            else:
                mult.append(i)
    temp = []
    for i in mult:
        if i in ['*','/','+','-']: # 연산자 체크
            if i in ['+','-']: # 덧셈의 경우
                hand = i
                Flag = True
            else: # 없겠지만 곱셈의 경우
                pass
        else: # 숫자
            if Flag:
                last = temp.pop()
                temp.append(last+i+hand)
                # l,lo = getStr(last)
                # n,no = getStr(i)
                # new = l + n
                # newO = lo + no + hand
                # temp.append(new+newO)
                Flag = False
            else:
                temp.append(i)
    return temp


def stack():
    global i
    arr = []
    while True:
        if i >= stringLen or string[i] == ')':
            i+=1
            break
        if string[i] == '(':
            i += 1
            section = stack()
            arr.append(section)
        else:
            arr.append(string[i])
            i += 1

    arr = calcul(arr)
    return arr[0]
i = 0
print(stack())