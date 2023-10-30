'''
투포인터
'''

n,k = list(map(int,input().split()))
table = [0]*1000001
mx = 0
for i in range(n):
    g,x = list(map(int,input().split()))
    mx = max(mx,x)
    table[x] += g
init = sum(table[:k*2+1])
res = init
for i in range(k,min(mx,1000001-k-1)):
    res = max(init,res)
    l = table[i-k]
    r = table[i+k+1]
    init -= l
    init += r
res = max(init,res)
print(res)