from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q1019
#######  TODAY  #######
##### 2022. 06. 07 #####
GIVEN ) 자연수 N 이 주어진다.
        어느 N 페이지로 된 책이 있을 때 각 숫자가 사용되는 횟수를 출력하라
INPUT ) 첫째 줄에 N ( 1,000,000,000 보다 작거나 같은 자연수 ) 가 주어진다
OUTPUT) 첫째 줄에 0~9 까지의 숫자가 각각 몇번씩 나오는지 구분하여 출력하라
Approach ) 당연히 for문 돌리면 무쬑건 타임아웃 분명 공식이 있음  
'''
import sys
sys.setrecursionlimit(25000)
# input = sys.stdin.readline
lst = [0]*10
lst[0] = -1
#  100,000,000 라고 생각해보자




TotalDP = []
node = 1
for i in range(2,11):
    node *= 10
    temp = [[0]*10 for _ in range(10)]
    tp = f"{(i-1)*(10**(i-2))}"
    basicNode = int(tp)
    for j in range(10):
        for k in range(10):
            if j == 0:
                if i == 2:
                    temp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                    break
                temp[0] = TotalDP[i-3][-1][:]
                break
            if k == j:
                temp[j][k] += node+basicNode+temp[j-1][k]
            else:
                temp[j][k] += basicNode+temp[j-1][k]
    TotalDP.append(temp[:])

# dp 생성 완료
N = 999
L = len(str(N))
rtTable = [0]*10
b4 = 0
for i in list(str(N)):
    L -= 1
    num = int(i)
    if L == 0:
        for k in range(1,num+1):
            rtTable[k] += 1
            if b4:
                rtTable[b4] +=1
        break
    temp = TotalDP[L-1][num-1][:]
    temp[0] += L
    temp[num] += 1
    for j in range(10):
        rtTable[j] += temp[j]
    b4 = num
print(rtTable)