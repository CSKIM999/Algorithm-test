class queen:
    def __init__(self, n):
        self.limit = n
        self.occup = [[0 for _ in range(n+1)] for _ in range(n+1)]
        self.oy = []
        self.res = 0

    def occx(self, x, y, flag):  # flag True 시 생성, False 시 삭제
        n = self.limit
        if flag:
            self.occup[x][y] += 1
        else:
            self.occup[x][y] -= 1

        for i in range(1, n):
            for nx, ny in [(x+i, y+i), (x-i, y+i), (x+i, y-i), (x-i, y-i)]:
                if 0 <= nx < n and 0 <= ny < n:
                    if flag:
                        self.occup[nx][ny] += 1
                    else:
                        self.occup[nx][ny] -= 1

    def play(self):

        n = self.limit
        depth = len(self.oy)
        if depth == n:
            self.res += 1
            return
        for i in range(n):
            if i not in self.oy and self.occup[depth][i] == 0:
                self.oy.append(i)
                self.occx(depth, i, True)
                self.play()
                self.oy.pop()
                self.occx(depth, i, False)

    def answer(self):
        return self.res


def solution(n):
    # task = queen(n)
    # task.play()
    # answer = task.answer()
    occup = [[0 for _ in range(n+1)] for _ in range(n+1)]
    oy = []
    res = 0

    def occx(x, y, flag):  # flag True 시 생성, False 시 삭제
        if flag:
            occup[x][y] += 1
        else:
            occup[x][y] -= 1

        for i in range(1, n):
            for nx, ny in [(x+i, y+i), (x+i, y-i)]:
                if 0 <= nx < n and 0 <= ny < n:
                    if flag:
                        occup[nx][ny] += 1
                    else:
                        occup[nx][ny] -= 1

    def play():
        nonlocal res
        depth = len(oy)
        if depth == n:
            res += 1
            return
        for i in range(n):
            if i not in oy and occup[depth][i] == 0:
                oy.append(i)
                occx(depth, i, True)
                play()
                oy.pop()
                occx(depth, i, False)
    play()
    answer = res
    print(answer)
    return answer
