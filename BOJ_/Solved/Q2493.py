import sys
import bisect
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q2493
#######  TODAY  #######
##### 2022. 10. 12 #####
GIVEN ) >>> 탑 <<<
        일직선 상에 N 개의 높이가 서로 다른 탑 ( 500,000 이하의 자연수 )이 설치되어있다.
        각 탑은 왼쪽 방향으로 신호를 발사하여 가장 먼저 만나는 탑에서 수신된다.
        각 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지 알아내는 프로그램을 작성하라.
        만약 수신받는 탑이 없는 탑이라면 0 을 출력하라
INPUT ) 첫째 줄에 탑의 수 N ( 500,000 이하의 자연수)
        둘째 줄에 빈칸을 공백으로 놓인 순서대로 탑들의 높이 X ( 100,000,000 이하의 자연수 )
OUTPUT) 탑의 순서대로 각 번호의 탑에서 발신한 신호를 수신하는 탑의 번호를 공백을 구분으로 출력
Approach )  
자료구조 : 딕셔너리(키값 사용) + 리스트
for 알파 in 입력리스트
    딕셔너리 키 값 안에 현재 알파보다 큰 탑이 있는가?
    >> 현재 알파에서 보내는 신호를 받을 탑이 있는가?
    YES
        현재 알파보다 큰 탑 중 가장 작은 탑 탱고를 찾기
        딕셔너리 안에 탱고보다 작은 값들은 모두 제거
        # 이번에 들어갈 알파가 그 작은 값들을 모두 가릴것
        정답리스트의 알파인덱스에 탱고 밸류값을 넣기
        딕셔너리 안에 알파값을 넣기
    NO
        현재 딕셔너리 안에 값이 있는가?
        YES
            모두 제거 ( 가려지니까 )
        딕셔너리에 알파값 넣기
        정답리스트 알파인덱스에 0 넣기


딕셔너리 디자인
bisect 를 쓴다면 리스트로도 가능하지 않은가? 오히려 편하지 않은가?
key = 높이 ( 모든 탑은 서로 높이가 다르기때문에 ID이자 Value 로 쓸수있음 )
value = 인덱스



'''
sys.setrecursionlimit(25000)
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

dic = {}  # for save index by height
stack = []
answer = [0]*n
for index, tower in enumerate(lst):
    while stack:
        top = stack.pop()
        if top > tower:
            answer[index] = dic[top]+1
            dic[tower] = index
            stack.append(top)
            stack.append(tower)
            break

    if not stack:
        stack.append(tower)
        dic[tower] = index
        continue
print(answer)
