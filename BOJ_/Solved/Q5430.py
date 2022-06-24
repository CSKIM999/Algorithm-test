import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q5430
#######  TODAY  #######
##### 2022. 06. 24 #####
GIVEN ) 문자열 문제
        R,D 함수로 이루어진 프로그램이 있다.
        R은 Reverse // 뒤집기 D 는 Delete // 지우기 기능이다.
        만약 빈 Arr 에 D 기응이 호출되면 에러가 발생한다
        배열 초기값과 수행함수가 주어질 때 최종결과를 구하라
INPUT ) 첫째 줄에 100 이하의 TC 의 갯수  T 가 주어진다
        각 TC 의 첫째 줄에는 수행함수 p 가 주어진다. ( 1 <= p <= 100,000 )
        다음 줄에는 배열에 들어있는 수의 개수 n 이 주어진다 ( 1<= n <= 100,000 )
        그 다음줄에는 숫자의 배열이 주어진다 각 원소는 100 이하의 자연수


OUTPUT) 각 TC 에 대해서 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력하라. 만약 에러가 발생하면 error 를 출력하라
Approach )
R 플래그 = 0
함수입력 = 배열
앞빼기, 뒷빼기 = 배열,배열
빼기합 = 0
for 함수원소 in 함수입력
    뒤집기라면?
        R플래그 반대로
    빼기라면?

        만약 R플래그 0
            앞빼기 +=1
            빼기합 +=1
        아니라면
            뒷빼기 +=1
            빼기합 +=1

        만약 빼기합 > 원소수
            에러출력
            탈출

새로운배열 = 합수입력[앞빼기:뒷빼기]
만약 R플래그 0
    출력 새로운배열
아니라면
    출력 새로운배열 뒤집기

'''
sys.setrecursionlimit(25000)
# input = sys.stdin.readline

T = int(input())
Tr = []
for _ in range(T):

    func = list(input())
    N = int(input())
    arrInput = input().strip()[1:-1]
    if N>0:
        arr = arrInput.split(',')
        arr = list(map(int,arr))
    else:
        arr = []

    flag = True
    rflag = True
    fm, bm, tm = 0, 0, 0
    res = []
    for f in func:
        if f == 'R':
            flag = not flag
        else:
            if flag:
                fm += 1
                tm +=1
            else:
                bm +=1
                tm +=1
        if tm>N:
            # print('error')
            Tr.append('error')
            rflag = False
            break
    if rflag:
        if bm!= 0:
            res =arr[fm:-bm]
        else:
            res = arr[fm:]
        if not flag:
            res.reverse()
        print(str(res).replace(' ',''))
'''
맞구만 ㅅㅂ 리스트 사이에 공백있다고 오답처리하는 븅신문제
'''