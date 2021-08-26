case = int(input())
n = []
data = []
move = []
move_data = [[] for _ in range(case)]
for i in range(case):
    n.append(int(input()))
    data.append(list(map(int,input().split())))
    move.append(int(input()))
    for j in range(move[i]):
        move_data[i].append(list(map(int,input().split())))

print(data)
print(move_data)
