# n nums of rows // k selected row //  ( 5 <= n <= 1,000,000 ) ,, 명령 갯수 200,000 이하
# U x // selectrow 의 X 칸 위에 있는 row 선택
# D x // 마찬가지
# C // selected row 삭제 후 바로 아래 row 선택. 만약 삭제행이 마지막 row 일경우 바로 윗행 선택
# Z 최근 삭제 행 복구

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
n = 8
k = 2



from collections import deque
def solution(n, k, cmd):
    q = deque(list(cmd))
    stack = deque()
    linkedList = [[i-1,i+1] if i!= 0 and i!=n-1 else [None,1] if i!=n-1 else [n-2,None] for i in range(n)]
    print(linkedList)
    selectedNode = k
    def cut(node):
        fr,bk = linkedList[node]
        stack.append(node)
        if fr == None:
            linkedList[bk][0] = None
            selectedNode = bk
        elif bk == None:
            linkedList[fr][1] = None
            selectedNode = fr
        else:
            linkedList[bk][0],linkedList[fr][1] = fr,bk
            selectedNode = bk
        return selectedNode

    def undo():
        node = stack.pop()
        fr,bk = linkedList[node]
        if fr == None or bk == None:
            if fr == None:
                linkedList[bk][0] = node
            else:
                linkedList[fr][1] = node
        else:
            linkedList[fr][1],linkedList[bk][0] = node,node

    def MU(node,num):
        now = node
        for i in range(num):
            now = linkedList[now][0]
        return now

    def MD(node,num):
        now = node
        for i in range(num):
            now = linkedList[now][1]
        return now
    while q:
        func = q.popleft().split()
        if len(func) >= 2:
            f,num = func[0],int(func[1])
            if f == 'D':
                selectedNode = MD(selectedNode,num)
            else:
                selectedNode = MU(selectedNode,num)
        else:
            f = func[0]
            if f == 'C':
                selectedNode = cut(selectedNode)
            else:
                undo()
    answer = ''
    count = 0
    stack = list(stack)
    # while count<n:
    #     pass
    stack.sort()
    for i in stack:
        o = "O"*(i - count) + 'X'
        count = i+1
        print(o)
        answer += o
    answer += 'O'*(n-count)
solution(n,k,cmd)