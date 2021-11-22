a = [[i]*3 for i in range(4)]
a[1][0:2] = [0]*(2-0)
print(a[1][0:2])
print(a)
