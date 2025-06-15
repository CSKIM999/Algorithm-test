import sys
INF = 1e9
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[None] * (1 << n) for _ in range(n)]

def tsp(node: int, visited: int) -> int:
    if visited == (1 << n) - 1:
        return cost[node][0] if cost[node][0] else INF

    if dp[node][visited] is not None:
        return dp[node][visited]

    best = INF
    for nxt in range(1, n):
        if cost[node][nxt] and not (visited & (1 << nxt)):
            tmp = tsp(nxt, visited | (1 << nxt)) + cost[node][nxt]
            if tmp < best:
                best = tmp

    dp[node][visited] = best
    return best

print(tsp(0, 1))
