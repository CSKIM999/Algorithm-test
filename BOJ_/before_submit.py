import sys
input = sys.stdin.readline
N = int(input())
data = []
for i in range(N):
    a,b = map(int,input().split())
    data.append([a,b])
data.sort()
X = [i[1] for i in data]
index = 0
dp = [0]
for i in X:
    if dp[index]<i:
        dp.append(i)
        index +=1
        continue
    for j in range(index,-1,-1):
        if dp[j] < i:
            dp[j+1] = i
            break
print(N-index)