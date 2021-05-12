########### 동전 거슬러주기 ###########

# n = 1260
# count = 0

# coin_types=[500,100,50,10]
# for coin in coin_types:
#     count+=n//coin
#     n%=coin


# print(count)


########### N,M,K 큰수의 법칙 ###########
# m, k=map(int,input().split())
# data = list(map(int,input().split()))

# n = len(data)
# data.sort()
# result = 0
# count = 0
# for i in range(m):
#     if count == k:
#         print('둘째 큰 값')
#         result += data[-2]
#         count = 0
#     else:
#         print('첫번째로 큰 값')
#         result += data[-1]
#         count +=1

# print('총합은 :' + str(result))
    


########### 숫자 카드 게임 ###########
# n = int(input())
# result = []
# for i in range(n):
#     data = list(map(int,input().split()))
#     data.sort()
#     result.append(data[0])
# result.sort()
# print(result[-1])


########### 1이 될 때 까지 ###########
n, k = map(int,input().split())
count = 0
while True:
    if n % k !=0:
        if n == 1:
            break
        n -=1
        count +=1
        print('1'+ '  n :' +str(n))
    elif n != 0:
        n = n/k
        count +=1
        print('2' + '  n :' +str(n))
    
    else:
        print('END')
        break

print(count)