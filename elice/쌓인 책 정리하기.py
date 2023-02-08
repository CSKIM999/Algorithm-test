'''
임의로 섞인 책을 순서대로 정렬하고싶다.
내가 할 수 있는 행동은 단 한가지, 책을 선택하고 가장 위로 올리는 것.
해당 행동만으로 책을 오름차순으로 정렬하는 최소횟수를 구하라.

책의 순서는 공백을 구분으로 한 문자열로 주어지며 중복값은 없다.
'''


# 정렬되지 않은 가장 큰 숫자 뒤에 정렬되지 않은 두번째 가장 큰 숫자
# pivot 과 flag 를 세우고 1부터 끝까지 순회.
# 정렬되지 않은 숫자를 발견하면 pivot 으로 삼음.
# pivot 이후에 pivot 보다 작은 수를 만나면 flag 와 max 처리
# pivot 보다 큰 수를 만나면 pivot 교체. flag 의 값이 답 최소 교체 횟수?
arr = list(map(int, input().split()))
pivot, flag = 0, 0
for index, item in enumerate(arr):
    index += 1

    if pivot == 0 and index != item:
        if pivot < item:
            pivot = item
    elif pivot != 0 and pivot > item:
        flag = max(flag, item)
    elif pivot != 0 and pivot < item:
        pivot = item

print(flag)

'''
운 좋게 pivot,flag 방식을 찾게 되었다.
무슨 규칙이 있을까 여러가지 예제를 만들어보다가
뭔가 저거같아서 풀어보니까 정답을 받을 수 있었음.
'''
