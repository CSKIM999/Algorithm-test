# import sys
# sys.setrecursionlimit(1000000)


# def solution(words):
#     dic = {}
#     answer = 0

#     def insert(d, v):
#         if v == "":
#             return
#         now = v[0]
#         try:
#             d[now][-1] += 1
#             insert(d[now], v[1:])
#         except KeyError:
#             d[now] = {-1: 1}
#             insert(d[now], v[1:])

#     def check(d, v, depth=0):
#         if v == "":
#             return depth
#         now = v[0]
#         if d[now][-1] == 1:
#             return depth+1
#         else:
#             return check(d[now], v[1:], depth+1)
#     for i in words:
#         insert(dic, i)
#     for i in words:
#         if len(i) == 1:
#             answer += 1
#         else:
#             answer += check(dic, i)

#     return answer


words = ["abc", "def", "ghi", "jklm"]


class trie:
    def __init__(self):
        self.root = {}

    def insert(self, string):
        cur_node = self.root
        for current in string:
            if current not in cur_node:
                cur_node[current] = {"count": 0}
            cur_node[current]["count"] += 1
            cur_node = cur_node[current]

    def check(self, string):
        cur_node = self.root
        count = 0
        for current in string:
            cur_node = cur_node[current]
            count += 1
            if cur_node["count"] == 1:
                return count
        return count


def solution(words):
    answer = 0
    t = trie()
    for word in words:
        t.insert(word)
    for word in words:
        answer += t.check(word)

    return answer


print(solution(words))


'''
처음엔 딕셔너리로 트라이처럼 구현하고
두번째론 클래스로 트라이를 구현했는데,
처음은 시간초과, 두번째엔 넉넉히 정답을 받았다.

찾아보니 트라이를 구현하는 데에는 클래스가 적절하다고 한다.
딕셔너리 + 재귀에서 먼저 딕셔너리는 공간복잡성의 오버헤드를,
재귀는 시간복잡성에서의 오버헤드를 유발할 수 있다고 한다.

재귀가 호출될 때 마다 콜스택에 함수가 쌓이는 과정에서
함수의 상태와 인수를 추적하기 위해 작은 누수를,
매 재귀마다 콜스택에 함수를 쌓아야하기 때문에 고차로 올라갈수록
성능의 저하로 인한 시간복잡도 저하가 야기됨.

그에 비해 For 문은 재귀에 비해 오버헤드가 "훨씬" 낮고
큰 입력에서 특히나 재귀와의 차이가 현격히 벌어짐.
'''
