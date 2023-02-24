'''
제한이 타이트하지 않아서 정확한 구현이 포인트가 될듯 함.
트라이 구조로 모든 user_id를 세팅해주고
이후 banned_id 를 통해 경우의 수를 튜플로 set에 넣어서 체크하자
'''
from collections import deque
# 트라이 사용할 dic, 현재 체크할 string , string index, possibleIndex


def solution(user_id, banned_id):
    bl = len(banned_id)
    possible = [set() for _ in range(bl)]
    answer = 0
    dic = {}

    def dfs(d, banned, i, pi):
        nl = len(banned)
        if i >= nl:
            if -1 in d:
                for item in d[-1]:
                    possible[pi].add(item)
            return
        now = banned[i]
        if now == '*':
            for x in d:
                if x == -1:
                    continue
                dfs(d[x], banned, i+1, pi)
        else:
            if now not in d:
                return
            dfs(d[now], banned, i+1, pi)

    def insertDic(d, string, i):
        sl = len(string)
        if sl <= i:
            if -1 not in d:
                d[-1] = set()
            d[-1].add(string)
            return
        now = string[i]

        if now not in d:
            d[now] = {}
        return insertDic(d[now], string, i+1)

    for ID in user_id:
        insertDic(dic, ID, 0)
    for index, BID in enumerate(banned_id):
        dfs(dic, BID, 0, index)

    q = deque()
    q.append([0, []])
    ans = set()

    while q:
        i, arr = q.popleft()
        if i >= bl:
            arr.sort()
            if tuple(arr) not in ans:
                ans.add(tuple(arr))
                answer += 1
            continue

        for j in possible[i]:
            if j not in arr:
                newArr = arr[:]
                newArr.append(j)
                q.append([i+1, newArr[:]])

    return answer


'''
트라이 구현은 능숙해졌는데 line 23 에서 삐끗했다..
디테일한 예외 처리도 신경쓸 것.
'''
