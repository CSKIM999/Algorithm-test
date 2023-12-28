# from lib import xprint,Prepare_Coding_Test
# Prepare_Coding_Test()
'''
~/Documents/GitHub/Algorithm-test/BOJ_ QuestionNumber __ Q2042
#######  TODAY  #######
##### 2023. 11. 24 #####
GIVEN ) 
어떤 변경이 빈번히 일어나는 수가 있다.
중간에 몇 개의 수를 변경하고 구간합을 구하고자 한다

INPUT ) 
첫째 줄에 수의 개수 N ( 1,000,000 이하의 자연수 ), M ( 10,000 이하의 자연수 ), K ( 10,000 이하의 자연수 )
둘째 줄부터 N+1 개의 줄에 숫자가 주어진다 
그 이후 
a,b,c 세 개의 정수가 주어지는데
a 가 1 인 경우 b번째 수를 c 로 바꾸고
a 가 2 인 경우 b번째 수 부터 c 번째 수 까지의 구간합을 구하면 된다.
OUTPUT) 

Approach )  
세그먼트 트리 실습

'''
# import sys
# sys.setrecursionlimit(25000)
# input = sys.stdin.readline
n,m,k = list(map(int,input().split()))


lst = []
func = []
for _ in range(n):
    lst.append(int(input()))
for _ in range(m+k):
    func.append(list(map(int,input().split())))

table = [0 for _ in range((2**n)+2)]


def merge(l,r):
    return l+r

def setTree(arr,target,start,end):
    if (start == end):
        arr[target] = lst[start]
        return arr[target]
    
    mid = (start+end) // 2 
    left = setTree(arr,2*target,start,mid)
    right = setTree(arr,2*target+1,mid+1,end)
    arr[target] = merge(left,right)
    
    return arr[target]

def getTree(start,end,target,left,right):
    if (end<left or start > right):
        return 0
    if (start <= left and right <= end):
        return table[target]
    
    mid = left+ (right-left)//2
    lv = getTree(start,end,2*target,left,mid)
    rv = getTree(start,end,2*target+1,mid+1,right)
    return merge(lv,rv)

def putTree(idx,value,target,left,right):
    if (idx<left or idx>right):
        return table[target]
    
    if (left == right):
        table[target] = value
        return table[target]
    
    mid = left + (right - left) // 2
    lv = putTree(idx,value,2*target,left,mid)
    rv = putTree(idx,value,2*target+1,mid+1,right)
    table[target] = merge(lv,rv)
    return table[target]

setTree(table,1,0,len(lst)-1)

for a,b,c in func:
    if a == 1:
        putTree(b,c,1,0,len(lst)-1)
    else:
        print(getTree(b,c,1,0,len(lst)-1))
