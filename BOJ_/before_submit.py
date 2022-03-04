import sys
input = sys.stdin.readline
key = 1000000
dp = [0]*5001
dp[1],dp[2] = 1,2
for i in range(3,5001):
    dp[i] = dp[i-1]+dp[i-2]
x = list(str(input().strip()))
c = 1
flag = False
temp = []
for k in range(len(x)):
    i = x[k]
    if 1<=int(i)<=2:
        c+=1
        flag = True
    elif int(i) == 0:
        if k==0 or not 1<=int(x[k-1])<=2:
            flag = False
            temp = [0]
            break
        if c>2:
            c -= 2
        else:
            c=1
        temp.append(c)
        c = 1
        flag= False
    else:
        if 6<int(i) and k>0 and x[k-1]=='2':
            c-=1
        if flag:
            temp.append(c)
        c = 1
        flag = False
if flag:
    temp.append(c-1)
elif not temp and len(x) > 0:
    temp.append(1)
result = 0
if temp[0] != 0:
    result = dp[temp[0]]
    for t in temp[1:]:
        if t>100:
          for i in range(len(dp),t+1):
            dp[i] = dp[i-1]+dp[i-2]
        result *= dp[t]

print(result%key)
    