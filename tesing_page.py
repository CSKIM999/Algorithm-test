import sys
sys.setrecursionlimit(60000)

def matrix_mult(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k]
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n//2)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(A, n-1)
        return matrix_mult(temp, A)

m = 1000000007
def solution(n):
    dp=[0 for _ in range(n+1)]
    dp[1],dp[2] =1,2
    if n==0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-2]+dp[i-1]
    answer = dp[-1]
    return answer

aa = [[1,1],[1,0]]
# print(solution(1000)%m)
print(matrix_pow(aa,100))