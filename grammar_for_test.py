########### 리스트 초기화 ###########
# array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# array[1][1] = 'kkk'

# print(array)
# print('')

# n,m = 3,4
# array=[[0]*m]*n
# print(array)
# print('')
# array[1][1] = 'kkk'
# print(array)
# print('')

# """
# 리스트를 초기화 할 땐 
# array =[[0]*m for _ in range(n)] 와 같은 리스트 컴프리헨션을 사용해야함.
# 만약 위와같이 초기화 할 경우 리스트는 
# A=[0,0,0,0] & array = [A , A , A] 와 같이 저장되어버림.
# 따라서 array[1][1]='kkk' 의 경우 나는 2행 A의 2열의 값을 지정했지만
# Python은 3행 모두 A 라는 객채로 보기때문에 모든 A 행의 2열 값이 'kkk' 로 바뀌어버리는 것이다.

# 하지만 리스트컴프리헨션의 경우
# A=[0,0,0,0] & array = [A1 , A2 , A2] 
# 와 같이 저장되고 따라서 내가 만약
# array[1][1]='kkk' 와 같이 2행 A의 2열의 값을 지정한다면
# Python 내에서 A2의 2열값을 지정하는것이므로 다른 행에는 영향을 미치지 않는다.
# """


########### 리스트 관련 메소드 ###########
# a=[1,2,3,5,4,5,6]
# a.remove(4)  # 확인할 수 있듯이 remove 메서드는 인덱스 값이 아닌 데이터값을 삭제함.
# print(a)


a=[1,2,3,4,5,5,6,5]
a.remove(5)   #실행시켜 볼 경우 맨 앞의 5만 없애는것을 확인 할 수 있음 따라서 모든 값을 지우기위해선
print(a)      #컴프리헨션을 사용하는것이 빠르다
print('')
RemoveSet={3,5}
result = [i for i in a if i not  in RemoveSet]
print(result)