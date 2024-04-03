def solution(n, s):
    c = s % n
    v = s // n
    if n>s:
        return [-1]
    answer = [v]*(n-c) + [v+1]*c
    return answer