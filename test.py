test = [1,2,3,4,5,6,7,8,9]
l = len(test)
ll = l//2

p = test[ll:]
for i in range(0,ll):
    print(test[i])
print(p)