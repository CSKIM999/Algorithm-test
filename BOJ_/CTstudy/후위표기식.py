'''
재귀함수로 만들어서 반환하자

스트링을 우선 리스트로 만들고
괄호 체크로 가장 작은 단위부터 가야함
그래서 재귀함수 필요
맨 앞에서부터 연산자 찾기
연산자 만나면 해당 인덱스 체크
덧뺄 or 곱나 flag로 덧셈뺄셈인데 flag1 이 true 면 pass하기
flag2 가 더 우선

인덱스 구해서 해당 앞뒤 리터럴 순서대로 넣고 연산자 뒤에 붙이기
'''
"(A+B)*(C+D)-E"
data = list(input())
calmap = {
    "+":0,
    "-":1,
    "*":2,
    "/":3,
    0:"+",
    1:"-",
    2:'*',
    3:'/'
}
def slicing(l_st,index):
    rt = l_st[index-1]+l_st[index+1]+f"{calmap[l_st[index]]}"
    return l_st[:index-1] + [rt] + l_st[index+2:]

def calcul(lst):
    pmFlag,mdFlag = False,False
    ho = -1
    hoh = -1
    hot = 1e9
    l = len(lst)
    for i in range(l):
        now = lst[i]
        if (now == "+" or now =="-") and not pmFlag:
            pmFlag = i
        elif (now == '*' or now =="/") and not mdFlag:
            mdFlag = i
        elif now == '(' and ho != 0:
            if ho == -1:
                hoh = i
                ho = 0
            ho += 1
        elif now == ')' and ho != 0:
            ho -= 1
            if hot == 1e9:
                hot = i
            else:
                hot = max(hot,i)
            
    
    if hoh != -1:
        nlst = lst[hoh+1:hot]
        return lst[:hoh] + calcul(nlst) + lst[hot+1:]
    if mdFlag:
        return slicing(lst,mdFlag)
    
    return slicing(lst,pmFlag)



while len(data) > 1:
    data = calcul(data)
data = list(data[0])
string = ""

for i in range(len(data)):
    if data[i] in ["0","1","2","3"]:
        string += calmap[int(data[i])]
    else:
        string += data[i]

print(string)