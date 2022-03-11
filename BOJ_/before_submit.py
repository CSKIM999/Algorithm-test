n = int(input())
tower = [[i+1 for i in range(n)],[],[]]
hist = []
def move(N,s,t):
    tower[s-1].pop()
    tower[t-1].append(N)
    hist.append([s,t])
def hanoi(N,s,v,t):
    if N ==1:
        move(1,s,t)
    else:
        hanoi(N-1,s,t,v)
        move(N,s,t)
        hanoi(N-1,v,s,t)
hanoi(n,1,2,3)
print(len(hist))
for a,b in hist:
    print(f"{a} {b}")