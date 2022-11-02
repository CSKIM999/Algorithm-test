n = 50000

dp = [0]*(n+1)
dp[1] = 1
for i in range(2, n+1):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(4, dp[i-j**2]+1)
print(dp[n])

dp = [0, 1]
for i in range(2, n + 1):
    target = 4
    for j in range(1, 50001):
        if j ** 2 > i:
            break
        target = min(target, dp[i - (j**2)])
    dp.append(target + 1)
print(dp[n])


dp = [0, 1]

for i in range(2, n+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[n])
