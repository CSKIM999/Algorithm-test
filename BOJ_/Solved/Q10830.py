import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q10830
#######  TODAY  #######
##### 2023. 02. 15 #####
GIVEN ) 행렬제곱

INPUT ) 

OUTPUT) 

Approach )  
'''
input = sys.stdin.readline


class matrix:
    def __init__(self):
        self.number = 0
        self.mat = {}
        self.hist = {0: {}}
        self.E = {}

    def set(self, number, arr):
        self.number = number
        self.E = {i: {} for i in range(number)}
        self.mat = {i: {} for i in range(number)}
        self.hist[0] = {i: {} for i in range(number)}
        for i in range(number):
            for j in range(number):
                if i == j:
                    self.E[i][j] = 1
                else:
                    self.E[i][j] = 0
                self.mat[i][j] = arr[i][j]
                self.hist[0][i][j] = arr[i][j]

    def exp(self, count):
        number = self.number
        self.count = count
        for v in range(count):
            ver = {i: {} for i in range(number)}
            for i in range(number):
                for j in range(number):
                    temp = 0
                    for k in range(number):
                        temp += self.hist[v][i][k]*self.hist[v][k][j]
                    ver[i][j] = temp % 1000000
            self.hist[v+1] = ver

    def calcul(self, alpha, beta):
        number = self.number
        ver = {i: {} for i in range(number)}
        for i in range(number):
            for j in range(number):
                temp = 0
                for k in range(number):
                    temp += alpha[i][k]*beta[k][j]
                ver[i][j] = temp % 1000000
        return ver

    def play(self, array):
        i = 0
        body = {}
        number = self.number
        for item in array:
            if i == 0:
                body = self.calcul(self.E, self.hist[item])
                i += 1
            else:
                body = self.calcul(body, self.hist[item])
        for i in range(number):
            print(" ".join([str(body[i][j] % 1000) for j in body[i]]))


n, k = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

a = matrix()
a.set(n, arr)
arr = []
count = 0
while True:
    if k < 2**count:
        break
    count += 1
count -= 1
newK = k
while newK > 0:
    for j in range(count, -1, -1):
        if newK >= 2**j:
            arr.append(j)
            newK -= 2**j
            break

arr.sort()

a.exp(count)
a.play(arr)

'''
1000 이상의 원소에서 1000의 자리 초과는 어차피 정답에 영향을 안줘서 %1000해준다는 아이디어가 있긴 했으나,
첫 적용에서 오류가 생기길래 안되는갑다 지레짐작해버림.

하지만 첫 적용에서 거듭제곱값이 달라서 생긴 문제였던거임 ㅋㅋ
'''
