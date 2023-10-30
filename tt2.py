n,m = 4,4
lastAttack = {}
for i in range(n):
    for j in range(m):
        lastAttack[(i,j)] = 0

print(lastAttack)
print(lastAttack[(1,1)])