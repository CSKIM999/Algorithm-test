from lib import xprint,Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q16719
#######  TODAY  #######
##### 2022. 07. 22 #####
GIVEN ) 주어진 문자열을 "항상" 사전순 가장 앞으로 오도록 하고자한다.
        ZOAC 을 보여주고싶다면 A -> C -> O -> Z 순으로 추가해주면 된다.
INPUT ) 첫째 줄에 알파벳 대문자로 구성된 최대 100자의 문자열이 주어진다.
OUTPUT) 규칙에 맞게 문자열을 출력
Approach )  아스키코드와 힙큐 사용해서 구현하자
            힙큐로는 구현제약이 많이생김
            최대길이가 100인만큼 N^3 으로 짜도 백만번 연산.
            3번 순회로 결정
'''
import sys
# input = sys.stdin.readline

I = list(list(input().split())[0])
N = len(I)
dummy = ['' for _ in range(N)]
lst = []
dic = {}

for i in range(N):
    x = ord(I[i])
    try:
        dic[x].append(i)
    except KeyError:
        dic[x] = [i]
def AorB(A,B):
    a = list(''.join(A))
    b = list(''.join(B))
    for i in range(len(a)):
        if ord(a[i])==ord(b[i]):
            continue
        elif ord(a[i])>ord(b[i]):
            return B,False
        else:
            return A,True
    return A,True
for q in range(N):
    temp = dummy[:]
    for i in dic:
        for j in dic[i]:
            temp2 = dummy[:]
            if len(''.join(temp)) == q:
                temp[j] = chr(i)
                node = [i,j]
                continue
            
            temp2[j] = chr(i)

            temp,flag = AorB(temp,temp2)
            if not flag:
                node = [i,j]
                flag = True
    ndic = dic[node[0]]
    if len(ndic) == 1:
        del dic[node[0]]
    else:
        ndic.remove(node[1])
        dic[node[0]] = ndic
    
    dummy = temp[:]
    print(''.join(dummy))

'''
2트 PASS
문자열은 확실히 약한것같음 아스키코드를 백분활용해야할듯
ord 와 chr , 공백 chr(32)

def AorB(A,B):
    a = list(''.join(A))
    b = list(''.join(B))
    for i in range(len(a)):
        if ord(a[i])>ord(b[i]):
            continue
    return A,True

AorB 에서 중간 탈출 return A 를 넣지 않으니
AAB 와 ACA 의 경우 i == 1 일때 A와 C 가 비교되어 A 가 우선이지만 탈출하지 못하고 마지막 B,A 비교를 통해 ACA 가 선택됨
중간 탈출조건을 넣어주는것으로 정답판정

문자열의 최대길이가 100인것이 힌트였음

'''