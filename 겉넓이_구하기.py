
'''
바닥을 제외한 정면, 평면, 배면, 우측면, 좌측면도 체크하기
평면은 무조건 n*m 일거고
나머지 4가지 체크해주면 될 듯

그리고 순회하려 했는데 그냥 가장 높은 거 행렬별로 찾아서 넣어주면 되는 듯 함
'''
n,m = list(map(int,input().split()))

table = [list(map(int,input().split())) for _ in range(n)]

# front,back = [0]*m,[0]*m
# left,right = [0]*n,[0]*n

# for i in range(n):
#     l,r = left[i],right[i]
#     for j in range(m):
#         now = table[i][j]
#         f,b = front[j], back[j]
#         if now > f:
#             front[j] = now
#         if now > b:
#             back[j] = now
#         if now > l:
#             left[i] = now
#         if now > r:
#             right[i] = now

# res = sum(left)+sum(right)+sum(front)+sum(back)+(m*n)*2
# print(left,right,front,back)
# print(res)

d = [[-1,0],[0,-1],[0,1],[1,0]]
res = (m*n)*2
while True:
    count = 0
    level = 0
    for i in range(n):
        for j in range(m):
            if level < table[i][j]:
                level = table[i][j]
            if table[i][j] <= 0:
                continue
            for k in range(4):
                nx,ny = i+d[k][0], j+d[k][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    count += 1
                    continue
                if table[nx][ny] <= 0:
                    count +=1
    
    for i in range(n):
        for j in range(m):
            table[i][j] -= 1
    if level == 0:
        break
    res += count

print(res)
            
