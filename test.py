def calcul(l, m, r):
    l, r = int(l), int(r)
    if m == "+":
        return l+r
    elif m == "-":
        return l-r
    elif m == "*":
        return l*r
    else:
        return l/r

# 순서가 있음. 괄호 - 나누기/곱셈 - 덧셈/뺄셈 순.
# 따라서 괄호 먼저 체크하고 이후 곱셉 이후 덧셈 체크


def define(array, grade):
    result = []
    a, b, c = None, None, None
    stack = []
    flag = 0
    if grade == 0:
        for i in array:
            if i == "(":
                flag += 1
                if flag == 1:
                    continue
            elif i == ")":
                flag -= 1
                if flag == 0:
                    for i in range(2):
                        stack = define(stack, i)
                    result.append(stack[0])
                    stack = []
                    continue
            if flag:
                stack.append(i)
            else:
                result.append(i)
        return result
    elif grade == 1:
        for i in array:
            if a == None:
                a = i
                continue
            elif b == None:
                if i == "+" or i == "-":
                    result.append(a)
                    result.append(i)
                    a = None
                    continue
                b = i
            elif c == None:
                c = i
                temp = calcul(a, b, c)
                a = temp
                b = None
                c = None
        result.append(a)
        if len(result) == 1:
            return result
        else:
            return define(result, 2)
    elif grade == 2:
        for i in array:
            if a == None:
                a = i
            elif b == None:
                b = i
            elif c == None:
                temp = calcul(a, b, i)
                a = temp
                b = None
        return [a]


g = ['(', ')', '-', '+', '/', '*']
test = "(1/6)"
arr = []
temp = ''
for i in test:
    if i in g:
        if temp:
            arr.append(int(temp))
            temp = ""
        arr.append(i)
    else:
        temp += i
if temp:
    arr.append(int(temp))
arr = define(arr, 0)
arr = define(arr, 1)
arr = define(arr, 2)
print(f"{arr[0]:.1f}")
