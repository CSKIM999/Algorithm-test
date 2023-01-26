import heapq as h


def solution(n, paths, gates, summits):
    hpush = h.heappush
    hpop = h.heappop
    dist = {i: [] for i in range(n+1)}
    for t, f, d in paths:
        dist[t].append((d, f))
        dist[f].append((d, t))
    summits.sort()
    checkSummits = {i for i in summits}
    gates = set(gates)

    def dijkstra(start):
        flag = 1e9
        temp = [1e9]*(n+1)
        q = [[0, start]]

        temp[start] = 0
        while q:
            point, node = hpop(q)
            if answer[1] != 1e9 and point >= answer[1]:
                continue
            if node in gates:
                if flag == 1e9:
                    flag = min(flag, point)
                    continue
                flag = min(flag, point)
                continue
            if flag != 1e9 and point > flag:
                continue

            if temp[node] < point:  # or end?
                continue
            for a, b in dist[node]:
                if b != start and b in checkSummits:
                    continue
                a = max(a, point)
                if temp[b] > a:
                    hpush(q, (a, b))
                    temp[b] = a

        return temp

    answer = [0, 1e9]
    for summit in summits:
        gtable = dijkstra(summit)
        m = min([gtable[i] for i in gates])
        if answer[1] != 1e9 and answer[1] <= m:
            continue
        answer = [summit, m]
    return answer


'''
line 9 언저리에서 gates 만 set 처리하고 
똑같이 in 확인해주는 summits 는 그대로 list 로 가져갔는데
정답처리 받았다.

원래 summits 도 빠르게 in 체크 가능하게 set 자료형을 쓰려했는디
list.sort() 가 list(set(list)) 와 다르게 나올수가 있나???
시간 초과가 아니라 오답판정이 나오는게 좀 의아하다.
'''
