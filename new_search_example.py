############################################  Q7 _ 럭키 스트레이트  ############################################
'''
Given ) 럭키 스트레이트는 특정 조건 만족할 경우만 발동한다
        특정 조건이란 현재 캐릭터의 점수 : N 에서 자릿수를 기준으로 점수 N 을 반으로 나누어 
        왼쪽부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합이 같을때를 의미한다.
        ex ) N = 123,402 일 경우 왼쪽의 합 6 오른쪽의 합 6 이므로 럭키스트레이트 발동 조건을 만족한다
Input ) 첫째 줄에 점수 N 이 정수로 주어진다.( 10<= N <= 99,999,999 ) 단, 점수 N 의 자릿수는 항상 짝수로 주어진다
Output) 첫째 줄에 럭키스트레이트 발동 가능할 경우 "LUCKY" 를 불가능할경우 "READY" 를 출력한다
'''

# # data = '123402'
# data = input()

# def LS(data):
#     half = len(data)/2
#     s = 0
#     for i in range(len(data)):
#         if i < half:
#             s -= int(data[i])
#         else:
#             s += int(data[i])
#     if s == 0:
#         print('LUCKY')
#     else:
#         print('READY')
# LS(data)
'''
1회차 > 상당히 쉬운 문제같다. BOJ 에서는 효율성테스트가 없어서 간단히 패스했으나 해답을 봐야 확실할 듯
'''

############################################  Q8 _ 문자열 재정렬  ############################################
'''
Given ) 알파벳 대문자와 숫자로 이루어진 문자열이 주어진다. 여기서 알파벳은 오름차순 정렬, 숫자는 모두 더해서 알파벳 뒤에 출력하라
Input ) 하나의 문자열 S 가 주어진다. (( 1 <= S <= 10,000 ))
Output) 요구 정답 출력
'''
# count = 0
# lst = []
# data = 'K1KA5CB7'
# for i in range(len(data)):
#     if data[i].isdigit() == True:
#         count+=int(data[i])
#     else:
#        lst.append(data[i]) 
# lst.sort()
# lst.append(str(count))
# print(''.join(lst))

'''
1회차>> isdigit // isalpha 를 들어는 봤는데 사용은 처음해본다. 그리고 join메서드도 처음 사용해본다.
추가로 join 메서드는 list 안에 모든 값이 같은 타입이어야 join 이 되는듯 하다.
'''


############################################  Q9 _ 문자열 압축  ############################################
'''
Given ) 임의의 문자열 S 가 주어진다 해당 문자열을 압축하고자 한다
        'aabbaccc' 의 경우 '2a2ba3c' 와 같이 압축하고 해당 패턴은 맨 앞부터 n 개 자리의 문자열을 선택하기로 한다
        따라서 문자열 'abcabcabcdedede' 3개 자리로 압축할 경우 '3abcdedede' 가 되는것.
Output) 주어진 문자열에서 가장 짧게 압축한 문자열의 길이를 반환하라
'''


# data = 'abcabcabcabcdededededede'

# min_len = len(data)
# half_num = int(len(data)/2)
# for i in range(1,half_num+1): 
#     compare = ''
#     count = 1
#     code = data[0:i]
#     for now in range(i,len(data),i): 
#         now_code = data[now:now+i]
#         if code == now_code: 
#             count +=1
#             if now+i >= len(data):
#                 compare += '{}{}'.format(count,code)
#                 code = now_code
#                 count = 1
#                 continue
#         elif code !=now_code and count == 1:
#             compare += '{}'.format(code)
#             code = now_code
#         else: 
#             compare += '{}{}'.format(count,code)
#             code = now_code
#             count = 1
#         if now+i >= len(data):
#             compare += (data[now:len(data)])
#     min_len = min(min_len,len(compare))

# print(min_len)

'''
1회차 > 다른 사람의 해답을 보았을 때 나보다 더욱 간결했다. 2개의 함수를 만들어서 사용했다.
        하지만 나는 함수 없이 2중 for문을 사용했기때문에, 아마 그 코드보다는 더욱 복잡한 코드일 것이다.
        또한 시간도 30분의 제한시간을 갖는 문제이지만, 나는 약 80분에 걸쳐서 풀어냈다. 아직 갈 길이 멀다.

'''


############################################  Q10 _ 자물쇠와 열쇠  ############################################
'''
Given ) 자물쇠의 크기는 n*n 크기의 정사각 격자형태이고 특이한 모양의 열쇠는 m*m 크기의 정사각 격자이다.
        자물쇠의 영역을 벗어나더라도 영역 내의 홈이 정확히 일치하면 자물쇠를 열 수 있다.
        열쇠를 나타내는 2차원 배열 key 와 lock이 매개변수로 주어질 때 해당 열쇠로 열 수 있다면 True를
        불가능하다면 False 를 return 하도록 함수를 작성하라.
        Key 는 M*M (3<= M <= 20 , M 은 자연수) 크기의 2차원 배열
        lock 는 N*N (3<= M <= 20 , M 은 자연수) 크기의 2차원 배열
        언제나 M < N 이며, key 와 lock의 원소는 0 또는 1 로 이루어져 있고, 0은 홈부분 1은 돌기를 나타낸다
'''

m,n = 3,3


key = list([0]*m for _ in range(m))
lock = list(list([0]*(n) for _ in range(n)) for _ in range(9))
key = [[0,0,0],[1,0,0],[0,1,1]]
lck = [[1,1,1],[1,1,0],[1,0,1]]
print(lck+key)
def rotate(data):
    data_prime = list([0]*len(data) for _ in range(len(data)))
    for i in range(len(data)):

        for j in range(len(data)):
            data_prime[j][-i-1] = data[i][j]
    data = data_prime
    return data


# key = rotate(key)
# print(key)