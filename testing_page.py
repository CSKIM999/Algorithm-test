n = int(input())
data = []
for i in range(n*n):
    delta = (list(map(int,input().split())))
    data.append([delta[0],tuple(delta[1:5])])
    

print(data)