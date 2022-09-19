from datetime import datetime, timedelta
import sys
from lib import xprint, Prepare_Coding_Test
Prepare_Coding_Test()
'''
BOJ_ QuestionNumber __ Q21942
#######  TODAY  #######
##### 2022. 07. 20 #####
GIVEN ) 로봇에 필요한 부품을 대여 및 반납할 땐 부품 대여장에 반드시 정보를 작성해야한다.
        대여기간을 초과하는 경우 1분당 벌금이 부과되며 대여장에 쓰이는 형식은 다음과 같다.
        yyyy-MM-dd hh:mm [부품 이름] [동아리 회원 닉네임]

        또한 부품을 대여할 때 지켜야하는 조건은 다음과 같다.
            1. 한 사람이 같은 종류의 부품을 두개 이상 대여하고있는 상태일 수 없다.
            2. 한 사람이 같은 시각에 서로 다른 종류의 부품들을 대여하는것이 가능하다.
            3. 같은 사람이더라도, 대여기간은 부품마다 별도로 적용된다.
INPUT ) 첫 번째 줄에 부품 대여장에 작성된 정보의 개수 N, 대여기간 L, 벌금 F이 공백으로 구분되어 주어진다.
        대여기간 형식은 DDD/hh:mm으로 DDD는 일, hh는 시간, mm은 분을 의미한다. (000/00:00 는 주어지지 않는다.)
        두 번째 줄부터 N + 1번째 줄까지 시간순으로 부품 대여장에 작성한 정보 (시각, 부품 이름 P, 회원 닉네임 M)이 공백으로 구분되어 주어진다.
        빌린 시각의 형식은 yyyy-MM-dd hh:mm으로 yyyy는 연도, MM는 월, dd는 일, hh는 시간, mm는 분을 의미한다. 이 문제에서 들어오는 연도는 항상 2021년도이다.
        부품 이름 P는 알파벳 소문자로만 이루어져 있다. 즉, 부품 이름에 공백이 없다.
        회원 닉네임 M은 알파벳 소문자와 숫자(0 ~ 9)로만 이루어져있다. 즉, 회원 닉네임에 공백이 없다.
OUTPUT) 벌금을 내야하는 사람들을 사전순으로 동아리 회원 닉네임 M와 내야하는 벌금을 한 줄씩 출력한다.
        만약 벌금을 내야하는 사람들이 없는 경우는 -1을 출력한다.
Approach )  대여정보 N 는 최대 8만개, DAY 는 최대 200 각 부품이름의 길이 최대 20자
            입력이 모두 끝나면 무조건 반납이 끝나게 된다.
            우선 벌금은 딕셔너리로 구현하자. key = ID , Value = 늦은시간(분) 새로운 ID 를 만날때마다 ID:0 을 추가하고 연체시마다 value 값에 늦은 시간 더해주기
            
n,l,f 입력받기 

l => 총시간(분) 으로 정제
패널티리스트 = []
i = 0
이름인덱스 = {}
n 번 돌리기
    현재날짜, 현재시간, 물품, 아이디 = 입력
    
    아이템 = 딕셔너리[아이디]

    첫방문?
        아이템 = 딕셔너리[아이디] = 딕셔너리
        패널티리스트.append(0)
        이름인덱스[아이디] = i
        i += 1


    
    트라이 #반납
        빌린날짜, 빌린시간 = 아이템[물품]
        현재날짜 - 빌린날짜, 현재시간 - 빌린시간 => 총 시간 (분) 계산
        만약 총시간 > l? # 연체
            인덱스 = 이름인덱스[아이디]
            패널티리스트[인덱스] += l - 총시간
        아니라면 #연체 아닌 반납
            del 딕셔너리[아이디][물품]
    캐치 #빌리는경우
        딕셔너리[아이디][물품] = [빌린날짜,빌린시간]

패널티리스트 heappop 쓰기

'''
# input = sys.stdin.readline

n, l, f = list(input().split())
n, f = map(int, [n, f])

l = list(l.split('/'))
d = int(l[0])*24*60
l = list(map(int, l[1].split(':')))
l = l[0]*60 + l[1] + d

dic = {}
plst = []
nameIndex = {}
i = 0
for _ in range(n):
    nowday, nowtime, p, name = list(input().split())
    nowday = list(map(int, nowday.split('-')))
    nowtime = list(map(int, nowtime.split(':')))
    nowday = datetime(nowday[0], nowday[1], nowday[2], nowtime[0], nowtime[1])

    try:
        items = dic[name]
    except KeyError:
        items = dic[name] = {}
        plst.append([0, name])
        nameIndex[name] = i
        i += 1

    try:
        bday = items[p]
        delta = (nowday-bday)
        btime = (delta.seconds // 60) + (delta.days * 60 * 24)
        if btime > l:
            Index = nameIndex[name]
            if plst[Index][1] != name:
                raise ValueError
            plst[Index][0] += btime - l
        del dic[name][p]

    except KeyError:
        dic[name][p] = nowday

plst.sort(key=lambda x: x[1])
flag = True
for a, b in plst:
    if not a:
        continue
    print(b, a*f)
    flag = False
if flag:
    print(-1)


'''
마지막 사전순 출력에서 한번 삐끗했다.
'''
