def solution(A, K):
    # write your code in Python 3.6
    bottom, top = min(A), max(A)
    alpha = top - bottom
    for i in range(len(A)-K+1):
        temp = A[i:i+K]
        if bottom not in temp and top not in temp:
            continue
        B = A[:i]+A[i+K+1:]
        alpha = min(alpha, max(B)-min(B))

    return alpha


a = [3, 5, 1, 3, 9, 8]
k = 4

print(solution(a,k))